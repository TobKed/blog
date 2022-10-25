Title: Month summary - September 2022
Date: 2022-09-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2022
Slug: 2022-september-links
Summary: Interesting stuff from the month
Status: published
Header_Cover: /images/posts/2022/2022_09_xx.jpg

# September 2022

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Articles

### [Customizing your shell](https://blog.balthazar-rouberol.com/customizing-your-shell.html)

> It is very common for programmers to tweak and customize their terminal and shell for hours,
> add or write new plug-ins, all in pursuit of the “perfect environment” and an increase of productivity.
> Others, on the contrary, avoid tweaking their shell altogether in order to always get the same experience on every machine.

### [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/)

> An in-depth exploration of the art of shell scripting.

### [Building a Web server in Bash, part I - sockets ](https://dev.to/leandronsp/building-a-web-server-in-bash-part-i-sockets-2n8b)

> Have you ever wondered how a Web server works under the hood?
> Moreover, would you be willing to sharpen your Shell scripting skills?

### [Working locally with GitHub PRs](https://noumenal.es/posts/working-local-with-prs-on-github/B01/)

> Working on a PR on django/djangoproject.com, a question came up about how to rebase if the GitHub UI doesn't offer exactly what you want:

> > What do you usually do in these situations?

### [Some ways to get better at debugging](https://jvns.ca/blog/2022/08/30/a-way-to-categorize-debugging-skills/)

> I thought the categorization was a very useful structure for thinking about how to get better at debugging, so I’ve reframed the five categories in the paper into actions you can take to get better at debugging.

### [Why your website should be under 14kB in size](https://endtimes.dev/why-your-website-should-be-under-14kb-in-size/)

> What is surprising is that a 14kB page can load much faster than a 15kB page — maybe 612ms faster — while the difference between a 15kB and a 16kB page is trivial.
>
> This is because of the TCP slow start algorithm. This article will cover what that is, how it works, and why you should care. But first we'll quickly go over some of the basics.

### [Docker Tip #94: Docker Compose v2 and Profiles Are the Best Thing Ever](https://nickjanetakis.com/blog/docker-tip-94-docker-compose-v2-and-profiles-are-the-best-thing-ever)

> I switched to v2 it because it's faster and profiles let you easily start specific services in different environments.

### [Supercharging A/B Testing at Uber](https://www.uber.com/en-PL/blog/supercharging-a-b-testing-at-uber/)

> “Immensely laborious calculations on inferior data may increase the yield from 95 to 100 percent.
> A gain of 5 percent, of perhaps a small total.
> A competent overhauling of the process of collection, or of the experimental design, may often increase the yield ten- or twelve-fold, for the same cost in time and labor.
> To consult the statistician after an experiment is finished is often merely to ask him to conduct a post mortem examination.
> He can perhaps say what the experiment died of. To utilize this kind of experience he must be induced to use his imagination, and to foresee in advance the difficulties and uncertainties with which, if they are not foreseen, his investigations will be beset.”
>
> - R. A. Fisher’s Presidential address to the 1st Indian Statistical Congress

### [The Productivity Guide: Time Management Strategies That Work](https://jamesclear.com/productivity)

> Let's define productivity. Productivity is a measure of efficiency of a person completing a task. We often assume that productivity means getting more things done each day. Wrong. Productivity is getting important things done consistently. And no matter what you are working on, there are only a few things that are truly important.
>
> Being productive is about maintaining a steady, average speed on a few things, not maximum speed on everything.

### [The Ivy Lee Method: The Daily Routine Experts Recommend for Peak Productivity](https://jamesclear.com/ivy-lee)

> Lee was a successful businessman in his own right and is widely remembered as a pioneer in the field of public relations. As the story goes, Schwab brought Lee into his office and said,
>
> - “Show me a way to get more things done.”
>
> - “Give me 15 minutes with each of your executives,” Lee replied.

### [Warren Buffett’s “2 List” Strategy: How to Maximize Your Focus and Master Your Priorities](https://jamesclear.com/buffett-focus)

> Let's talk about the simple 3-step productivity strategy that Warren Buffett uses to help his employees determine their priorities and actions.

### [Increasing development productivity with repository management](https://kalis.me/increasing-development-productivity-repository-management/)

> Do you have to manually clone all your repos? Of course not. This is where repository management comes in.

### [80 days to get into FAANG](https://towardsdatascience.com/80-days-to-get-into-faang-5c77f27d5224l)

> This article will give a summary of my journey. More importantly, it will outline and address my main preparations, routine, struggles, and how I overcame those. I will mainly focus on the technical interviews. I hope this will be useful for any aspiring SWE/MLE looking to make the next big jump.

