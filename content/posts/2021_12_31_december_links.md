Title: Month summary - December 2021
Date: 2021-12-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2021
Slug: 2021-december-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2021/2021_12_xx.jpg
Status: published

# December 2021

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

#### Blog

Last month I stumbled upon the [Jack De Winter blog](https://jackdewinter.github.io/) where he published a few articles
about [Pelican](https://blog.getpelican.com/), a static website generator written in Python which powers my blog as well.
Inspired by those articles I made some improvements, like:

- enabling website crawling
- adding a RSS channel
- small styling improvements

I also wrote some small sloppy Python script which verifies all links on the website
(there may be some typos or pages that were turned down etc.).
I had a good time playing with configuration and scripting.

#### Posts

I published two blog posts this month:

- [Productivity course]({filename}/posts/2021_04_15_productivity.md) - this post waited in the queue for a few months to be published
- [Django application on Google Cloud Platform]({filename}/posts/2021_12_30_django_on_gcp.md) - the idea for this post was born in 2020,
  however since so many unexpected things happened last year it was not the highest priority to complete it. I published it successfully this year.

<p></p>

#### Presentation: Terraform

While working on [Django application on Google Cloud Platform]({filename}/posts/2021_12_30_django_on_gcp.md) I spent some
time playing with Terraform. Since I like it very much, it led  me to this thought: why not make some small presentation about it?
I contacted folks from [Brival](https://www.brival.co/), agreed on the date, and it went pretty well in my opinion.
I not only described some theory but also spun up and tore down some examples of infrastructure on GCP.
It was pretty nice to meet with people, and I had a good time giving the talk. Cheers and Happy Terraforming.

## Articles

### [How to read a code](https://www.iamjonas.me/2020/08/how-to-read-code.html)

> More common is to be thrown into an ongoing project. Or even more common is to be added to a project because key personnel left. With no time for handover. So how do you get up to speed and make changes with confidence then?

### [Overview mode](https://www.iamjonas.me/2020/06/overview-mode.html)

> were not spending enough time upfront explicitly stating and understanding what the problem we're solving really is. Once well understood we can then propose a solution and assessing whether that solution actually solves the proposed problem. It involves writing things down. A lot.

### [The boring technology behind a one-person Internet company - The Official Listen Notes Blog ](https://www.listennotes.com/blog/the-boring-technology-behind-a-one-person-23/)

> After reading this post, you should be able to replicate what I build for Listen Notes or easily do something similar. You don’t need to hire a lot of engineers.

### [Want to be great? Know a lot](https://www.iamjonas.me/2021/10/want-to-be-great-know-lot.html)

> To become better you need to know what's out there. You need to turn the unknown unknowns into known unknowns.

### [The Well-Maintained Test: 12 Questions for New Dependencies](https://adamj.eu/tech/2021/11/04/the-well-maintained-test/)

> Joel Spolsky’s infamous [Joel Test](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/) is a quick heuristic test for checking a software engineering team’s technical chops. I’ve come up with a similar test that we can use to decide whether a new package we’re considering depending on is well-maintained.>

### [The Joel Test: 12 Steps to Better Code](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/)

> I’ve come up with my own, highly irresponsible, sloppy test to rate the quality of a software team.

### [Unconfusing Unicode: What is Unicode?](https://regebro.wordpress.com/2011/03/23/unconfusing-unicode-what-is-unicode/)

> Unicode can be very confusing and I see a lot of questions and problems based on the same misconceptions.

### [~jpetazzo/Anti-Patterns When Building Container Images](https://jpetazzo.github.io/2021/11/30/docker-build-container-images-antipatterns/)

> This is a list of recurring anti-patterns that I see when I help folks with their container build pipelines, and suggestions to avoid them or refactor them into something better.

### [Against the Trap of Efficiency: The Counterintuitive Antidote to the Time-Anxiety That Haunts and Hampers Our Search for Meaning](https://www.themarginalian.org/2021/12/20/four-thousand-weeks-oliver-burkeman/)

> “Productivity is a trap. Becoming more efficient just makes you more rushed, and trying to clear the decks simply makes them fill up again faster… Since finitude defines our lives… living a truly authentic life — becoming fully human — means facing up to that fact.”
>
> By Maria Popova

## Python

### [Writing Simple Python GUIs for your Command-Line-Phobe Coworkers](https://cushychicken.github.io/python-guis-for-heretics/)

> Why add a GUI? Simple: your coworkers know GUIs, and they love GUIs. They love them, even if they’ve never heard the term “GUI” and don’t know what “GUI” means.

### [Fine Tuning Pelican: Enabling Website Crawling](https://jackdewinter.github.io/2019/10/30/fine-tuning-pelican-enabling-website-crawling/)

> It is worthwhile to ensure that the website is properly set up to regulate any web crawling that does occur. This article details the setup required to enable this regulation.

### [Internals of sets and dicts](https://www.fluentpython.com/extra/internals-of-sets-and-dicts/)

> Understand how Python dictionaries and sets are built with hash tables to make sense of their strengths and limitations.

### [Writing fast async HTTP requests in Python](https://blog.jonlu.ca/posts/async-python-http)

> I do a lot of web scraping in my spare time, and have been chasing down different formats and code snippets to make a large amount of network requests locally, with controls for rate limiting and error handling.

### [Handling exceptions in Python like a PRO 🐍 💣](https://guicommits.com/handling-exceptions-in-python-like-a-pro/)

> One of the downsides of a flexible language like python is that people often assume that as long as something works then it's probably the proper way of doing so. I would like to write this humble guide on how to effectively use python exceptions and how to handle exceptions and log them correctly.

### [Structuring exceptions in Python like a PRO 🐍 🏗️ 💣](https://guicommits.com/how-to-structure-exception-in-python-like-a-pro/)

> Given now you know how to properly [handle your exceptions](https://guicommits.com/handling-exceptions-in-python-like-a-pro/) with [Tryceratops](https://guicommits.com/project-tryceratops/) 🦖 help, the next step is to structure them effectively so you can scale and reuse them.

### [The One Python Library Everyone Needs](https://glyph.twistedmatrix.com/2016/08/attrs.html)

> Use[ _attrs_](https://github.com/python-attrs/attrs). Use it. Use it for everything.

## Django

### [The definitive guide to modeling polymorphism in Django](https://confuzeus.com/hub/django-web-framework/model-polymorphism/)

> Polymorphism allows you to use one type of object to work with multiple kinds of data.
> Django makes it super easy to model your database, including polymorphism.
> However, it also makes it too easy to design a poor performing database.

## Python libraries

### [sitemap - Pelcian plugin](https://github.com/pelican-plugins/sitemap)

> Generates a site map for Pelican-powered sites.

### [attrs](https://github.com/python-attrs/attrs)

> _attrs_ is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods).

### [cluegen](https://github.com/dabeaz/cluegen)

> Cluegen is a library that allows you to define data classes using Python type clues.

## Cloud

### [AWS Organizations with Terraform Workspaces](https://guicommits.com/why-use-aws-organizations-with-terraform/)

> How to use AWS Organizations to your advantage with meaningful examples, and how to use terraform to manage it and replicate resources across them.

## Other stuff

### [Awesome-Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)

> A list of Free Software network services and web applications which can be hosted on your own servers.

### [joplin](https://github.com/laurent22/joplin/)

> Joplin - an open source note taking and to-do application with synchronization capabilities for Windows, macOS, Linux, Android and iOS.

### [ALL about RSS](https://github.com/AboutRSS/ALL-about-RSS)

> A list of RSS related stuff: tools, services, communities and tutorials, etc.

### [adamchainz/mac-ansible](https://github.com/adamchainz/mac-ansible)

> Configuring my mac with Ansible

### [cat -v harmful stuff](https://harmful.cat-v.org/)

> Encyclopedia of things considered harmful.

## Podcasts

### [Porozmawiajmy o IT #143: Pasja informatyki](https://porozmawiajmyoit.pl/poit-143-pasja-informatyki/)

> Dziś moim gościem jest Mirosław Zelent  – programista freelancer, nauczyciel, współtwórca kanału Pasja informatyki na YouTube, podcaster. Fan filozofii, psychologii, rozwoju i ludzi.

### [Darknet Diaries: EP 101: Lotería](https://darknetdiaries.com/episode/101/)

> In 2014 the Puerto Rico Lottery was mysteriously losing money. Listen to this never before told story about what happened and who did it.

### [PythpnBytes - Episode #264: We're just playing games with Jupyter at this point](https://pythonbytes.fm/episodes/show/264/we-re-just-playing-games-with-jupyter-at-this-point)

> Special guest: Kim van Wyk

### [The Real Python Podcast - Episode 90: A Python Journey: Cyber Security, Automating AWS, and TDD](https://realpython.com/podcasts/rpp/90/)

> Hugh has a background in programming C and Perl and started to use Python in a cyber security job. He explains the way he used Python to search for malware. Hugh provides some suggestions for security packages and tools.

## Videos

### [Travis Fischer, Esther Nam: Character encoding and Unicode in Python - PyCon 2014](https://www.youtube.com/watch?v=Mx70n1dL534)

> Playback on other websites has been disabled by the video owner. [Watch on YouTube](https://www.youtube.com/watch?v=Mx70n1dL534)

### [Hammock Driven Development - Rich Hickey](https://www.youtube.com/watch?v=f84n5oFoZBc)

> Playback on other websites has been disabled by the video owner. [Watch on YouTube](https://www.youtube.com/watch?v=f84n5oFoZBc)

### [HS Talks w Hackerspace Silesia! #2](https://www.youtube.com/watch?v=PISWsNC6XaU)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube.com/embed/PISWsNC6XaU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Raymond Hettinger - Dataclasses: The code generator to end all code generators - PyCon 2018](https://www.youtube.com/watch?v=T-TwcmT6Rcw)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube.com/embed/T-TwcmT6Rcw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
