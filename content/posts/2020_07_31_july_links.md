Title: Month summary - July 2020
Date: 2020-07-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2020 
Slug: 2020-july-links
Summary: Interesting stuff from the month
Status: published

# July 2020

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

This month I made a few improvements in the release process of [Apache Beam](https://github.com/apache/beam) Python SDK and its CI/CD.
I connected building source distribution and wheels on GitHub Action with existing release scripts to work in cooperation now.
This allowed for the separate repository used for package preparation to be deprecated.
I spent a lot of time working with GitHub Action, therefore I released my own action called [github-forks-sync-action](https://github.com/TobKed/github-forks-sync-action).
It can be used to synchronise forked repositories with upstream.
I also made a contribution to [apache/airflow](https://github.com/apache/airflow) related to REST API by implementing DagSource endpoint.

## Articles

### [Beyond the Cache with Python and Redis](https://redislabs.com/blog/beyond-the-cache-with-python)

> A look at using Redis for caching, sub/pub events, data streaming, as a search engine, and even a primary database.

### [Git Interview Questions](https://www.git-tower.com/learn/git/faq/git-interview-questions)

> The essential list of frequently asked questions around Git and Version Control, including answers.

### [Why you shouldn't use ENV variables for secret data](https://diogomonica.com/2017/03/27/why-you-shouldnt-use-env-variables-for-secret-data/)

> The twelve-factor app manifesto recommends that you pass application configs as ENV variables. However, if your application requires a password, SSH private key, TLS Certificate, or any other kind of sensitive data, you shouldn't pass it alongside your configs.

### [PyDev of the Week: Philip James](https://www.blog.pythonlibrary.org/2020/07/06/pydev-of-the-week-philip-james)

> Philip James (@phildini) has spoken at various PyCons and DjangoCons and is the PyDev of the Week!

## Python

### [Pickle’s nine flaws](https://nedbatchelder.com/blog/202006/pickles_nine_flaws.html)

> Python’s pickle module is a very convenient way to serialize and de-serialize objects. It needs no schema, and can handle arbitrary Python objects. But it has problems. This post briefly explains the problems.

## Django

### [Invalid HTTP_HOST header errors in Django and Nginx](https://www.borfast.com/blog/2020/07/06/invalid-http_host-header-errors-in-django-and-nginx)

> An overview and fix for the common issue of Invalid HTTP_HOST header errors when running behind Nginx.

### [Running in Production: A Site to View 3D Scans of Cars with Twinner](https://runninginproduction.com/podcast/40-a-site-to-view-3d-scans-of-cars-with-twinner)

> Jesse Hunt talks about building a site with Django that lets you view 3D scans of cars with Twinner. It’s hosted on 2 Heroku hobby Dynos and has been up and running in production since January 2020.

### [Pure serverless Django with django-gcloud-connectors](https://dev.to/googlecloud/pure-serverless-django-with-django-gcloud-connectors-apo)

> Katie McLaughlin on configuring Django with the non-relational Google Datastore.

### [Django Log In with Email not Username](https://learndjango.com/tutorials/django-log-in-email-not-username)

> Update the default username/email/password pattern on login/signup with just email/password using a custom user model and django-allauth.

## Python libraries

### [tuna](https://github.com/nschloe/tuna)

> Performance analysis for Python.

## Tools

### [Awesome Actions](https://github.com/sdras/awesome-actions)

> A curated list of awesome things related to GitHub Actions.

### [GitHub Actions Advent Calendar](https://www.edwardthomson.com/blog/github_actions_advent_calendar.html)

> During the December 2019 Edward Thomson published an advent calendar of top tips for GitHub Actions.

## Other stuff

### [Help message for shell scripts](https://samizdat.dev/help-message-for-shell-scripts/)

> Yeah, there is always a way to show a message using cat (meow) or a bunch of echo calls. But there is a neat trick.

### [50 ideas that changed my life](https://www.perell.com/blog/50-ideas-that-changed-my-life)

> These are my guiding principles and the light of intellectual life of the author. All of them will help you think better, and I hope they inspire curiosity.

### [git commit accepts several message flags (-m) to allow multiline commits](https://www.stefanjudis.com/today-i-learned/git-commit-accepts-several-message-flags-m-to-allow-multiline-commits/)

> When you use git on the command line you might have used the message flag (-m). It allows developers to define commit messages inline when calling git commit.

### [gRPC → Episode 75 - Heroku Podcast codeish](https://www.heroku.com/podcasts/codeish/75-grpc)

> We’ll explore the capabilities of gRPC, a modern way for clients and servers to reliably communicate.

## Videos

### [Tutorial: Katie McLaughlin - Deploying Django on Serverless Infrastructure - PyCon 2020](https://www.youtube.com/watch?v=oYy9_4fm56o)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%"' src="https://www.youtube-nocookie.com/embed/oYy9_4fm56o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Workshop: Google: Charles Engelke - Serverless Python Applications with Google Cloud - PyCon 2020](https://www.youtube.com/watch?v=4bjX9iKqpXA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%"' src="https://www.youtube-nocookie.com/embed/4bjX9iKqpXA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
