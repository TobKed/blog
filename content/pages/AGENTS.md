---
draft: true
build:
  list: never
  render: never
---

# Topic Pages (`content/pages/`)

This directory contains two kinds of Hugo pages:

1. **Site navigation & hub pages** (do **not** auto-add external links here unless explicitly asked):

   - `about_me.md` (`/pages/about-me/`): Author bio and talks.
   - `links.md` (`/pages/links/`): Central navbar hub page that links to all curated topic sub-pages below. **Whenever a new curated topic page is created in `content/pages/`, add an entry for it in `links.md` (sorted alphabetically by title).**
   - `blogs.md` (`/pages/blogs/`, draft): Personal blogroll of individual engineering blogs.

2. **Curated topic pages** (evergreen reference pages where relevant links from monthly posts or user requests should also be proposed):

   - `ai.md` (`/pages/ai-resources/`)
   - `async.md` (`/pages/async-multithreading-and-multiprocessing-resources/`)
   - `microservices.md` (`/pages/microservices-resources/`)
   - `python.md` (`/pages/python-django-resources/`)
   - `sleep.md` (`/pages/sleep/`)
   - `writing.md` (`/pages/writing/`)

______________________________________________________________________

## Front Matter Convention

Every curated topic page uses YAML front matter with `build.list: never` and `build.render: always` so Hugo renders the page at `/pages/<slug>/` without mixing it into post listings:

```yaml
---
title: Topic Title
slug: topic-slug
date: 'YYYY-MM-DD'
tags:
  - tag1
  - tag2
summary: Short description of the topic page
categories:
  - main
build:
  list: never
  render: always
---
```

______________________________________________________________________

## Entry Formatting Rules

- **Section headings** use level-2 headings (`## Section Name`), with optional `###` sub-headings (e.g., `### PL` for Polish-language links).
- **Every resource entry** (articles, repos, tools, books, videos) uses a bulleted bold link followed by a colon and a concise 1-sentence description:
  ```markdown
  - **[Title](https://example.com/)**: Concise one-sentence summary of what the resource covers or why it is useful.
  ```
  - For GitHub repositories, use `owner/repo` as the link text: `- **[owner/repo](https://github.com/owner/repo)**: Description.`
- **Sorting**: Keep entries sorted **alphabetically by link title** (case-insensitive) within each section.
- **Empty sections**: If a section has no entries yet, keep `_(No resources yet)_` as a placeholder; remove the placeholder when adding the first item to that section.
- **No duplicates**: Never add a URL (or YouTube video ID) that already exists on the same topic page.

______________________________________________________________________

## Topic Page Catalog & Section Map

When evaluating a new URL (e.g., via the `add-link-to-blog` skill), check whether it matches one or more of the curated topic pages below:

### 1. `content/pages/ai.md` (`AI resources`)

- **Matches:** AI coding agents, agent harnesses, Claude Code / Codex / Cursor skills, plugins, spec-driven development (SDD) tools, AI engineering workflows, and LLM tools.
- **Sections:**
  - `## Tools & Setup` — Agent harnesses, CLIs, and workflow setups
  - `## Skills` — Reusable agent skills and skill repositories
  - `## Spec Driven` — Spec-driven development frameworks and toolkits
  - `## Plugins` — Editor/agent plugins for AI coding
  - `## Websites` — Web apps, guides, and articles on AI engineering
  - `## Books` — Books on AI and LLMs
  - `## Videos` — Talks and videos on AI engineering

### 2. `content/pages/async.md` (`Async, multithreading and multiprocessing resources`)

- **Matches:** Python `asyncio`, event loops, coroutines, concurrency, parallelism, `threading`, `multiprocessing`, and async Django/database patterns.
- **Sections:**
  - `## Websites` — Articles, deep dives, and tutorials
  - `## Books` — Books on async and concurrency
  - `## Videos` — Talks, playlists, and video tutorials

### 3. `content/pages/microservices.md` (`Microservices resources`)

- **Matches:** Microservices architecture, distributed systems pitfalls, service boundaries, modular monoliths vs. microservices.
- **Sections:**
  - `## Websites` — Articles and case studies
  - `## Books` — Books on microservices and distributed architecture
  - `## Videos` — Conference talks and videos

### 4. `content/pages/python.md` (`Python & Django resources`)

- **Matches:** Evergreen Python and Django reference tools, books, podcasts, blogs, tutorial channels, and conferences (as opposed to one-off news items).
- **Sections:**
  - `## Books` — Books on Python, Django, Flask, and TDD
  - `## Podcasts` — Python and software engineering podcasts
  - `## Videos` — Video archives and conference talk indexes
  - `## Blogs` — Personal engineering blogs focused on Python and Django
  - `## Tutorials` — Tutorial platforms and YouTube channels
  - `## Django` — Official Django resources, package directories, and class inspectors
  - `## Conferences & Meet-ups` — Python conferences and local community meetups

### 5. `content/pages/sleep.md` (`Sleep`)

- **Matches:** Sleep science, circadian rhythm, recovery, insomnia protocols, and sleep hygiene.
- **Sections:**
  - `## Links` — Articles, books, and written toolkits
  - `## Videos` — English-language talks and podcast episodes
  - `### PL` (under `## Videos`) — Polish-language videos on sleep

### 6. `content/pages/writing.md` (`Writing & Blogging`)

- **Matches:** Blogging craft, why to write, technical/engineering writing, RFCs and design docs, documentation best practices, note-taking systems (Zettelkasten, second brain, NotebookLM), workplace communication, and anti-AI-slop writing.
- **Sections:**
  - `## Blogging & Why Write` — Personal blogging, writing habits, and motivation
  - `## Engineering Writing & Documentation` — Design docs, tutorials, brag docs, and technical documentation
  - `## Note-Taking & Thinking in Text` — Note-taking methods, PKM, and codebase notes
  - `## Communication & Anti-Slop` — Engineering communication frameworks and fighting low-effort AI slop
  - `## Tools & Platforms` — Writing and note-taking apps/tools
  - `## Videos` — Talks and videos on writing, note-taking, and AI slop
