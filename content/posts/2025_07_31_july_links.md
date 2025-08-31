Title: Month summary - July 2025
Date: 2025-07-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2025
Slug: 2025-july-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2025/2025_07_xx.jpg
Status: draft

# July 2025

Time for another monthly post sharing some of the IT discoveries that crossed my path lately.
Below you'll find a mix of articles, links, and resources, some of which tie into my current activities and areas of interest.

## Some thoughts

This month I stumbled upon something that completely blew my mind: copyparty. It's an incredibly versatile and portable file server packed into a single file with zero dependencies.

As the project on GitHub says:

#### [GitHub - 9001/copyparty](https://github.com/9001/copyparty/)

> Portable file server with accelerated resumable uploads, dedup, WebDAV, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps - 9001/copyparty

It's one of those tools that just does everything you need without any fuss. For a great introduction and to see it in action, check out this video:

#### [introducing copyparty, the FOSS file server - YouTube](https://www.youtube.com/watch?v=15_-hgsX2V0)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/15_-hgsX2V0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Definitely worth a look if you ever need to share files quickly and efficiently.

______________________________________________________________________

## Articles

### [How to Think About Time in Programming - Shan Rauf](https://shanrauf.com/archive/how-to-think-about-time-in-programming)

> A conceptual model for thinking about time in programming that encapsulates the complexity that many programmers cite online

### [Stop Coding Like You Work at Google | by Aeon Flex](https://medium.com/@neonmaxima/stop-coding-like-you-work-at-google-ce9fca31c711)

> Let’s get one thing straight right now. You don’t work at Google. I don’t either. Most of us don’t. And yet, for some reason, there’s this widespread epidemic of developers out here coding like…

### [Scott Spence - Speeding Up My ZSH Shell](https://scottspence.com/posts/speeding-up-my-zsh-shell)

> Super quick one I want to document here! I got myself on a side quest, again! No biggie, my ZSH shell was taking ages to load. When I say ages, more like 5+ seconds every time I opened a new terminal, that sort of thing can add up. This is just something I’ve lived with over the years, nothing has prompted this other than me wondering why it’s slow, then searching for how to profile it.

### [Your Career Needs a Vision, Not More Goals - by Steve Huynh](https://alifeengineered.substack.com/p/your-career-needs-a-vision-not-more)

> Why you can hit every target and still feel lost. A simple 3-part framework for an intentional life.

### [Why I'm Not Proud of My 170,000 YouTube Subscribers](https://alifeengineered.substack.com/p/why-im-not-proud-of-my-170000-youtube)

> Success is an output you can't control. Here's what to focus on instead.

### [How to Deal With a Toxic Top-Performer | by Dave Bailey](https://foundercoach.medium.com/how-to-deal-with-a-toxic-top-performer-b535f3268fc1)

> Every founder hires a brilliant jerk. They start as a dream hire, then turn into a cultural liability. Here’s how to fix it by shifting from personality to structure. They know the domain inside out…

### [Mniej znane opcje konfiguracyjne Gita - devszczepaniak.pl](https://devszczepaniak.pl/mniej-znane-opcje-konfiguracyjne-gita/)

> Podnieś swój komfort pracy z Gitem na wyższy poziom. Poznaj nieco mniej znane, lecz bardzo użyteczne opcje konfiguracyjne Gita.

### [How I do it | daniel.haxx.se](https://daniel.haxx.se/blog/2025/07/13/how-i-do-it/)

> The blog post by Daniel Stenberg discusses his dedication and approach to managing the curl project, an open-source tool he has been leading for decades. He describes his work routine, motivation, and the independence of the curl project. Daniel emphasizes the importance of maintaining high standards, continuous improvement, and the sense of responsibility he feels towards the users of curl. He also touches on his leadership style, which focuses on reducing bureaucracy and encouraging community participation. The post highlights his passion for programming and the balance he maintains between work and personal life.

## Productivity

### [How I've run major projects](https://www.benkuhn.net/pjm/)

> The page discusses the importance of delegating project management tasks effectively, emphasizing the need for clear, high-level goals with minimal overlap between workstreams.
> It highlights that the best project managers are not necessarily the strongest technical individual contributors but are highly organized and focused on end goals.

### [The Silent Killer Of Motivation And What To Do About It](https://alifeengineered.substack.com/p/the-silent-killer-of-motivation-and)

> 3 "Good" Habits That Secretly Lead to Burnout, Fatigue, and Exhaustion

### [The Art Of Showing Up - by Steve Huynh - A Life Engineered](https://alifeengineered.substack.com/p/the-art-of-showing-up)

> The fastest way to get things done is to forget the finish line.

## AI

### [GitHub - Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

> Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

### [The rise of "context engineering"](https://blog.langchain.com/the-rise-of-context-engineering/)

> The article discusses the concept of context engineering, which involves building dynamic systems to provide the right information and tools in the right format for large language models (LLMs) to accomplish tasks effectively.

### [Our top guides to building, evaluating, and deploying generative AI](https://www.linkedin.com/pulse/our-top-guides-building-evaluating-deploying-generative-ai-fjkte/)

> The best way to learn AI is by building. From finding quick ways to deploy open models to building complex, multi-agentic systems, it’s easy to feel overwhelmed by the sheer volume of resources out there.

### [I Built a Claude Code Context Modal Inside of Neovim | Daniel Miessler](https://danielmiessler.com/blog/neovim-claude-ai-plugin)

> Sometimes I just wish I had AI right at this moment, right with this text. So I built Kai, an AI popup menu for Neovim that brings Claude directly to your editor.

## Python

### [Design Patterns You Should Unlearn in Python-Part1 | Lihil](https://www.lihil.cc/blog/design-patterns-you-should-unlearn-in-python-part1/)

