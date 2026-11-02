package main

import (
	"bytes"
	"io"
	"net"
	"os"
	"path/filepath"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/charmbracelet/log"
	gossh "golang.org/x/crypto/ssh"
)

type syncBuf struct {
	mu sync.Mutex
	b  bytes.Buffer
}

func (s *syncBuf) Write(p []byte) (int, error) { s.mu.Lock(); defer s.mu.Unlock(); return s.b.Write(p) }
func (s *syncBuf) String() string              { s.mu.Lock(); defer s.mu.Unlock(); return s.b.String() }
func (s *syncBuf) Reset()                      { s.mu.Lock(); defer s.mu.Unlock(); s.b.Reset() }

func dial(t *testing.T, user string, posts []post) *gossh.Client {
	t.Helper()
	ln, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatal(err)
	}
	s, err := newServer(ln.Addr().String(), filepath.Join(t.TempDir(), "key"), posts)
	if err != nil {
		t.Fatal(err)
	}
	go s.Serve(ln)
	t.Cleanup(func() { s.Close() })
	c, err := gossh.Dial("tcp", ln.Addr().String(), &gossh.ClientConfig{
		User: user, HostKeyCallback: gossh.InsecureIgnoreHostKey(),
	})
	if err != nil {
		t.Fatal(err)
	}
	return c
}

// ptySession starts an interactive session like a real terminal would.
func ptySession(t *testing.T, c *gossh.Client) (*gossh.Session, io.Writer, *syncBuf) {
	t.Helper()
	sess, err := c.NewSession()
	if err != nil {
		t.Fatal(err)
	}
	if err := sess.RequestPty("xterm-256color", 40, 100, gossh.TerminalModes{}); err != nil {
		t.Fatal(err)
	}
	out := &syncBuf{}
	sess.Stdout, sess.Stderr = out, out
	in, _ := sess.StdinPipe()
	if err := sess.Shell(); err != nil {
		t.Fatal(err)
	}
	return sess, in, out
}

func waitFor(t *testing.T, out *syncBuf, want string) {
	t.Helper()
	for deadline := time.Now().Add(5 * time.Second); time.Now().Before(deadline); time.Sleep(50 * time.Millisecond) {
		if strings.Contains(out.String(), want) {
			return
		}
	}
	t.Fatalf("never saw %q in output:\n%s", want, out.String())
}

func TestBrowseAndReadOverSSH(t *testing.T) {
	posts := []post{
		{Title: "Newest post", Date: "2026-10-31", Path: "/newest/", Body: "Hello from **the body**."},
		{Title: "Older post", Date: "2020-01-01", Path: "/older/", Body: "old"},
	}
	sess, in, out := ptySession(t, dial(t, "reader", posts))

	// Answer the background-colour and device-attributes queries like a real terminal.
	waitFor(t, out, "\x1b[c")
	in.Write([]byte("\x1b]11;rgb:0000/0000/0000\x07\x1b[?62c"))
	waitFor(t, out, "Older post")
	in.Write([]byte("\r"))
	waitFor(t, out, "Hello from")
	waitFor(t, out, "blog.tobked.dev/newest/")
	out.Reset()
	in.Write([]byte("q")) // back to the list
	waitFor(t, out, "Older post")
	in.Write([]byte("q")) // quit
	if err := sess.Wait(); err != nil {
		t.Fatalf("session did not exit cleanly: %v", err)
	}
}

func TestSessionLimit(t *testing.T) {
	defer func(n int) { maxSessions = n }(maxSessions)
	maxSessions = 1
	c := dial(t, "reader", nil)
	_, _, first := ptySession(t, c)
	waitFor(t, first, "\x1b[c") // the app is running and holds the only slot
	_, _, second := ptySession(t, c)
	waitFor(t, second, "Too many readers")
}

func TestLogQuotesClientInput(t *testing.T) {
	logs := &syncBuf{}
	log.SetOutput(logs)
	defer log.SetOutput(os.Stderr)
	sess, err := dial(t, "x\nFAKE admin connect \x1b]0;pwned\x07", nil).NewSession()
	if err != nil {
		t.Fatal(err)
	}
	sess.CombinedOutput("")
	waitFor(t, logs, "disconnect")
	if strings.Contains(logs.String(), "\nFAKE") || strings.Contains(logs.String(), "\x1b") {
		t.Fatalf("raw client input in logs: %q", logs.String())
	}
}

func TestRejectsWithoutPty(t *testing.T) {
	sess, err := dial(t, "reader", nil).NewSession()
	if err != nil {
		t.Fatal(err)
	}
	out, _ := sess.CombinedOutput("")
	if !strings.Contains(string(out), "Requires an active PTY") {
		t.Fatalf("got %q", out)
	}
}
