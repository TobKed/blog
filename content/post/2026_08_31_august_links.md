---
draft: true
title: Month summary - August 2026
date: "2026-08-31"
tags:
  - python
  - blog
  - podcast
  - series
  - aggregate
  - summary
  - month
  - "2026"
slug: 2026-august-links
summary: Interesting stuff from the month
image: /images/posts/2026/2026_08_xx.jpg
categories:
  - summary
---

# August 2026

Time for another monthly post sharing some of the IT discoveries that crossed my path lately.
Below you'll find a mix of articles, links, and resources, some of which tie into my current activities and areas of interest.

## Some thoughts

### Communication

Working on my communication skills: since everyone is already overloaded with the amount of text to process, I am trying to keep messages short and straight to the point.
Not necessarily grammatically correct, but I'd rather leave a few mistakes here and there than give the impression I copy-pasted some LLM output.
Some relevant links:

- [nohello.net](https://nohello.net/)
- [noslopgrenade.com](https://noslopgrenade.com/)

### Tooling

Having fun with tooling: testing [mise](https://mise.jdx.dev/), which should solve the never-ending struggle with local environments.

For example, I had an alias to create Python virtual environments with `v-env <python-version>` (which creates the virtual env in a `venv` folder in the current directory), and I overrode `cd` to activate it automatically whenever it spotted one.
Nothing complicated, and it works well enough, but it looks like `mise` can take that off my hands.

What `mise` can do for you:

1. Version manager - one config file per project:

```toml
# mise.toml
[tools]
python = "3.12"
node = "22"
terraform = "latest"
```

2. Env manager — replaces direnv:

```toml
[env]
DATABASE_URL = "postgres://localhost/dev"
_.file = ".env"
_.path = ["./node_modules/.bin"]
```

3. Task runner — replaces a Makefile-for-scripts:

```toml
[tasks.test]
run = "pytest"
depends = ["lint"]
```

Then just `mise run test`.

I'll play with it more to see how it behaves, but it looks promising.

#### Better window switcher

I have just switched from [alt-tab](https://alt-tab.app/) (which started limiting functionality for non-paying users) to the fully free and open-source [BetterCmdTab](https://github.com/rokartur/BetterCmdTab), and it seems to work pretty well.
The only issue I hit was with four Chrome windows open—it couldn't see one of them for some reason, but otherwise it works like a charm.
I especially like that you can select apps with `j/k` (viva la vim keybindings).
Small improvements, but since I spend so much time at the computer, I feel they compound.
And tinkering with my setup gives me a lot of joy too.

______________________________________________________________________

## Articles

### [A Life Engineered: Addition by Subtraction](https://alifeengineered.substack.com/p/addition-by-subtraction)

> This week I'm getting better by doing less.

### [Tom Moertel’s Blog: Beyond “Clean Code”: Why Your Comments Matter](https://blog.moertel.com/posts/2026-07-27-beyond-clean-code-why-your-comments-matter.html)

> To the extent that your programming language lets you express these things naturally in your logic, you should do so.
> But don’t contort your logic to accommodate intent and “why” information that would be easier for your audience to understand in natural language.

### [DHH: Endless execution](https://world.hey.com/dhh/endless-execution-4157e065)

> What a time to be alive. Nay, what a blessing.

### [Shane AAnderson - How to create snippets in LazyVim](https://shaneanderson.id.au/how-to-create-snippets-in-lazyvim.html)

> Took me way too much effort to figure this out and searching for info resulted in a lot of posts with other people asking the same question or outdated information as LazyVim has changed its plugins a bunch of times, hopefully this helps someone else out there.

### [Building an Omarchy-Inspired Setup on macOS | Christopher Penkin](https://www.penkin.me/development/tools/productivity/configuration/2025/11/28/building-omarchy-inspired-setup-macos.html)

> Learn how to build a keyboard-driven tiling window manager setup on macOS using yabai, sketchybar, and skhd. Inspired by Omarchy's philosophy of minimal aesthetics and instant workspace switching, this guide covers configuration, multi-monitor support, and creating a distraction-free development environment on a MacBook Pro M1.

## AI

### [Five studies changing how I think about AI in software engineering](https://newsletter.getdx.com/p/five-studies-that-are-changing-how)

> AI compressed the upstream work. What does that mean for everything downstream?

### [Pydantic AI - The Human-in-the-Loop is Tired](https://pydantic.dev/articles/the-human-in-the-loop-is-tired)

> So if you're feeling overwhelmed, destabilized, simultaneously more productive and less happy, know that you're not alone.

### [/hallmak](https://www.usehallmark.com/)

> The anti-slop design skill for Claude Code, Cursor, and Codex. Twenty themes with real structural variety, and a 57-gate check before anything ships.

### [Real Python: CrewAI in Python: Coordinating Teams of AI Agents](https://realpython.com/crewai-python/)

> CrewAI excels at structured, role-based workflows where each agent has clear responsibilities.
> It saves you from complex orchestration code by handling task coordination and data flow automatically.

### [We Gave GPT 5.6 Sol a Real Business. It Lied, Spammed, and Lost $447](https://www.bottlenecklabs.com/blog/autonomously-run-businesses)

> If an agent had a wallet, a computer, and 24 hours, could it run a profitable startup?

### [aftermath - Welcome To The Resistance: Meet The Workers Dodging (And Sabotaging) Their Employer's AI Mandat](https://aftermath.site/ai-resistance-tips-workforce-llm-workers/)

> 'When I copy-edit writing I take an extra twenty minutes to double check, then say I had Claude copy edit it as well. Everyone’s really happy with my performance'

### [AI is removing the middle class of software engineering](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

> The people who don't will become much cheaper to hire or get replaced entirely while the money gets funnelled towards an increasingly smaller number of people who can actually be trusted.

### [Claude Blog - Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions)

> How to run efficient sessions that get the most value from every token.

### [GitHub - ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

> A skill to stop your coding agent from burying the answer. ADHD-friendly output.

### [GitHub - mattpocock/skills](https://github.com/mattpocock/skills)

> Skills for Real Engineers. Straight from my .agents directory.

### [GitHub - cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack/skills/)

#### AI generated summary

A collection of reusable Cursor agent skills and prompt patterns (architect, TDD, root-cause-fixing, type-system discipline, blast-radius, etc.) that codify practical engineering principles as invokable skills for AI coding agents.

## Tools

### [GitHub - AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)

> A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID++. No account, no telemetry.

### [GitHub - rokartur/BetterCmdTab](https://github.com/rokartur/BetterCmdTab)

> The Cmd+Tab macOS deserves.

## Cloud

### [GitHub - floci-io/floci](https://github.com/floci-io/floci)

> Floci is a free, open-source local AWS emulator for development, testing, and CI. It gives you AWS-shaped services on your machine without requiring a cloud account, an auth token, or paid feature gates.

## Videos

### [A Life Engineered: Ex-Amazon VP on What Actually Gets You Promoted | Ethan Evans](https://www.youtube.com/watch?v=Gf0pR4_bv-o)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/Gf0pR4_bv-o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [OMH 2025: Grzegorz Wróbel - Homelab dla bezpiecznika - domowy poligon dla pasji, nauki i pracy](https://www.youtube.com/watch?v=YSon1JW5qXM)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/YSon1JW5qXM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [A Life Engineered - Ex-Amazon VP on What Actually Gets You Promoted | Ethan Evans](https://www.youtube.com/watch?v=Gf0pR4_bv-o)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/Gf0pR4_bv-o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [A Life Engineered - How to Learn And Grow Unbelievably Fast](https://www.youtube.com/watch?v=mV-JSdeMSn0)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/mV-JSdeMSn0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [The future of creativity on the internet in a world with AI](https://www.youtube.com/watch?v=17_HcR95YBc)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/17_HcR95YBc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Matt Pocok - LIVE: Uncle Bob on Software Fundamentals in the Age of AI](https://www.youtube.com/watch?v=zcLPGC-tvgk)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/zcLPGC-tvgk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Matt Pocok - /wayfinder: Nothing is too big to plan anymore](https://www.youtube.com/watch?v=F3lL98Pj90o)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/F3lL98Pj90o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [A Life Engineered - Negotiation Expert: How To 3X Your Tech Salary](https://www.youtube.com/watch?v=v87stFQMFNY)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/v87stFQMFNY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [NetworkChuck - I think I might finally switch to Linux](https://www.youtube.com/watch?v=9SDkU5VDQEQ)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/9SDkU5VDQEQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [David Senra - Tobi Lütke: 21 Years of Building Shopify](https://www.youtube.com/watch?v=ZSM2uFnJ5bs)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/ZSM2uFnJ5bs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Mischa van den Burg - Why Is Everyone Buying This $150 Linux Laptop?](https://www.youtube.com/watch?v=Eor_qf5KCHI)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/Eor_qf5KCHI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Claude just killed the note-taking app. Here is proof.](https://youtu.be/geIKyDaXwGg)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/geIKyDaXwGg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [The First CLI Tool You'll Use It Every Day](https://youtu.be/JhMkEZenxlU)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/JhMkEZenxlU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Build A Claude Knowledge Base That Self-Improves!](https://youtu.be/ib74sLgjIBM)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/ib74sLgjIBM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Nick Milo Reads My Obsidian Vault Like a Doctor](https://youtu.be/PwUGO74DYJQ)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/PwUGO74DYJQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Stop writing software like it's 1999! - Hannes Lowette - NDC Copenhagen 2026](https://www.youtube.com/watch?v=_1LEFUgHFJI)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/_1LEFUgHFJI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [So I tried Matt's skills...](https://youtu.be/0oXOOlqVu5M)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/0oXOOlqVu5M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
