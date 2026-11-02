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

	"github.com/charmbracelet/bubbles/list"
	"github.com/charmbracelet/bubbles/viewport"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/glamour"
	"github.com/charmbracelet/lipgloss"
	"github.com/charmbracelet/ssh"
	"github.com/charmbracelet/wish"
	"github.com/charmbracelet/wish/activeterm"
	bm "github.com/charmbracelet/wish/bubbletea"
	"github.com/charmbracelet/wish/logging"
	gossh "golang.org/x/crypto/ssh"
)

type model struct {
	list     list.Model
	vp       viewport.Model
	reading  *post
	renderer *lipgloss.Renderer
	footer   lipgloss.Style
}

func newModel(posts []post, r *lipgloss.Renderer) model {
	items := make([]list.Item, len(posts))
	for i, p := range posts {
		items[i] = item{p}
	}
	l := list.New(items, list.NewDefaultDelegate(), 0, 0)
	l.Title = "blog.tobked.dev"
	return model{list: l, renderer: r, footer: r.NewStyle().Faint(true)}
}

func (m model) Init() tea.Cmd { return nil }

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		// The client picks its size; the views allocate width×height cells.
		msg.Width, msg.Height = min(msg.Width, 300), min(msg.Height, 150)
		m.list.SetSize(msg.Width, msg.Height)
		rewrap := msg.Width != m.vp.Width
		m.vp.Width, m.vp.Height = msg.Width, msg.Height-1
		if m.reading != nil && rewrap {
			m.vp.SetContent(m.render(*m.reading))
		}
		return m, nil
	case tea.KeyMsg:
		if m.reading != nil {
			switch msg.String() {
			case "q", "esc", "backspace", "left", "h":
				m.reading = nil
				return m, nil
			case "ctrl+c":
				return m, tea.Quit
			}
			var cmd tea.Cmd
			m.vp, cmd = m.vp.Update(msg)
			return m, cmd
		}
		if msg.String() == "enter" && m.list.FilterState() != list.Filtering {
			if it, ok := m.list.SelectedItem().(item); ok {
				p := it.p
				m.reading = &p
				m.vp.SetContent(m.render(p))
				m.vp.GotoTop()
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
	if m.renderer.HasDarkBackground() {
		style = "dark"
	}
	r, err := glamour.NewTermRenderer(
		glamour.WithStandardStyle(style),
		glamour.WithColorProfile(m.renderer.ColorProfile()),
		glamour.WithWordWrap(min(m.vp.Width, 100)-4),
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

func (m model) View() string {
	if m.reading == nil {
		return m.list.View()
	}
	return m.vp.View() + "\n" + m.footer.Render(fmt.Sprintf(
		" ↑/↓ scroll · q back · %3.0f%%", m.vp.ScrollPercent()*100))
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
				return newModel(posts, bm.MakeRenderer(s)), []tea.ProgramOption{tea.WithAltScreen()}
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
