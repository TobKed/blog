Title: Month summary - January 2022
Date: 2022-01-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2022
Slug: 2022-january-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2022/2022_01_xx.jpg
Status: published

# January 2022

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

I heavily use my beloved Kindle and always highlight interesting fragments or sometimes event words.
However, I did not review these notes for a veeery long time.
They are stored in a simple text file, therefore reading raw content is not the most convenient way of consuming it.
To say the least.
I recalled that some time ago my friend [Tomasz Urbaszek](<>) created a simple tool written in Go to parse and browse Kindle clippings.
It is called [gonotes](https://github.com/turbaszek/gonotes) and since I learned a little bit of Go, it was the perfect way to test my fresh skill on it, so I contributed a few fixes.

## Articles

### [From 0 to $50B: the Coinbase Profile](https://www.aakashg.com/2022/01/12/coinbase/)

> Brian Armstrong just bought one of the most expensive homes in the state of California. For $133M, his modern Bel Air mansion is now one of the priciest single-family home transactions ever.
>
> The self-confessed “on the spectrum” (of Autism) CEO has managed to become one of the world’s richest entrepreneurs, as well as one of the most powerful men in web3. With the purchase of his Bel Air mansion, Brian has coronated his position as one of the richest and powerful men in the world, period.

### [Five Tips For a Healthier Postgres Database in the New Year](https://blog.crunchydata.com/blog/five-tips-for-a-healthier-postgres-database-in-the-new-year)

> In this coming year we look forward to making the developer experience of Postgres better than it's ever been.

### [How I build a feature - Simon Willison](https://simonwillison.net/2022/Jan/12/how-i-build-a-feature/)

> I’m maintaining a lot of different projects at the moment. I thought it would be useful to describe the process I use for adding a new feature to one of them, using the new sqlite-utils create-database command as an example.

### [Abstract your code](https://guicommits.com/abstract-your-code/)

> Implementation abstraction makes your code flexible and decoupled from vendors or hard implementations, and finally, it's quite easy to follow, yet is constantly ignored.
>
> This post would fit perfectly in a series named “Coding Practices that should be obvious, but for some unknown reason aren't”.

### [Why is Exposing the Docker Socket a Really Bad Idea? ](https://blog.quarkslab.com/why-is-exposing-the-docker-socket-a-really-bad-idea.html)

> It is written almost everywhere: do not expose the Docker socket on Linux! This is followed by the statement that doing so grants root access to the host. But why? What can be done and how? This is what we are about to explore in this article.

## Python

### [Is your Python code vulnerable to log injection?](https://dev.arie.bovenberg.net/blog/is-your-python-code-vulnerable-to-log-injection/)

> Following the news on log4j lately, you may wonder if Python’s logging library is safe. After all, there is a potential for injection attacks where string formatting meets user input.

### [Python Type Hints - How to Handle Optional Imports](https://adamj.eu/tech/2021/12/29/python-type-hints-optional-imports/)

> This post is not about importing typing.Optional, but instead imports that are themselves optional. Libraries often have optional dependencies, and the code should work whether or not the import is there.

### [Set up a Gunicorn Configuration File, and Test It](https://adamj.eu/tech/2021/12/29/set-up-a-gunicorn-configuration-file-and-test-it)

> If you use Gunicorn, it’s likely you have a configuration file. This is a Python module that contains settings as module-level variables.

### [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)

> In this document, we’ll take a tour of Python’s features suitable for implementing programs in a functional style. After an introduction to the concepts of functional programming, we’ll look at language features such as iterators and generators and relevant library modules such as itertools and functools.

### [An introduction to Pydbantic — a single model solution to Data Verification & Storage](https://itnext.io/an-introduction-to-pydbantic-a-single-model-solution-to-data-verification-storage-254cfe9e757f)

> In a nutshell, pydantic provides a framework for validating input between interfaces to ensure the correct input data( type, structure, required, optional) are met, eliminating the need to add logic to catch & verify bad input.

### [To Virtualenv or not to Virtualenv for Docker? This is the question.](https://potiuk.com/to-virtualenv-or-not-to-virtualenv-for-docker-this-is-the-question-6f980d753b46)

> In this post, I want to disect why the approach is — in my opinion — rather bad for important set of use cases (related to building containers containing Python) and what should be done to fix it. I believe recommending virtualenv as “recommended solution” in all cases — including container building — is the decision that pip maintainers should rethink.

### [Awesome Python Typing](https://github.com/typeddjango/awesome-python-typing)

> Collection of awesome Python types, stubs, plugins, and tools to work with them.

### [Mypy - Type hints cheat sheet (Python 3)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

> This document is a quick cheat sheet showing how the [PEP 484](https://www.python.org/dev/peps/pep-0484) type annotation notation represents various common types in Python 3.

### [10 Unknown Security Pitfalls for Python](https://blog.sonarsource.com/10-unknown-security-pitfalls-for-python)

> In this blog post, we share 10 security pitfalls we encountered in real-world Python projects. We chose pitfalls that we believe are less known in the developer community. By explaining each issue and its impact we hope to raise awareness and sharpen your security mindset. If you are using any of these features, make sure to check your Python code!

## Django

### [My (free) Django monitoring stack for 2022](https://mattsegal.dev/django-monitoring-stack.html)

> You've built and deployed a website using Django. Congrats! After that initial high of successfully launching your site comes the grubby work of fixing bugs. There are so many things that can will go wrong.

### [Feature flags and waffles](https://www.mattlayman.com/blog/2017/feature-flags-and-waffles/)

> Feature flags are a tool that give development teams the ability to expose a feature in a controlled manner.

## Python libraries

### [Samila](https://github.com/sepandhaghighi/samila)

> Samila is a generative art generator written in Python, Samila let's you create arts based on many thousand points. The position of every single point is calculated by a formula, which has random parameters. Because of the random numbers, every image looks different.

## Go

### [Go by Example](https://gobyexample.com/)

> Go is an open source programming language designed for building simple, fast, and reliable software. Please read the official documentation to learn a bit about Go code, tools packages, and modules.
>
> Go by Example is a hands-on introduction to Go using annotated example programs.

## Tools

### [Healthchecks](https://github.com/healthchecks/healthchecks)

> Healthchecks is a cron job monitoring service. It listens for HTTP requests and email messages ("pings") from your cron jobs and scheduled tasks ("checks"). When a ping does not arrive on time, Healthchecks sends out alerts.

### [yt-dlp](https://github.com/yt-dlp/yt-dlp)

> A youtube-dl fork with additional features and fixes.

### [borg](https://github.com/borgbackup/borg)

> BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it supports compression and authenticated encryption.
>
> The main goal of Borg is to provide an efficient and secure way to backup data. The data deduplication technique used makes Borg suitable for daily backups since only changes are stored. The authenticated encryption technique makes it suitable for backups to not fully trusted targets.

## Other stuff

### [Autodocumenting Makefiles](https://daniel.feldroy.com/posts/autodocumenting-makefiles)

> When I type just make without any arguments, by default that triggers the help function, which runs the Python script at the top of the makefile.

## Podcasts

### [The Real Python Podcast - Episode 91: 2021 Real Python Articles Wrap Up](https://realpython.com/podcasts/rpp/91/)

> It’s been a year of change at Real Python! The Real Python team has written, edited, curated, illustrated, and produced a mountain of Python articles this year. We also added many new members to the team, updated the site’s features, and created new styles of tutorials and projects.

## Videos

### [Brandon Rhodes The Dictionary Even Mightier - PyCon 2017](https://www.youtube.com/watch?v=66P5FMkWoVU)

> Playback on other websites has been disabled by the video owner. [Watch on YouTube](https://www.youtube.com/watch?v=66P5FMkWoVU)

### [The Internet's Own Boy: The Story of Aaron Swartz](https://www.youtube.com/watch?v=9vz06QO3UkQ)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/9vz06QO3UkQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Modern Continuous Delivery • Ken Mugrage • GOTO 2019](https://www.youtube.com/watch?v=wjF4X9t3FMk)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/wjF4X9t3FMk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [PyWaw #97](https://www.youtube.com/watch?v=p9suUK4NpY0)

> Grzegorz Kocjan: Serverless - jak nie strzelić sobie w kolano
> Sebastian Buczyński: Domain-Driven Design, czyli jak nie zbudować kolejnego potworka
> Wojciech Rząsa: Mikroserwisy - od HTTP do Kafki

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/p9suUK4NpY0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [PyCon.DE 2017 Thomas Waldmann - The BorgBackup Project](hmttps://www.youtube.com/watch?v=oLFMsP1GMa0)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/oLFMsP1GMa0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