### [The Most Effective Creatives Maximize Leverage, Not Hours Worked](https://towardsdatascience.com/the-most-effective-creatives-maximize-leverage-not-hours-worked-20ed0070fdd7)

> Forget ‘quiet quitting’: 3 strategies for creating more business impact with fewer hours

### [Why NoSQL Scales better than SQL](https://blog.devgenius.io/why-nosql-scales-better-than-sql-eb0b46b4aac5)

> Why are SQL data stores not as scalable as NoSQL? What is the reason that we need ‘NoSQL’ now?

### [How Did REST Come To Mean The Opposite of REST?](https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/)

> [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) must be the most broadly misused technical term in computer programming history.

## Python

### [Using Mypy in production at Spring](https://notes.crmarsh.com/using-mypy-in-production-at-spring)

> At Spring, we maintain a large Python monorepo with complete Mypy coverage configured under Mypy’s strictest available settings.
> In short, that means every function signature is annotated and implicit Any conversions are disallowed.

### [Why You Should Use More Enums In Python](https://florian-dahlitz.de/articles/why-you-should-use-more-enums-in-python)

> A gentle introduction to enumerations in Python.

### [Running Airflow on ARM M1/M2? Hell yes, but upgrade to Airflow 2.3+](https://medium.com/apache-airflow/running-airflow-on-arm-m1-m2-hell-yes-but-upgrade-to-airflow-2-3-2b4b4c855e1a)

