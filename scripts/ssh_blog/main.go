// Serves the blog over SSH: ssh -p 2222 localhost
package main

import (
	"context"
	"errors"
	"flag"
	"fmt"
	"log"
	"os"
	"os/signal"
	"strings"
	"syscall"
	"time"

	"charm.land/bubbles/v2/key"
	"charm.land/bubbles/v2/list"
	"charm.land/bubbles/v2/viewport"
	tea "charm.land/bubbletea/v2"
	"charm.land/glamour/v2"
	"charm.land/lipgloss/v2"
	"charm.land/ssh"
	"charm.land/wish/v2"
	"charm.land/wish/v2/activeterm"
	bm "charm.land/wish/v2/bubbletea"
	"charm.land/wish/v2/logging"
	gossh "golang.org/x/crypto/ssh"
)

type model struct {
	list    list.Model
	sublist *list.Model
	vp      viewport.Model
	reading *post
	dark    bool
	footer  lipgloss.Style
}

func newList(title string, posts []post, quitHelp string) list.Model {
	items := make([]list.Item, len(posts))
	for i, p := range posts {
		items[i] = item{p}
	}
	l := list.New(items, list.NewDefaultDelegate(), 0, 0)
	l.Title = title
	l.KeyMap.Quit = key.NewBinding(key.WithKeys("q", "esc"), key.WithHelp("q", quitHelp))
	return l
}

func newModel(posts []post) model {
	return model{
		list:   newList("blog.tobked.dev", posts, "quit"),
		vp:     viewport.New(),
		dark:   true,
		footer: lipgloss.NewStyle().Faint(true),
	}
}

func (m model) open(p post) model {
	if len(p.subpages) > 0 {
		sub := newList(p.Title+" · "+siteURL+p.Path, p.subpages, "back")
		sub.SetSize(m.list.Width(), m.list.Height())
		m.sublist = &sub
		return m
	}
	m.reading = &p
	m.vp.SetContent(m.render(p))
	m.vp.GotoTop()
	return m
}

func (m model) Init() tea.Cmd { return tea.RequestBackgroundColor }

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.BackgroundColorMsg:
		m.dark = msg.IsDark()
		if m.reading != nil {
			m.vp.SetContent(m.render(*m.reading))
		}
		return m, nil
	case tea.WindowSizeMsg:
		// The client picks its size; the views allocate width×height cells.
		msg.Width, msg.Height = min(msg.Width, 300), min(msg.Height, 150)
		m.list.SetSize(msg.Width, msg.Height)
		if m.sublist != nil {
			m.sublist.SetSize(msg.Width, msg.Height)
		}
		rewrap := msg.Width != m.vp.Width()
		m.vp.SetWidth(msg.Width)
		m.vp.SetHeight(msg.Height - 1)
		if m.reading != nil && rewrap {
			m.vp.SetContent(m.render(*m.reading))
		}
		return m, nil
	case tea.KeyPressMsg:
		if m.reading != nil {
			switch msg.String() {
			case "q", "esc", "backspace", "left", "h":
				m.reading = nil
				return m, nil
			case "g", "home":
				m.vp.GotoTop()
				return m, nil
			case "G", "end":
				m.vp.GotoBottom()
				return m, nil
			case "ctrl+c":
				return m, tea.Quit
			}
			var cmd tea.Cmd
			m.vp, cmd = m.vp.Update(msg)
			return m, cmd
		}
		if m.sublist != nil {
			if m.sublist.FilterState() != list.Filtering {
				switch msg.String() {
				case "enter":
					if it, ok := m.sublist.SelectedItem().(item); ok {
						m = m.open(it.p)
					}
					return m, nil
				case "q", "backspace":
					m.sublist = nil
					return m, nil
				case "esc":
					if m.sublist.FilterState() == list.Unfiltered {
						m.sublist = nil
						return m, nil
					}
				case "left", "h":
					if m.sublist.Paginator.Page == 0 {
						m.sublist = nil
						return m, nil
					}
				}
			}
			var cmd tea.Cmd
			*m.sublist, cmd = m.sublist.Update(msg)
			return m, cmd
		}
		if msg.String() == "enter" && m.list.FilterState() != list.Filtering {
			if it, ok := m.list.SelectedItem().(item); ok {
				m = m.open(it.p)
			}
			return m, nil
		}
	}
	var cmd tea.Cmd
	m.list, cmd = m.list.Update(msg)
	return m, cmd
}

