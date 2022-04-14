Title: Month summary - March 2022
Date: 2022-03-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2022
Slug: 2022-march-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2022/2022_03_xx.jpg
Status: draft

# March 2022

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

Apache Software Foundation contacted me about my repo [Fetch Apache GitHub Actions Statistic](https://github.com/TobKed/fetch-apache-ga-stats).
To help them collect statistics and make setting up workflows from the repo easy and convenient I wrapped up all related infrastructure into [Terraform code](https://github.com/TobKed/fetch-apache-ga-stats/tree/master/terraform).
I enjoy figuring out connections between different cloud resources and since I am a fanboy of Terraform it was a pretty nice time spent this month working on that.

## Articles

### [The Thirty Minute Rule](https://daniel.feldroy.com/posts/thirty-minute-rule)

> The rule is that if anyone gets stuck on something for more than 30 minutes, they should ask for help.

### [A Slightly Advanced Introduction to Vim](https://linuxgazette.net/152/srinivasan.html)

> This is not a five minute introduction to vim for a complete newbie. I presume you have used vim before and are comfortable with moving around, and making changes. Although :vimtutor is not a prerequisite to this tutorial, I highly recommend it.
>
> This document contains some mnemonics, and some slightly advanced features of vim that can help the average vim user/programmer increase his/her productivity by leaps and bounds.

### [Scaling Django with Postgres Read Replicas](https://andrewbrookins.com/python/scaling-django-with-postgres-read-replicas/)

> Replication is a feature of PostgreSQL that you typically use to achieve high availability by running copies of a database that are ready to take over if your primary database fails. However, you can also use replication to make your Django applications faster. In this post, I’ll explain how to configure Django to query read-only Postgres replicas, allowing you to scale your database read performance linearly with the number of replicas.

### [How to design better APIs](https://r.bluethl.net/how-to-design-better-apis#heading-2-use-iso-8601httpsenwikipediaorgwikiiso8601-utc-dates)

> 15 language-agnostic, actionable tips on REST API design.

### [Some developers are fouling up open-source software](https://www.zdnet.com/article/some-developers-are-fouling-up-open-source-software/)

> From ethical concerns, a desire for more money, and simple obnoxiousness, a handful of developers are ruining open-source for everyone.

## Python

### [Mocking in Python Has Never Been Easier](https://peterkogan.medium.com/mocking-in-python-has-never-been-easier-5f9b15e1498f)

> The Pytest Mock Generator library simplifies writing the ‘arrange’ and ‘assert’ sections. It generates the ‘arrange’ and ‘assert’ sections for you and allows you to focus on the ‘act’ section of your tests.

### [How and why I use pytest's xfail](https://blog.ganssle.io/articles/2021/11/pytest-xfail.html)

> xfail vs skip
>
> The main difference is that with skip you don't run the test at all, whereas with xfail, you run the test and make sure that it failed (if it doesn't fail, it's marked as XPASS)

### [Modern Python Environments - dependency and workspace management](https://testdriven.io/blog/python-environments/)

> Once you get through the pain of setting up a Python environment for a single "hello world"-esque application, you'll need to go through an even more difficult process of figuring out how to manage multiple environments for multiple Python projects.

### [How to Write User-friendly Command Line Interfaces in Python](https://towardsdatascience.com/how-to-write-user-friendly-command-line-interfaces-in-python-cc3a6444af8e)

> The first step to make people love your application.

### [Python Built-in Functions To Know](https://www.pythonmorsels.com/built-in-functions-in-python/#commonly-overlooked)

> We're going to take a look at all 71 of Python's built-in functions, in a birds eye view sort of way.

### [Value objects with Python](https://blog.szymonmiks.pl/p/value-objects-with-python/)

> A Value object is a basic building block from tactical DDD (Domain Driven Design).

### [Processing large JSON files in Python without running out of memory](https://pythonspeed.com/articles/json-memory-streaming/)

> If you need to process a large JSON file in Python, it’s very easy to run out of memory. Even if the raw data fits in memory, the Python representation can increase memory usage even more.

### [Python Project Setup – Virtual Environments and Package Management](https://bas.codes/posts/python-virtualenv-venv-pip-pyenv-poetry)

> Modern Python projects need a bit more than venv and pip. Learn about the best tools for package management and environment isolation.

### [The Right Way To Compare Floats in Python](https://davidamos.dev/the-right-way-to-compare-floats-in-python/)

> Floating-point numbers are a fast and efficient way to store and work with numbers, but they come with a range of pitfalls that have surely stumped many fledgling programmers — perhaps some experienced programmers, too!

### [Python Built-in Functions To Know](https://www.pythonmorsels.com/built-in-functions-in-python/#commonly-overlooked)

> This will be a very long article, so I've linked to 5 sub-sections and 25 specific built-in functions in the next section so you can jump ahead if you're pressed for time or looking for one built-in in particular.

### [Why your mock doesn’t work](https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html)

> Mocking is a powerful technique for isolating tests from undesired interactions among components. But often people find their mock isn’t taking effect, and it’s not clear why. Hopefully this explanation will clear things up.

## Django

### [The 10 Most-Used Django Packages](https://learndjango.com/tutorials/10-most-used-django-packages)

> Inspired by a past article on [The 22 Most-Used Python Packages in the World](https://medium.com/better-programming/the-22-most-used-python-packages-in-the-world-7020a904b2e), I teamed up with [Jeff Triplett](https://jefftriplett.com/about/) to investigate the top 10 Django packages based on PyPI (The Python Package Index) downloads. We looked at the past 30 days though data from the past 365 days is also available.

### [Setting up a basic Django project with Poetry](https://builtwithdjango.com/blog/basic-django-setup)

> We will be using Pyenv and Poetry to manage the virtual environment and dependencies for your project.

### [How to deploy a Django application using NGINX and Gunicorn?](https://medium.com/@chaitanybhardwaj1997/how-to-deploy-a-django-application-using-nginx-and-gunicorn-aa584a8b7cc8)

> One thing that I have observed very ordinarily being practised is, that freshers or even experienced developers, when onboards on any new application, directly start developing stuff without even having any knowledge about how the application was deployed. This can cause them trouble when they’d be required to build an application from scratch and make it production-ready.

## Python libraries

### [wrapt](https://github.com/GrahamDumpleton/wrapt)

> The aim of the wrapt module is to provide a transparent object proxy for Python, which can be used as the basis for the construction of function wrappers and decorator functions.

### [attrs](https://github.com/python-attrs/attrs)

> Python Classes Without Boilerplate.

### [dateparser](https://github.com/scrapinghub/dateparser)

> python parser for human readable dates

## Django libraries

### [django-maintenance-mode](https://github.com/fabiocaccamo/django-maintenance-mode)

> django-maintenance-mode shows a 503 error page when maintenance-mode is on.
>
> It works at application level, so your django instance should be up.
>
> It doesn't use database and doesn't prevent database access.

### [django-query-capture](https://github.com/AsheKR/django-query-capture/)

> Django Query Capture can check the query situation at a glance, notice slow queries, and notice where N+1 occurs.

## Go

### [Introduction to DDD Lite: When microservices in Go are not enough](https://threedots.tech/post/ddd-lite-in-go-introduction/)

> When I started working in Go, the community was not looking positively on techniques like DDD (Domain-Driven Design) and Clean Architecture. I heard multiple times: “Don’t do Java in Golang!”, “I’ve seen that in Java, please don’t!".

## Tools

### [bpytop](https://github.com/aristocratos/bpytop)

> Resource monitor that shows usage and stats for processor, memory, disks, network and processes.

### [lf](https://github.com/gokcehan/lf)

> Terminal file manager

### [mpv](https://github.com/mpv-player/mpv)

> **mpv** is a free (as in freedom) media player for the command line. It supports a wide variety of media file formats, audio and video codecs, and subtitle types.

### [fzf](https://github.com/junegunn/fzf)

> **fzf** is a general-purpose command-line fuzzy finder.

### [awesome-tuis](https://github.com/rothgar/awesome-tuis)

> List of projects that provide terminal user interfaces

## Other stuff

### [github.com/rafi/.config](https://github.com/rafi/.config)

> Rafael Bodill's macOS/Archlinux dotfiles

### [Most influential books for programmers](https://github.com/cs-books/influential-cs-books)

> These are books considered most influential for programmers from this [StackOverflow thread](http://stackoverflow.com/questions/1711/what-is-the-single-most-influential-book-every-programmer-should-read).

## Videos

### [Dan Palmer - Scaling Django to 500 apps](https://www.youtube.com/watch?v=NsHo-kThlqI)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/NsHo-kThlqI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [David Brumley - How the Best Hackers Learn Their Craft](https://www.youtube.com/watch?v=6vj96QetfTg)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/6vj96QetfTg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
