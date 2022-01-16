Title: Month summary - September 2021
Date: 2021-09-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2021
Slug: 2021-september-links
Summary: Interesting stuff from the month
Status: published

# September 2021

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

At the end of the month I attended the meetup called [IT Depends #8: DataLake i wyzwania AdTechu, czyli jak nie utonąć w danych (DataLake and AdTech challenges, i.e. how not to drown in data)](https://www.linkedin.com/events/itdepends-8-datalakeiwyzwaniaad6830784358421458944/) organized by [Clearcode](https://clearcode.cc/) company.
There were two very interesting presentations:

<ul>
  <li> <b> Data Lake - co to jest i dlaczego lepiej nie robić z jeziora bagna?</b> (Data Lake - what is it and why is it better not to make a swamp out of a lake?) by Noemi</li>
  <li> <b>Change Data Capture, czyli jak wiedzieć o każdej zmianie w Twojej bazie danych</b> (Change Data Capture: how to know about every change in your database) by Dawid</li>
</ul>

Additionally I attended workshops where we played with [Debezium](https://github.com/debezium/debezium) which is <i>is an open source project that provides a low latency data streaming platform for change data capture</i>.
Whe used it to track changes in PostgreSQL database and stream them to Kafka from where they were consumed by a small JS app. The repository for this workshop is publicly available here: [ClearcodeHQ/it-depends-8](https://github.com/ClearcodeHQ/it-depends-8).

It was a very nicely conducted meetup which I happily attended, moreover I won some gadgets like a cup, a t-shirt and a book about data lakes.

## Articles

### [Best practices for writing code comments](https://stackoverflow.blog/2021/07/05/best-practices-for-writing-code-comments/)

> While it's easy to measure the quantity of comments in a program, it's hard to measure the quality, and the two are not necessarily correlated. A bad comment is worse than no comment at all.

### [How to improve your Docker containers security \[cheat sheet included\]](https://blog.gitguardian.com/how-to-improve-your-docker-containers-security-cheat-sheet/)

> Containers are no security devices. That's why we've curated a set of easily actionable recommendations to improve your Docker containers security.

### [GitHub Actions: Reduce duplication with action composition](https://github.blog/changelog/2021-08-25-github-actions-reduce-duplication-with-action-composition/)

> Previously, actions written in YAML could only use scripts. Now, they can also reference other actions. This makes it easy to reduce duplication in your workflows.

### [Picturing Git: Conceptions and Misconceptions](https://www.biteinteractive.com/picturing-git-conceptions-and-misconceptions)

> There’s an odd thing I’ve noticed about the way many developers use Git. Often, they don’t really have an accurate mental model of what Git is and what it does. It’s surprisingly easy to get used to employing a few basic Git commands without having any real idea of what they mean.

### [Five Ansible Techniques I Wish I’d Known Earlier](https://zwischenzugs.com/2021/08/27/five-ansible-techniques-i-wish-id-known-earlier)

> If you’ve ever spent ages waiting for an Ansible playbook to get through a bunch of tasks so yours can be tested, then this article is for you.

### [Technical documentation writing quick tips](https://marijkeluttekes.dev/blog/articles/2021/09/06/technical-documentation-writing-quick-tips/)

> These are tips that I give colleagues and pupils based on practical experience. Writing is a skill, and people have written entire books about the subject; hence this is a “quick tips” article.

## Python

### [The Unknown Features of Python's Operator Module](https://martinheinz.dev/blog/54)

> At the first glance Python's operator module might not seem very interesting. It includes many operator functions for arithmetic and binary operations and a couple of convenience and helper functions. They might not seem so useful, but with help of just a few of these functions you can make your code faster, more concise, more readable and more functional. So, in this article we will explore this great Python module and make the most out of the every function included in it.

### [145 Python Projects with Source Code](https://medium.com/coders-camp/130-python-projects-with-source-code-61f498591bb)

> Python is one of the best programming languages. Due to its readability and beginner-friendly nature, it has been accepted by industries around the world. So to master Python for any field you have to work on projects. In this article, I will take you through more than 130 Python projects with source code.

### [Mastering Web Scraping in Python: Scaling to Distributed Crawling ](https://www.zenrows.com/blog/mastering-web-scraping-in-python-scaling-to-distributed-crawling)

> Wondering how to build a website crawler and parser at scale? Implement a project to crawl, scrape, extract content, and store it at scale in a distributed and fault-tolerant manner.

### [How you can track your personal finances using Python](https://sgoel.dev/posts/how-you-can-track-your-personal-finances-using-python/)

> In this post, I'd like to describe how you can track your personal finances using a workflow that is highly focused on data privacy, is 100% self-hosted, and uses only the Python ecosystem.

### [Python Project-Local Virtualenv Management](https://hynek.me/til/python-project-local-venvs/)

> On UNIX-like operating systems you can have the Python equivalent of node_modules today, for every Python version, without changing your workflows.

### [FastAPI with Async SQLAlchemy, SQLModel, and Alembic](https://testdriven.io/blog/fastapi-sqlmodel/)

> This tutorial looks at how to work with SQLAlchemy asynchronously with SQLModel and FastAPI. We'll also configure Alembic for handling database migrations.

### [Python 3.10 – Simplifies Unions in Type Annotations](https://www.blog.pythonlibrary.org/2021/09/11/python-3-10-simplifies-unions-in-type-annotations/)

> The focus of this tutorial is to talk about PEP 604, which makes writing union types easier when adding type annotation (AKA: type hinting) to your codebase.

### [Writing unit tests for Lambda functions in Python](https://emshea.com/post/writing-python-unit-tests-lambda-functions)

> This post shares what I've learned about writing unit tests for Lambda functions. I'll explain what unit tests are and why they can help you write and make changes to your function code quickly. I've also written an example Python function and unit test (using the unittest framework) so you can see it in practice.

### [Type hints, protocols, and good sense](https://speakerdeck.com/ramalho/type-hints-protocols-and-good-sense)

> PyCon India keynote, presented September 19, 2021. Main sections: 1. The state of static typing in Python 2. The four modes of typing 3. The central role of typing.Protocol 4. Typing limits and how to address them.

### [Logging in Python like a PRO](https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/)

> I'll show you what good logging is with real-life examples. Most people don't know what to log, so they end up creating just noise....

### [Handling exceptions in Python like a PRO](https://blog.guilatrova.dev/handling-exceptions-in-python-like-a-pro/)

> One of the downsides of a flexible language like python is that people often assume that as long as something works then it's probably the proper way of doing so. I would like to write this humble guide on how to effectively use python exceptions and how to handle exceptions and log them correctly

### [Validating and Formatting Phone Numbers in Python with phonenumbers](https://stackabuse.com/validating-and-formatting-phone-numbers-in-python/)

> In this tutorial, we’ll learn how to parse, validate and extract phone numbers, as well as how to extract additional information from the phone number(s) like the carrier, timezone, or geocoder details.

### [Writing unit tests for Lambda functions in Python](https://emshea.com/post/writing-python-unit-tests-lambda-functions)

> This post shares what I've learned about writing unit tests for Lambda functions. I'll explain what unit tests are and why they can help you write and make changes to your function code quickly.

### [Why does Black insist on reformatting my entire project?](https://lukasz.langa.pl/36380f86-6d28-4a55-962e-91c2c959db7a/)

> For some users, one giant commit that reformats the world is an unpleasant thought. After all, it’s a “useless commit” and poisons git blame! I think that’s backwards.

## Django

### [Python and Django Logging in Plain English](https://djangodeconstructed.com/2018/12/18/django-and-python-logging-in-plain-english/)

> If you’ve ever written a program and printed out a value to see what’s going on during execution, then you understand at some level why logging is so valuable. Knowing what’s happening in your code at a point in time is enormously useful from both technical and business perspectives.

### [Python and Django Logging in Plain English](https://djangodeconstructed.com/2018/12/18/django-and-python-logging-in-plain-english/)

> If you’ve ever written a program and printed out a value to see what’s going on during execution, then you understand at some level why logging is so valuable. Knowing what’s happening in your code at a point in time is enormously useful from both technical and business perspectives.

### [I Built a Django Scaffold Library That Creates A Fully Functional REST API in Seconds](https://python.plainenglish.io/scaffold-django-apis-in-seconds-3fb1610a7908)

> [dr_scaffold](https://github.com/Abdenasser/dr_scaffold)This library will help you to scaffold full Restful API Resources in seconds using only one command.

### [Django React Boilerplate - With Free Samples](https://blog.appseed.us/django-react-boilerplate/)

> Learn how to bundle Django and React and code a full-stack boilerplate using this modern stack - with free samples.

### [Understand Django - User File Use](https://www.mattlayman.com/understand-django/media-files/)

> The latest installment in this series from Matt Layman covers file management, such as accepting images/files from users.

### [Using Celery task to generate data for a view](https://appliku.com/post/using-celery-task-to-generate-data-for-a-view)

> In this article we'll solve a problem when a view is taking too long to generate the response by moving actual data generation into the Celery task.

### [Django Base Site](https://github.com/epicserve/django-base-site)

> The Django Base Site is a Django site that is built using the best Django practices and comes with all the common Django packages that you need to jumpstart your next project.

## Python libraries

### [prettymaps](https://github.com/marceloprates/prettymaps)

> A minimal Python library to draw customized maps from OpenStreetMap data.

### [prettymaps](https://github.com/marceloprates/prettymaps)

> A minimal Python library to draw customized maps from OpenStreetMap data.

## Django libraries

### [Django cursor pagination](https://github.com/photocrowd/django-cursor-pagination)

> A cursor based pagination system for Django. Instead of refering to specific pages by number, we give every item in the queryset a cursor based on its ordering values. We then ask for subsequent records by asking for records after the cursor of the last item we currently have. Similarly we can ask for records before the cursor of the first item to navigate back through the list.

### [DjHTML](https://github.com/rtts/djhtml)

> A pure-Python Django/Jinja template indenter without dependencies.

### [Django Advanced Filters](https://github.com/modlinltd/django-advanced-filters)

> A django ModelAdmin mixin which adds advanced filtering abilities to the admin.

### [Django Cacheops](https://github.com/Suor/django-cacheops)

> A slick app that supports automatic or manual queryset caching and automatic granular event-driven invalidation.

## Tools

### [Debezium](https://github.com/debezium/debezium)

> Change data capture for a variety of databases.

## Cloud

### [Managing GCP service usage through delegated role grants](https://medium.com/google-cloud/managing-gcp-service-usage-through-delegated-role-grants-a843610f2226)

> Delegated role grants is a new feature in GCP that allows organization administrators to control which roles a user can grant or revoke even when the user has setIamPolicy permission on a resource. In other words, through delegated role grants organization administrators can give a user permissions to grant/revoke specific roles.

### [Awesome GCP Certifications](https://github.com/sathishvj/awesome-gcp-certifications)

> Google Cloud Platform Certification resources.

## Other stuff

### [Genius checklist](https://supermemo.guru/wiki/Genius_checklist)

> This article by Dr Piotr Wozniak is part of SuperMemo Guru series on memory, learning, creativity, and problem solving.

### [20 Reasons To Quit Social Media](https://durmonski.com/life-advice/reasons-to-quit-social-media/)

> The decision is up to you. You can either bombard your brain with endless distractions. Or you can use the time to dig deep on topics that actually interest you.

## Podcasts

### [The Real Python Podcast - Episode 77: Advantages of Completing Small Python Projects](https://realpython.com/podcasts/rpp/77/)

> Are you a beginner or intermediate Python programmer who has made it through some of the fundamentals? Have you tried to tackle a big project but got stuck and frustrated? Completing some small projects might be the answer. This week on the show, we have author Al Sweigart and talk about his new book, “The Big Book of Small Python Projects.”

## Videos

### [Natalia Stanko - Recovering from burnout - PyCode 2020](https://www.youtube.com/watch?v=uEat-OXaT9M)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/uEat-OXaT9M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