func (m model) render(p post) string {
	style := "light"
	if m.dark {
		style = "dark"
	}
	r, err := glamour.NewTermRenderer(
		glamour.WithStandardStyle(style),
		glamour.WithWordWrap(min(m.vp.Width(), 100)-4),
	)
	if err != nil {
		return err.Error()
	}
	md := p.Body
	if first, _, _ := strings.Cut(strings.TrimSpace(md), "\n"); strings.TrimSpace(first) != "# "+p.Title {
		md = "# " + p.Title + "\n\n" + md
	}
	head := siteURL + p.Path
	if !p.page {
		head = p.day() + " · " + head
	}
	md = "*" + head + "*\n\n" + md
	out, err := r.Render(md)
	if err != nil {
		return err.Error()
	}
	return out
}

func (m model) View() tea.View {
	s := m.list.View()
	if m.sublist != nil {
		s = m.sublist.View()
	}
	if m.reading != nil {
		s = m.vp.View() + "\n" + m.footer.Render(fmt.Sprintf(
			" ↑/↓/j/k scroll · g/G top/bottom · q/h back · %3.0f%%", m.vp.ScrollPercent()*100))
	}
	v := tea.NewView(s)
	v.AltScreen = true
	return v
}

// maxSessions caps open session channels, counted from the moment they open: each
// can buffer up to 2 MB, and one connection may open many.
var maxSessions = 50

// limitSessions replaces the default session handler to cap channels and env
// requests, which the ssh package would otherwise accept without limit.
func limitSessions(s *ssh.Server) error {
	sem := make(chan struct{}, maxSessions)
	s.ChannelHandlers = map[string]ssh.ChannelHandler{
		"session": func(srv *ssh.Server, conn *gossh.ServerConn, nc gossh.NewChannel, ctx ssh.Context) {
			select {
			case sem <- struct{}{}:
				defer func() { <-sem }()
				ssh.DefaultSessionHandler(srv, conn, limitEnv{nc}, ctx)
			default:
				nc.Reject(gossh.ResourceShortage, "Too many readers right now, try again in a minute.")
			}
		},
	}
	return nil
}

type limitEnv struct{ gossh.NewChannel }

func (c limitEnv) Accept() (gossh.Channel, <-chan *gossh.Request, error) {
	ch, reqs, err := c.NewChannel.Accept()
	if err != nil {
		return ch, reqs, err
	}
	out := make(chan *gossh.Request)
	go func() {
		defer close(out)
		n := 0
		for r := range reqs {
			if r.Type == "env" {
				if n++; n > 16 || len(r.Payload) > 256 {
					r.Reply(false, nil)
					continue
				}
			}
			out <- r
		}
	}()
	return ch, out, nil
}

func newServer(addr, hostKey string, posts []post) (*ssh.Server, error) {
	var key ssh.Option
	if pem := os.Getenv("SSH_HOST_KEY"); pem != "" {
		key = wish.WithHostKeyPEM([]byte(pem))
	} else {
		key = wish.WithHostKeyPath(hostKey)
	}
	// Middlewares run last to first: log, require a pty, then the app.
	return wish.NewServer(
		wish.WithAddress(addr),
		key,
		wish.WithIdleTimeout(10*time.Minute),
		wish.WithMaxTimeout(time.Hour),
		limitSessions,
		wish.WithMiddleware(
			bm.Middleware(func(s ssh.Session) (tea.Model, []tea.ProgramOption) {
				return newModel(posts), nil
			}),
			activeterm.Middleware(),
			logging.StructuredMiddleware(), // quotes control characters in client-supplied names
		),
	)
}

func main() {
	addr := flag.String("addr", "localhost:2222", "listen address")
	root := flag.String("site", "../..", "blog repo root (hugo.toml, content/)")
	hostKey := flag.String("host-key", ".host_key/ed25519", "host key path, created if missing")
	flag.Parse()
	if os.Getenv("FLY_APP_NAME") != "" && os.Getenv("SSH_HOST_KEY") == "" {
		log.Fatal("SSH_HOST_KEY is not set; refusing to start with a throwaway host key")
	}

	posts, err := loadSite(*root)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("loaded %d pages and posts", len(posts))

	s, err := newServer(*addr, *hostKey, posts)
	if err != nil {
		log.Fatal(err)
	}

	done := make(chan os.Signal, 1)
	signal.Notify(done, os.Interrupt, syscall.SIGTERM)
	log.Printf("listening on %s", *addr)
	go func() {
		if err := s.ListenAndServe(); err != nil && !errors.Is(err, ssh.ErrServerClosed) {
			log.Fatal(err)
		}
	}()
	<-done
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	_ = s.Shutdown(ctx)
}
