Title: Month summary - January 2021
Date: 2021-01-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2021
Slug: 2021-january-links
Summary: Interesting stuff from the month
Status: published


# January 2021

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.


## Some thoughts

During this month I worked mostly on system tests for Apache Airflow.
System tests in Airflow are tests which execute example DAGs and hit real resources, e.g.: Google Cloud Storages and Amazon S3.
The huge advantage of them is that they can spot bugs which may slip in eventually or find breaking changes in external APIs.
The fact that they work with real services means that these services have to be enabled, and in some cases provisioned and configured before.
Cloud services have free tiers but still billing has to be configured and someone has to pay for it eventually.
This is not something many people will do, but since I am interested in the cloud I wanted to make the running of these tests more convenient.
It resulted in a repository: [politools/airflow-system-tests](https://github.com/politools/airflow-system-tests).
The tests are being run on Google Cloud Build which clones Airflow repository and runs system tests within the Breeze environment.
With one command, plenty of parallel tests may be executed.


## Articles

### [A Simple and Dynamic Method for Consistent Productivity](https://matthewsaltz.wordpress.com/2020/11/24/a-simple-and-dynamic-method-for-consistent-productivity/)

> About a month ago I started a new system that I really like, and I hope I will stay with it.

### [Doing Python development under Mac OS](https://peter-whittaker.com/install-python-MacOS)

> Easy-peasy. Right?

### [The 7 types of rest that every person needs](https://ideas.ted.com/the-7-types-of-rest-that-every-person-needs/)

> This post is part of TED’s “How to Be a Better Human” series, each of which contains a piece of helpful advice from people in the TED community.

### [System Design 101](https://stanete.com/system-design-101)

> Why is it so important to design our services so they have no state? Specially if they are running somewhere on a server.

### [20 Months in, 2K Hours Spent and 200K € Lost. A Story About Resilience and the Sunk Cost Fallacy](https://medium.com/swlh/20-months-in-2k-hours-spent-and-200k-lost-a-story-about-resilience-and-the-sunk-cost-fallacy-69fd4f61ef59)

> TL;DR: It can be really hard to know if we’re just resilient or falling for the sunk cost fallacy.

### [Time Awareness or How I Found Time for Life While Working Remotely](https://timeawareness.substack.com/p/time-awareness-and-remote-work)

> I quickly found out that not having a context switch between the office and home forced me into non-healthy behaviors like giving work all the available time.

### [10 Powerful Life Skills for the New Decade](https://neilkakkar.com/powerful-life-skills.html)

> Over the past few years, I’ve noticed certain skills in people I admire, from Paul Graham, Vitalik Buterin, to Ender Wiggin.

### [Equal pay for equal work](https://dusted.codes/equal-pay-for-equal-work)

> Remote work is on the rise, the economy is on a decline and businesses are re-structuring themselves around what many consider the new normal.

### [Pipenv & Requests Author Kenneth Reitz Interview](https://evrone.com/kenneth-reitz-interview)

> Kenneth Reitz: “Encapsulating concepts is better than extrapolating complexity.”

### [Sekurak: Konta Trumpa zbanowane we wszystkich istotnych serwisach społecznościowych](https://sekurak.pl/konta-trumpa-zbanowane-we-wszystkich-istotnych-serwisach-spolecznosciowych-amazon-apple-google-blokuje-parlera-cenzura-na-niespotykana-dotad-skale-czy-normalnosc/)

> Amazon/Apple/Google blokuje Parlera. Cenzura na niespotykaną dotąd skalę czy normalność?

### [Tech Companies Are Profiling Us From Before Birth](https://thereader.mitpress.mit.edu/tech-companies-are-profiling-us-from-before-birth/)

> Children today are the very first generation of citizens to be datafied from before birth. The social and political consequences of this historical transformation have yet to be seen.

### [With the Death of Cash, Privacy Faces a Deeply Uncertain Future](https://hackernoon.com/with-the-death-of-cash-privacy-faces-a-deeply-uncertain-future-l8c344v)

> The Coming Death of Cash and the Battle for the Future of Money. In One Future We have a Private, Anonymous Alternative to Cash but in the Black Mirror Future the Money in Your Pocket Knows Everything About You.

### [Degoogling my life](https://thefiringneuron.com/2021/01/17/degoogling-my-life/)

> Privacy is a human right, when so much of our life is lived online. In my opinion, the two most evil companies on the planet with a blatant disregard for privacy because it is so fundamental to their business model are: Facebook (and by extension, WhatsApp and Instagram) and Google.

### [Forget About SMART Goals: 5 Unconventional Goal Setting Methods to Try Instead](https://blog.doist.com/unconventional-goal-setting/)

> Traditional goal setting didn’t work for you last year? Try on something new...

### [Why senior engineers get nothing done](https://swizec.com/blog/why-senior-engineers-get-nothing-done)

> Remember when you started your job, how was it?

### [Burned Out and Fantasizing About a Big Life Reset? Start Here](https://blog.doist.com/burnout-career-life-reset/)

> Honest (and realistic) advice from those who’ve been there.

### [5 Tips to Speed up Your Docker Image Build](https://vsupalov.com/5-tips-to-speed-up-docker-build)

> Are your Docker builds taking forever? Docker can be a valuable part of your tool belt, or a constant source of annoyance.

## Python

### [5 JavaScript things you should know/understand as a Python Developer](https://zanderle.com/musings/2021/1/5-javascript-things-you-should-knowithunderstand-as-a-python-developer/)

> Modern JavaScript is in many ways very similar to Python. But it's also very different.

### [Web Authentication Methods Compared](https://testdriven.io/blog/web-authentication-methods/)

> In this article, we'll look at the most commonly used methods for handling web authentication from the perspective of a Python web developer.

## Django

### [7 concepts you should know to get a job as a Django developer](https://justdjango.com/blog/7-concepts-to-get-a-job/)

> In this post I'm going to explain the most important concepts you should know to get a job as a Django developer.

## Tools

### [PeterWhittaker/myDotFiles](https://github.com/PeterWhittaker/myDotFiles)

> Peter Whittaker dot files

### [Docker BuildKit: faster builds, new features, and now it’s stable](https://pythonspeed.com/articles/docker-buildkit)

> Over the past few years the Docker developers have been working on a new backend for building images, BuildKit.

### [GCPSketchnote](https://github.com/priyankavergadia/GCPSketchnote)

> GCPSketchnote

### [Dockerfile best practices ](https://github.com/hexops/dockerfile)

> This repository has best-practices for writing Dockerfiles that I (@slimsag) have quite painfully learned over the years both from my personal projects and from my work @sourcegraph. 

### [rsync-time-backup](https://github.com/laurent22/rsync-time-backup)

> This script offers Time Machine-style backup using rsync. It creates incremental backups of files and directories to the destination of your choice. The backups are structured in a way that makes it easy to recover any file at any point in time.

### [Joplin](https://github.com/laurent22/joplin)

> Joplin - an open source note taking and to-do application with synchronization capabilities for Windows, macOS, Linux, Android and iOS.

### [jenv](https://github.com/jenv/jenv)

> Master your Java Environment with jenv.

## Other stuff

### [Minimal safe Bash script template](https://betterdev.blog/minimal-safe-bash-script-template/)

> The opposite of "it's like riding a bike" is "it's like programming in bash".

## Videos

### ["Speeding up Your Docker Image Build" - Vladislav Supalov (PyConline AU 2020)](https://www.youtube.com/watch?v=LSiF8RNM1g)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube.com/embed/LSiF8RNM1g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [IT.talk 2020](https://www.youtube.com/watch?v=jfOGnsPkNiw)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube.com/embed/jfOGnsPkNiw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
