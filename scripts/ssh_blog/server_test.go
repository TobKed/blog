package main

import (
	"bytes"
	"net"
	"path/filepath"
	"strings"
	"sync"
	"testing"
	"time"

	gossh "golang.org/x/crypto/ssh"
)

type syncBuf struct {
	mu sync.Mutex
	b  bytes.Buffer
}

func (s *syncBuf) Write(p []byte) (int, error) { s.mu.Lock(); defer s.mu.Unlock(); return s.b.Write(p) }
func (s *syncBuf) String() string              { s.mu.Lock(); defer s.mu.Unlock(); return s.b.String() }

func dial(t *testing.T, posts []post) *gossh.Client {
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
		User: "reader", HostKeyCallback: gossh.InsecureIgnoreHostKey(),
	})
	if err != nil {
		t.Fatal(err)
	}
	return c
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
		{Title: "Newest post", Date: "2026-10-31", Slug: "newest", Body: "Hello from **the body**."},
		{Title: "Older post", Date: "2020-01-01", Slug: "older", Body: "old"},
	}
	sess, err := dial(t, posts).NewSession()
	if err != nil {
		t.Fatal(err)
	}
	if err := sess.RequestPty("xterm-256color", 40, 100, gossh.TerminalModes{}); err != nil {
		t.Fatal(err)
	}
	out := &syncBuf{}
	sess.Stdout = out
	in, _ := sess.StdinPipe()
	if err := sess.Shell(); err != nil {
		t.Fatal(err)
	}

	// Answer the background-colour and device-attributes queries like a real terminal.
	waitFor(t, out, "\x1b[c")
	in.Write([]byte("\x1b]11;rgb:0000/0000/0000\x07\x1b[?62c"))
	waitFor(t, out, "Older post")
	in.Write([]byte("\r"))
	waitFor(t, out, "Hello from")
	waitFor(t, out, "blog.tobked.dev/newest/")
	in.Write([]byte("q"))              // back to the list
	time.Sleep(200 * time.Millisecond) // sent together, bubbletea reads "qq" as one key
	in.Write([]byte("q"))              // quit
	if err := sess.Wait(); err != nil {
		t.Fatalf("session did not exit cleanly: %v", err)
	}
}

func TestRejectsWithoutPty(t *testing.T) {
	sess, err := dial(t, nil).NewSession()
	if err != nil {
		t.Fatal(err)
	}
	out, _ := sess.CombinedOutput("")
	if !strings.Contains(string(out), "Requires an active PTY") {
		t.Fatalf("got %q", out)
	}
}