<span class="ai-summary"> AI generated summary </span>

This article explains why some classic design patterns, like Singleton and Builder, are unnecessary in Python due to its dynamic features. It offers simpler, more Pythonic alternatives to these patterns.

### [Inheritance over composition, sometimes - death and gravity](https://death.andgravity.com/over-composition)

> Last time, we built a hybrid concurrent.futures executor using inheritance. Today, we're building it again (twice!) using composition and functions only, to figure out which way is better and why. Consider this a worked example.

### [Python Gotcha: Logging an uncaught exception  · Ponderings of an Andy](https://andrewwegner.com/python-gotcha-logging-uncaught-exception.html)

> Uncaught exceptions will crash an application. If you don't know how to log these, it can be difficult to troubleshoot such a crash. Let's walk through this gotcha and see how to fix it.

### [Making a Simple HTTP Server with Asyncio Protocols](https://jacobpadilla.com/articles/asyncio-protocols)

> Learn how to build a fast, minimal HTTP server using asyncio.Protocol, complete with routing, parsing, and response handling from scratch!

### [Code reading: The python std lib module - shelve.py](https://www.beyonddream.me/post-5/)

> The article provides an in-depth exploration of the Python standard library module 'shelve.py'.urce code. It explains how 'shelve' allows for persistent, dictionary-like objects and highlights key components and methods within the module. The article serves as a guide for understanding and utilizing 'shelve' effectively.

## Django

### [From Rock Bottom to Production Code – Blog](https://www.matthewraynor.com/blog/from-rock-bottom-to-production-code)

> Matthew Raynor shares his inspiring journey from a life-altering accident to becoming a self-taught Python/Django developer. After a diving accident left him quadriplegic, Matthew faced numerous challenges, including living in a nursing home. Determined to change his life, he taught himself programming using a stylus strapped to his hands. He started with Python and Django, building multiple full-stack applications, including a business dashboard for an art moving company and his personal website, MatthewRaynor.com. His website serves as a portfolio, blog, e-commerce store, and includes an AI chatbot. Matthew's story is one of resilience, learning, and transformation, showcasing his skills and determination to succeed as a developer.

### [Loopwerk: Hosting your Django sites with Coolify](https://www.loopwerk.io/articles/2025/coolify-django/)

> How I moved my Django projects from a manual server setup to Coolify for easier, zero-downtime deployments.

### [Django: iterate through all registered URL patterns - Adam Johnson](https://adamj.eu/tech/2025/07/22/django-iterate-url-patterns/)

> I’ve found it useful, on occasion, to iterate through all registered URL patterns in a Django project. Sometimes this has been for checking URL layouts or auditing which views are registered.

## Python libraries

### [Unlock deeper insights with the new Python client library for Data Commons - Google Developers Blog](https://developers.googleblog.com/en/pythondatacommons/)

> Explore the new Python client library for Data Commons, offering enhanced features and support for custom instances to unlock deeper insights from public statistical data.

### [From SQL To SQLModel: A Cleaner Way To Work With Databases In Python - Pybites](https://pybit.es/articles/from-sql-to-sqlmodel-a-cleaner-way-to-work-with-databases-in-python/)

> SQLModel is a library that lets you interact with databases through Python code with Python objects and type annotations instead of writing direct SQL queries.

## Go

### [Running a million-board chess MMO in a single process · eieio.games](https://eieio.games/blog/a-million-realtime-chess-boards-in-a-single-process/)

<span class="ai-summary"> AI generated summary </span>

This article explores the development of a system that manages a million real-time chess boards in a single process. It highlights the use of a dense array, a single mutex for simplicity, and Cloudflare for caching to optimize performance and reduce server load. The article also discusses snapshot taking, serialization, and rollback mechanisms.

## Tools

### [GitHub - steipete/agent-rules](https://github.com/steipete/agent-rules)

> A collection of reusable rules and knowledge documents for AI coding assistants like Claude Code and Cursor.

### [GitHub - google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

> An open-source AI agent that brings the power of Gemini directly into your terminal.

### [GitHub - 9001/copyparty](https://github.com/9001/copyparty/)

> Portable file server with accelerated resumable uploads, dedup, WebDAV, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps - 9001/copyparty

## Cloud

### [Build and Deploy a Remote MCP Server to Google Cloud Run in Under 10 Minutes | Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-google-cloud-run-in-under-10-minutes)

> Learn how to quickly build and deploy a remote Model Context Protocol (MCP) server to Google Cloud Run, enabling secure and scalable integration of external context with Large Language Models (LLMs).

## Other stuff

### [Jukebox](https://www.jukeboxhq.com)

> Turn your phone or any device into a jukebox! Share a link with friends so they can add songs to your shared music queue.

## Videos

### [Simon Brown - Software architecture as a contributor to high performing teams - YouTube](https://www.youtube.com/watch?v=-nWY8Jq5mlA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/-nWY8Jq5mlA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Nie buduj marki osobistej. Ciemne strony działania w społeczności - YouTube](https://www.youtube.com/watch?v=URNzJb4rG0k)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/URNzJb4rG0k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<span class="ai-summary"> AI generated summary </span>

This video explores the dark sides of building a personal brand within the search community, highlighting challenges like maintaining authenticity and avoiding burnout.

### [I make easier and better decisions each day, because of THIS (so I'm open sourcing it) - YouTube](https://www.youtube.com/watch?v=JOlX4iSBhp8)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/JOlX4iSBhp8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [introducing copyparty, the FOSS file server - YouTube](https://www.youtube.com/watch?v=15_-hgsX2V0)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/15_-hgsX2V0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
