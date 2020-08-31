Title: Month summary - August 2020
Date: 2020-08-31
Category: python
Tags: python, blog, podcast, series, aggregate
Slug: 2020-august-links
Summary: Interesting stuff from the month
Status: draft


# August 2020

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

This month I worked mostly on the Apache Beam project. One of the biggest achievements this month was introducing cross platform test suites which run on GitHub Actions. These test suites verify Java and Python Beam SDKs by running unit and integration tests on Linux, MacOS and Windows platforms. I used Atlassian Python API wrapper to automate creation of Jira issues for tests which fail on Windows. 

I also developed a proposal for the Beam Metrics Report mail handled by Jenkins scheduled job. Mail will be created by fetching metrics data from influxDB and generating a table with a comparison of mean metric values from last and previous week with highlighted deviations and links to the corresponding Grafana dashboards. It will allow to quickly detect possible regressions.

Additionally, for an internal project I developed a small application which synchronizes data from Google Drive with the Datastore database. It  is deployed on Google Cloud Platform free of charge. It consists of Cloud Function written in Python which is triggered periodically by Cloud Scheduler. Infrastructure is defined as Terraform files which enabled easy development of Continuous Integration / Continuous Delivery pipeline on GitLab platform.

## Articles

### [15 Command-Line Tools to Make You Better at Shell & CLI](https://dev.to/zaiste/15-command-line-tools-to-make-you-better-at-shell-cli-35n6)

> Shell is the essential tool for every programmer. Here's a list of command-line tools that aim to provide modern, often much faster, alternatives to the existing shell commands.

### [Do not trust Google](https://lukeboyle.com/blog-posts/2020/08/do-not-trust-google)

> Facebook seems to be our current punching bag of choice because of their supposed ability to manipulate political opinion, but in my opinion Google is a much more insidious company with far greater potential for abuse.

### [What's it like as a Senior Engineer?](https://www.zainrizvi.io/blog/whats-it-like-as-a-senior-engineer/)

> Experiences working at Google & Microsoft

### [New Case Studies About Google’s Use of Go](https://opensource.googleblog.com/2020/08/new-case-studies-about-googles-use-of-go.html)

> Go has turned out to have a much broader reach than we had ever expected. Its growth in the industry has been phenomenal, and it has powered many projects at Google.

## Python

### [What Are Python Wheels and Why Should You Care?](https://realpython.com/python-wheels/)

> In this tutorial, you’ll learn what Python wheels are and why you should care as both a developer and end user of Python packages. You’ll see how the wheel format has gained momentum over the last decade and how it has made the package installation process faster and more stable.

### [Delete entities of Datastore in bulk with Dataflow implemented in Python](https://levelup.gitconnected.com/delete-entities-of-datastore-in-bulk-with-dataflow-implemented-in-python-37cbe2dd7e08)

> A simple way to delete entities in bulk with Apache Beam Python SDK on Dataflow and the way to run a pipeline with runtime parameters

## Django

### [Customize the Django Admin With Python](https://realpython.com/customize-django-admin-python)

> This Django Admin tutorial covers a little bit of everything.

### [A minimal Websockets setup with Django in production](https://www.untangled.dev/2020/08/02/django-websockets-minimal-setup/)

> J.V. Zammit shows us how to setup WebSockets in production and an interesting use-case for doing so.

### [A breakdown of how NGINX is configured with Django](https://mattsegal.dev/nginx-django-reverse-proxy-config.html)

> Matt Segal covers Nginx in depth.

### [Using Postgres JSONB Fields in Django](https://pganalyze.com/blog/postgres-jsonb-django-python)

> This article walks through the different types of JSON fields, querying JSONB data in Postgres, Django’s support for JSONB, and potential limitations of JSONB fields.

### [Django Views — The Right Way](https://spookylukey.github.io/django-views-the-right-way/)

> Views are one of the core components of a Django application. Django offers two kinds of views: function-based views and class-based views. Which one should you use? Fortunately, there’s an opinionated guide to help you sort things out!

## Tools

### [ytop - system monitor](https://github.com/cjbassi/ytop)

> Another TUI based system monitor, this time in Rust!

### [Public APIs](https://github.com/public-apis/public-apis)

> A collective list of free APIs for use in software and web development.

### [GitHub public roadmap](https://github.com/github/roadmap)

> GitHub product roadmap is where you can learn about what features GitHub team are working on, what stage they're in, and when they expect to bring them to you.

## Videos

### [Szersze spojrzenie na Backend - Szymon Przedwojski | Przeprogramowani ft. Gość #5](https://www.youtube.com/watch?v=c-Gi7OaykQo)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%"' src="https://www.youtube.com/embed/c-Gi7OaykQo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