> Over the last few months I had a lot of questions and discussions at Airflow Slack and in Airflow GitHub Issues about running Airflow on ARM (which was really all about running Airflow on Apple Silicon (M1/M2).
> Does it work? Can we use it? What if I buy the new Apple Laptop for my users who want to run Airflow locally (mostly for DAG development)?

### [Airflow’s Magic Loop](https://medium.com/apache-airflow/airflows-magic-loop-ec424b05b629)

> A simple optimization that saves us a significant running time.

### [10 Python Interview Questions for Senior Developers](https://medium.com/techtofreedom/10-python-interview-questions-for-senior-developers-4fefe773719a)

> Dive into the internals

### [5 Levels of Understanding the Mutability of Python Objects](https://medium.com/techtofreedom/5-levels-of-understanding-the-mutability-of-python-objects-a5ed839d6c24)

> Every Python programmer may have been confused about the mutability of objects. This concept is indeed a little difficult to understand in Python.

### [Python String Methods to Know](https://www.pythonmorsels.com/string-methods/)

> Python's strings have 47 methods. That's almost as many string methods as there are built-in functions in Python! Which string methods should you learn first?

### [30 PyTricks I've Learned By Joining the Real Python Mailing List.](https://dev.to/wiseai/30-pytricks-ive-learned-by-joining-the-real-python-mailing-list-227i)

> I subscribed to the Real Python mailing list two years ago, and I learned a lot of tips and tricks during that time. Even though it might seem like an odd way to learn Python, I have found it to be extremely helpful. I have written down some notes about the most useful tips and tricks that I have learned over the last two years, and I wanted to share them with you today.

### [Why You Should Use Data Classes in Python](https://www.giulianopertile.com/blog/why-you-should-use-dataclasses-in-python/)

> Don’t you know what a Data Class is? You know how to use it? And what is the difference with a regular class? Here in this post I will try to answer these questions and many more.

### [Recipes from Python SQLite docs](https://rednafi.github.io/reflections/recipes-from-python-sqlite-docs.html)

> While going through the documentation of Python's sqlite3 module, I noticed that it's quite API-driven, where different parts of the module are explained in a prescriptive manner.
> I, however, learn better from examples, recipes, and narratives.
> Although a few good recipes already exist in the docs, I thought I'd also enlist some of the examples I tried out while grokking them.

### [Heroku Alternatives for Python-based Applications](https://testdriven.io/blog/heroku-alternatives/)

> Unfortunately, starting November 28, 2022, Heroku will discontinue its free tier. This means you'll no longer be able to leverage free dynos, Postgres databases, and Redis instances.

## Django

### [Django Shared Property](https://github.com/schinckel/django-shared-property)

> Properties that are both ORM expressions and python code.

### [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)

> You’ve built a shiny Django app and want to release it to the public, but you’re worried about time-intensive tasks that are part of your app’s workflow. You don’t want your users to have a negative experience navigating your app. You can integrate Celery to help with that.

## Tools

### [dotfiles](https://dotfiles.github.io/)

> Your unofficial guide to dotfiles on GitHub.

### [Awesome dotfiles](https://github.com/webpro/awesome-dotfiles)

> A curated list of dotfiles resources. Inspired by the [awesome](https://github.com/sindresorhus/awesome) list thing. Note that some articles or tools may look old or old-fashioned, but this usually means they're battle-tested and mature (like dotfiles themselves). Feel free to propose new articles, projects or tools!

## Cloud

### [Kubernetes examples](https://k8s-examples.container-solutions.com/)

> A series of YAML references with canonical and as-simple-as-possible demonstrations of kubernetes functionality and features.

### [Google Kubernetes Engine: 7 years and 7 amazing benefits](https://cloud.google.com/blog/products/containers-kubernetes/benefits-of-using-kubernetes)

> Today, as we celebrate seven years of general availability of the most automated and scalable managed Kubernetes,
> Google Kubernetes Engine (GKE), we present seven of the common ways that GKE helps customers do amazing things.

### [Make the most of your cloud deployment with Active Assist](https://cloud.google.com/blog/topics/developers-practitioners/make-most-your-cloud-deployment-active-assist)

> The vastness of the cloud (hundreds of products within Google Cloud and counting!) can make it difficult to take full advantage of the wide range of opportunities and optimizations it brings.
> Constantly tuning your deployment can quickly become tedious work due to the sheer magnitude of options.

### [A visual tour of Google Cloud certifications](https://cloud.google.com/blog/topics/training-certifications/which-google-cloud-certification-exam-should-you-take)

> Interested in becoming Google Cloud certified? Wondering which Google Cloud certification is right for you? We’ve got you covered.

### [Preparing for the Google Cloud Professional Cloud DevOps Engineer Exam](https://medium.com/google-cloud/preparing-for-the-google-cloud-professional-cloud-devops-engineer-exam-30e9d5fe07e4)

> If you want to learn about Site Reliability Engineering (SRE) and DevOps tools available in Google Cloud then the Google Professional Cloud DevOps Engineer certification is the right challenge for you.

### [Introducing Google Cloud Logging Python v3.0.0](https://medium.com/google-cloud/introducing-google-cloud-logging-python-v3-0-0-4c548663bab4)

> Manage your app’s Python logs and related metadata using Google Cloud.

### [Streaming from Google Cloud Pub/Sub to Bigquery without the Middlemen](https://medium.com/google-cloud/streaming-from-google-cloud-pub-sub-to-bigquery-without-the-middlemen-327ef24f4d15)

> Thus, to simplify it further and for such simple use-cases, Google has now launched direct streaming capability from Pub/Sub via “BigQuery Subscription”. In addition, Pub/Sub topic schemas provide the option of writing Pub/Sub messages to BigQuery tables with compatible schemas. If the schema is not enabled for your topic, messages will be registered as bytes or strings to the given BigQuery table.

### [Google Cloud Global External HTTP(S) Load Balancer - Deep Dive](https://cloud.google.com/blog/topics/developers-practitioners/google-cloud-global-external-https-load-balancer-deep-dive)

> Load balancing in Google Cloud is a fully scalable, distributed and redundant managed service offered in different flavors such as global external, regional external, and regional internal.

### [What is Kubernetes HPA and How Can It Help You Save on the Cloud?](https://cast.ai/blog/what-is-kubernetes-hpa-and-how-can-it-help-you-save-on-the-cloud/)

> Autoscaling is a core capability of Kubernetes. The tighter you configure the scaling mechanisms – HPA, VPA, and Cluster Autoscaler – the lower the waste and costs of running your application.

### [Building a secure CI/CD pipeline using Google Cloud built-in services](https://cloud.google.com/blog/products/devops-sre/devsecops-and-cicd-using-google-cloud-built-in-services)

> In this blog, we will be focusing on the tools and technology side of DevOps. At the core of the technical aspect of DevOps, the concept is Continuous Integration and Continuous Delivery (CI/CD). The idea behind CI/CD concept is to create an automated software delivery pipeline that continuously deploys the new software releases in an automated fashion.

### [Kubernetes CLI (kubectl) tips you didn't know about](https://learncloudnative.com/blog/2022-05-10-kubectl-tips)

> There are so many excellent tips I decided to collect the most interesting ones in a single post.

## Other stuff

### [Docuseek](https://docuseek2.com/)

> Docuseek streams essential independent, social-issue and environmental films to colleges, universities and K-12 schools, providing exclusive access to content from renowned leaders in documentary film distribution.

## Podcasts

### [ Aplikacja minimalizmu w codziennym życiu - Art Balsam | NZDL #021 ](https://www.youtube.com/watch?v=B9sLaQqmulM)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/B9sLaQqmulM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Videos

### [TechWorld with Nana: Microservices explained - the What, Why and How?](https://www.youtube.com/watch?v=rv4LlmLmVWk)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/rv4LlmLmVWk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [TechWorld with Nana: Istio & Service Mesh - simply explained in 15 mins](https://www.youtube.com/watch?v=16fgzklcF7Y)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/16fgzklcF7Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
