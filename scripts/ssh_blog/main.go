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
		m.list.SetSize(msg.Width, msg.Height)
		m.vp.Width, m.vp.Height = msg.Width, msg.Height-1
		if m.reading != nil {
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
	if !strings.HasPrefix(strings.TrimSpace(md), "# ") {
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

func newServer(addr, hostKey string, posts []post) (*ssh.Server, error) {
	return wish.NewServer(
		wish.WithAddress(addr),
		wish.WithHostKeyPath(hostKey),
		wish.WithIdleTimeout(15*time.Minute),
		wish.WithMaxTimeout(time.Hour),
		wish.WithMiddleware(
			bm.Middleware(func(s ssh.Session) (tea.Model, []tea.ProgramOption) {
				return newModel(posts, bm.MakeRenderer(s)), []tea.ProgramOption{tea.WithAltScreen()}
			}),
			activeterm.Middleware(),
			logging.Middleware(),
		),
	)
}

func main() {
	addr := flag.String("addr", "localhost:2222", "listen address")
	root := flag.String("site", "../..", "blog repo root (hugo.toml, content/)")
	hostKey := flag.String("host-key", ".host_key/ed25519", "host key path, created if missing")
	flag.Parse()

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
