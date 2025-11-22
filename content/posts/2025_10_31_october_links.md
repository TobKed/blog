Title: Month summary - October 2025
Date: 2025-10-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2025
Slug: 2025-october-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2025/2025_10_xx.jpg
Status: draft

# October 2025

Time for another monthly post sharing some of the IT discoveries that crossed my path lately.
Below you'll find a mix of articles, links, and resources, some of which tie into my current activities and areas of interest.

## Some thoughts

### AI House OpenAI meetup

The highlight of the month was the [AI House OpenAI meetup](https://luma.com/wkcnkqw5) in Amsterdam. It was a great event focused on "Vibe Coding" and getting the most out of OpenAI's coding assistant.

[Anouk Muis](https://www.linkedin.com/in/anoukmuis/?originalSubdomain=uk) from OpenAI gave a workshop on ChatGPT's Codex, followed by a panel discussion with [Vladislav Tankov](https://www.linkedin.com/in/vladislav-tankov/) (Director of AI at JetBrains) and [Jelmer Borst](https://www.linkedin.com/in/japborst/) (Head of Analytics & AI at Picnic Technologies). It was great to explore practical strategies for effective AI-assisted coding at the new AI House hub.

<img src="{static}/images/posts/2025/2025_10_ai_house_open_ai.jpg" alt="AI House" style="display: block; margin-left: auto; margin-right: auto;">

<img src="{static}/images/posts/2025/2025_10_ai_house_open_ai_panel.jpg" alt="AI House panel discussion" style="display: block; margin-left: auto; margin-right: auto;">

### Tools updates

I finally switched terminal emulators. I had been struggling with some random key binding issues in [iTerm2](https://www.iterm2.com/), but I managed to recreate my preferred workflow with a hotkey window in [Ghostty](https://ghostty.org/) using its quick terminal feature:

```
keybind = global:cmd+enter=toggle_quick_terminal
```

I also enabled Touch ID for `sudo` commands, so I no longer need to type my password all the time ([link1](https://0xmachos.com/2023-10-01-Touch-ID-sudo/), [link2](https://github.com/0xmachos/macos-scripts/blob/master/enable-touchid-sudo)).

On the window management front, I started using [Alt-Tab](https://github.com/lwouis/alt-tab-macos) for better windows switching and [Rectangle](https://rectangleapp.com/) for snapping windows. Both have significantly improved my workflow.

### Life

I watched a lot of Graham Weaver videos this month. His "Last Lecture" series gave me a lot of inspiration and motivation.

- [Last Lecture Series: How to Design a Winnable Game – Graham Weaver](https://www.youtube.com/watch?v=0SQor2z2QAU)
- [Last Lecture Series: “How to Live an Asymmetric Life” Graham Weaver](https://www.youtube.com/watch?v=dZxbVGhpEkI)
- [Last Lecture Series: “Your Life as the Hero’s Journey” Graham Weaver](https://www.youtube.com/watch?v=WhkTFEzyqlo)
- [Last Lecture Series: "How to Live your Life at Full Power" Graham Weaver](https://www.youtube.com/watch?v=uxoCnxlxpIk)

______________________________________________________________________

## Articles

### [Crafting Software: Writing Maintainable Code](https://wedgworth.dev/crafting-software-writing-maintainable-code/)

> Maintainable code can easily be the difference between long-lived, profitable software, and short-lived money pits.

### [The Software Essays that Shaped Me · Refactoring English](https://refactoringenglish.com/blog/software-essays-that-shaped-me/)

#### AI generated summary

The page explores influential essays that shaped the author's software development philosophy, emphasizing clear test code, the benefits of plain JavaScript, choosing reliable technologies, digital disaster preparedness, and user-friendly input validation.

### [Advice I Wish I Knew as a Junior Developer](https://raheeljunaid.com/blog/advice-for-developers/)

#### AI generated summary

> The blog post provides advice for junior developers based on the author's experiences in software development. Key points include the importance of working with legacy code, managing expectations by underpromising and overdelivering, maintaining professional relationships for career advancement, and understanding that all code is temporary.

### [The Productive Discomfort Zone: Why Real Career Growth Feels Awful](https://alifeengineered.substack.com/p/the-productive-discomfort-zone-why)

#### AI generated summary

The article explores the 'productive discomfort zone,' a phase where career growth feels challenging and uncomfortable, yet is essential for achieving exceptional success. It contrasts this with the 'flow state,' highlighting the importance of persevering through difficult periods.

### [A One-Pager Is All You Need - by Jordan Cutler](https://read.highgrowthengineer.com/p/a-one-pager-is-all-you-need)

> The highly valuable tool for influence and moving solutions forward as an engineer

### [Distributing your own scripts via Homebrew](https://justin.searls.co/posts/how-to-distribute-your-own-scripts-via-homebrew/)

#### AI generated summary

This article by Justin Searls explains how to distribute CLI tools via Homebrew. It covers setting up a GitHub repository, creating a Homebrew tap, and automating updates with GitHub Actions, highlighting the benefits and challenges of using Homebrew.

### [An Engineer's Guide To Cultivating Confidence](https://alifeengineered.substack.com/p/an-engineers-guide-to-cultivating)

> You don't need to "feel" confident to be confident. Here's how.

### [What is "good taste" in software engineering?](https://www.seangoedecke.com/taste/)

#### AI generated summary

The article discusses the concept of 'good taste' in software engineering, emphasizing that it is distinct from technical skill and involves selecting the right engineering values for a project. It highlights the importance of flexibility and understanding trade-offs in design decisions, and how personal values shape an engineer's taste.

### [Firefox is the best mobile browser | Kelvin's personal website](https://kelvinjps.com/blog/firefox-best-mobile-browser/)

#### AI generated summary

Firefox is praised as the best mobile browser due to its open-source nature, privacy features, and support for powerful extensions on Android. The article highlights extensions that block ads and pop-ups, improve user experience on Medium and Twitter/X, and more. It also discusses Firefox's sync feature and customizable homepage.

### [Examples are the best documentation](https://rakhim.exotext.com/examples-are-the-best-documentation)

#### AI generated summary

The article emphasizes the value of examples in technical documentation, arguing that they help developers quickly understand complex concepts without needing to delve into detailed explanations. It highlights the challenges developers face with formal documentation and suggests that examples can make documentation more accessible and practical.

## AI

### [Neural Networks: Simpler Than You Think | Hamza's Blog](https://www.hamza.se/blog/neural-networks)

> A walkthrough of implementing a neural network from scratch in Python, exploring what makes these seemingly complex systems actually quite straightforward.

### [Python MCP Server: Connect LLMs to Your Data – Real Python](https://realpython.com/python-mcp/)

> Learn how to build a Model Context Protocol (MCP) server in Python. Connect tools, prompts, and data to AI agents like Cursor for smarter assistants.

### [Pairing with Claude Code to Rebuild My Startup’s Website](https://blog.nseldeib.com/p/pairing-with-claude-code-to-rebuild)

> Adventures using AI agents, especially Claude Code, and MCP Servers

### [Effective context engineering for AI agents \\ Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

#### AI generated summary

The article explores context engineering as a critical aspect of AI development, focusing on optimizing the information used by AI models to achieve desired behaviors. It emphasizes the need for careful token curation due to the limitations of large language models and provides strategies for effective context management.

### [Vibing a Non-Trivial Ghostty Feature – Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing)

#### AI generated summary

The article explores the creation of a macOS unobtrusive update notification feature using AI and agentic coding tools. It emphasizes the importance of human intervention in refining AI-generated code and overcoming challenges, showcasing AI as an assistant in software development.

### [The rise of "context engineering"](https://blog.langchain.com/the-rise-of-context-engineering/)

#### AI generated summary

Context engineering involves creating dynamic systems to provide the right information and tools for LLMs to perform tasks effectively. It is crucial as LLM applications become more complex, focusing on structured context over clever prompt phrasing. LangGraph and LangSmith are tools that facilitate context engineering.

### [GitHub - alvinunreal/tmuxai: AI-Powered, Non-Intrusive Terminal Assistant](https://github.com/alvinunreal/tmuxai)

> AI-Powered, Non-Intrusive Terminal Assistant.

### [GitHub - PicoTrex/Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images/tree/main)

> A curated collection of fun and creative examples generated with Nano Banana🍌, Gemini-2.5-flash-image based model.

### [Void](https://voideditor.com/)

> Void is an open source Cursor alternative. Full privacy. Fully-featured.

### [v0 by Vercel](https://v0.app/)

> Your collaborative AI assistant to design, iterate, and scale full-stack applications for the web.

## Security

### [How I Almost Got Hacked By A 'Job Interview'](https://blog.daviddodda.com/how-i-almost-got-hacked-by-a-job-interview)

> I was 30 seconds away from running malware, Here's how a sophisticated scam operation almost got me, and why every developer needs to read this.

### [Weak password allowed hackers to sink a 158-year-old company](https://www.bbc.com/news/articles/cx2gx28815wo)

> Transport company KNP forced to shut down after international hacker gangs target thousands of UK businesses.

## Python

### [Python lazy imports you can use today | PythonTest](https://pythontest.com/python-lazy-imports-now/)

> There's a proposal for Python to natively support lazy importing starting in Python 3.15. However, there are techniques covered in this post that allow you to use lazy importing now with 3.13, 3.12, ... really every version of Python.

### [Beyond the AI Hype: Guido van Rossum on Python’s Philosophy, Simplicity, and the Future of Programming. | ODBMS Industry Watch](https://www.odbms.org/blog/2025/10/beyond-the-ai-hype-guido-van-rossum-on-pythons-philosophy-simplicity-and-the-future-of-programming/)

#### AI generated summary

Guido van Rossum discusses Python's philosophy of simplicity and its role in AI, the importance of type hints, and the challenges of transitioning from Python 2 to 3. He expresses concerns about the ethical implications of AI and hopes for Python's legacy to empower individual developers.

### [Python 3.14: Cool New Features for You to Try – Real Python](https://realpython.com/python314-new-features/)

> Learn what's new in Python 3.14, including an upgraded REPL, template strings, lazy annotations, and subinterpreters, with examples to try in your code.

## Django

### [Python and then some: Using Async Functions in Celery with Django Connection Pooling](https://mrdonbrown.blogspot.com/2025/10/using-async-functions-in-celery-with.html?m=1)

> The blog post discusses the challenges and solutions for using asynchronous functions in Celery tasks within a Django application, particularly when using Django's connection pooling feature introduced in version 5.1. It explains that Celery does not natively support async functions, which can lead to issues with database connection pooling. The post details how Django's async ORM works, highlighting the use of `ThreadSensitiveContext` to manage database connections in async contexts. It provides a solution for wrapping async functions in Celery tasks using a custom decorator and handling connection cleanup. Additionally, it addresses issues related to Celery's prefork mode and provides code snippets for implementing the solutions.

### [DjangoCon US 2025 Recap — Portfolio documentation](https://katherinemichel.github.io/blog/conferences/djangocon-us-2025-recap.html)

#### AI generated summary

The DjangoCon US 2025 recap covers key presentations, including Will Vincent's insights on Django's limitations for LLMs, Paolo Melchiorre's GeneratedField feature, and Dwayne McDaniel's talk on AI security risks. The event celebrated Django's 20th anniversary with social gatherings and highlighted the importance of community and innovation in the Django ecosystem.

### [Django bulk_update memory issue | Anže’s Blog](https://blog.pecar.me/django-bulk-update-memory-issue)

#### AI generated summary

The blog post addresses a memory issue with Django's `bulk_update` method during a migration involving a large number of database objects. The author experienced a memory spike that led to a `SIGTERM` and resolved it by implementing custom batching. The issue was reported, but the proposed fix was rejected, leading to a documentation update warning about potential memory usage.

### [Adding imports to the Django shell · Applied Cartography](https://jmduke.com/posts/post/django-shell/)

#### AI generated summary

The author explains how to customize the Django shell to automatically import specific modules, a feature they missed after removing django-extensions due to Django 5.2's new capabilities.

## Python libraries

### [GitHub - feldroy/air: The new Python web framework by the authors of Two Scoops of Django](https://github.com/feldroy/air)

> Air 💨: The new web framework that breathes fresh air into Python web development. Built with FastAPI, Starlette, and Pydantic.

## Tools

### [Tilt | Kubernetes for Prod, Tilt for Dev](https://tilt.dev/)

#### AI generated summary

Tilt is an open-source toolkit that simplifies microservice development by providing smart rebuilds, live updates, and a user-friendly interface for Kubernetes. It enhances productivity through features like holistic app visibility, fast live updates, and built-in best practices.

### [GitHub - tw93/Mole: 🐹 Dig deep like a mole to clean you Mac.](https://github.com/tw93/Mole)

#### AI generated summary

Mole is a terminal-based tool for cleaning and optimizing Mac systems, offering deep cleanup, app uninstallation, and system optimization features.

### [GitHub - lwouis/alt-tab-macos](https://github.com/lwouis/alt-tab-macos?tab=readme-ov-file)

> Windows alt-tab on macOS

### [GitHub - slackhq/nebula](https://github.com/slackhq/nebula)

> A scalable overlay networking tool with a focus on performance, simplicity and security

### [ZeroTier | Next-Generation Connectivity and Cybersecurity](https://www.zerotier.com/)

> Connect everything, from cloud to IoT, with the next-generation global network solution. Simple, resilient, and secure networking in minutes.

## Cloud

### [Every Developer Needs to Self-Host](https://dev.to/code42cate/every-developer-needs-to-self-host-43mm)

#### AI generated summary

This article argues that self-hosting is a valuable practice for developers, offering insights into hardware and network management while potentially saving costs compared to cloud services.

## Other stuff

### [Indefinite Backpack Travel – Jeremy Maluf](https://jeremymaluf.com/onebag/)

#### AI generated summary

This page explores the author's minimalist lifestyle of indefinite travel with only a laptop backpack. It highlights the benefits of onebag travel, such as reduced travel hassles and a focus on essentials. The author provides a detailed list of possessions and emphasizes practicality over consumerism, allowing for spontaneous travel and maintaining social connections.

### [grug.design](https://www.grug.design/know)

> The Grug Brained Designer

## Videos

### [Last Lecture Series: How to Design a Winnable Game – Graham Weaver](https://www.youtube.com/watch?v=0SQor2z2QAU)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/0SQor2z2QAU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Last Lecture Series: “How to Live an Asymmetric Life,” Graham Weaver](https://www.youtube.com/watch?v=dZxbVGhpEkI)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/dZxbVGhpEkI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Last Lecture Series: “Your Life as the Hero’s Journey,” Graham Weaver](https://www.youtube.com/watch?v=WhkTFEzyqlo)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/WhkTFEzyqlo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Last Lecture Series: How to Live your Life at Full Power — Graham Weaver](https://www.youtube.com/watch?v=uxoCnxlxpIk)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/uxoCnxlxpIk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [The Holy Grail of Neovim Note Taking](https://www.youtube.com/watch?v=5ht8NYkU9wQ)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/5ht8NYkU9wQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Lecture #9: How to Read so that you _Retain_ Information](https://www.youtube.com/watch?v=uiNB-6SuqVA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/uiNB-6SuqVA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [n8n Now Runs My ENTIRE Homelab](https://www.youtube.com/watch?v=budTmdQfXYU)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/budTmdQfXYU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [DEF CON 33 - Kill List: Hacking an Assassination Site on the Dark Web - Carl Miller, Chris Monteiro](https://www.youtube.com/watch?v=cYZmRp90hss)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/cYZmRp90hss" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [What Big Tech Still Gets WRONG about Great Programmers | Casey Muratori](https://www.youtube.com/watch?v=gZ2V5VtwrCw)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/gZ2V5VtwrCw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### AI generated summary

Casey Muratori addresses the common misconceptions held by big tech companies regarding the qualities of great programmers, highlighting the disconnect between industry hiring practices and the true skills that define exceptional programming talent.

### [AI Slop Is Destroying The Internet](https://www.youtube.com/watch?v=_zfN9wnPvU0)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/_zfN9wnPvU0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Visualizing transformers and attention | Talk for TNG Big Tech Day '24](https://www.youtube.com/watch?v=KJtZARuO3JY)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/KJtZARuO3JY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Vibes won't cut it — Chris Kelly, Augment Code](https://www.youtube.com/watch?v=Dc3qOA9WOnE)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/Dc3qOA9WOnE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Google’s NotebookLM is Getting Even More Powerful](https://www.youtube.com/watch?v=i9kiuGIHlMY)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/i9kiuGIHlMY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [13 Years in QA: Why Traditional QA is Disappearing (And What to Do)](https://www.youtube.com/watch?v=4J53WvB1-4E)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/4J53WvB1-4E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [The AWS Outage Uncovered Something EVERY Developer Should Know](https://www.youtube.com/watch?v=X2wmzn-tfiQ)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/X2wmzn-tfiQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
