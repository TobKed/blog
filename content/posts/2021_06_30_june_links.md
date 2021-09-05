Title: Month summary - June 2021
Date: 2021-06-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2021
Slug: 2021-june-links
Summary: Interesting stuff from the month
Status: published


# June 2021

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Articles

### [8 Tips to Improve Remote Work Communication With Your Teammates](https://weworkremotely.com/8-tips-to-improve-remote-work-communication-with-your-teammates)

> Stellar communication skills are a number one priority for remote employees. It’s how global teams stay on the same page and reach milestones and goals together.

### [Best Practices Around Production Ready Web Apps with Docker Compose](https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose)

> Here's a few patterns I've picked up based on using Docker since 2014. I've extracted these from doing a bunch of freelance work.

### [SSH quoting](https://www.chiark.greenend.org.uk/~cjwatson/blog/ssh-quoting.html)

> A while back there was a thread on one of our company mailing lists about SSH quoting, and I posted a long answer to it. Since then a few people have asked me questions that caused me to reach for it, so I thought it might be helpful if I were to anonymize the original question and post my answer here.

### [How to Handle Secrets on the Command Line](https://smallstep.com/blog/command-line-secrets/)

> The command line really wasn’t designed for secrets. So, keeping secrets secret on the command line requires some extra care and effort.

### [Disasters I've seen in a microservices world](https://world.hey.com/joaoqalves/disasters-i-ve-seen-in-a-microservices-world-a9137a51)

>  The "Netflix OSS stack" was the coolest thing back then, allowing engineers worldwide to leverage Netflix's lessons in distributed systems. More than six years later, if we look into software engineering jobs right now, most of them talk about a microservices' architecture.

### [I made 56874 calls to explore the telephone network. Here’s what I found.](https://shufflingbytes.com/posts/wardialing-finnish-freephones/)

> What kind of systems are there in the Finnish telephone network today?

### [The ritual of the deploy](https://veekaybee.github.io/2021/06/20/the-ritual-of-the-deploy/)

> Humans have always been terrible at dealing with uncertainty. Historically, we used to cope with it by inventing superstitions. The ancient world is filled with rituals to ward off potential ill omens during times that were especially out of the control of human capability.

### [Load Testing with Gatling II](https://theartfultester.com/blog/2021/06/25/load-testing-with-gatling-2/)

> It seems to me that performance testing is often neglected and pushed back as a “nice to have” stretch-goal, instead of being a core part of the test automation strategy. So if you’re putting it off because it seems intimidating or difficult, you’ve come to the right place.

### [Setting Memory And CPU Limits In Docker](https://www.baeldung.com/ops/docker-memory-limit)

> There are many cases in which we need to limit the usage of resources on the docker host machine. In this tutorial, we'll learn how to set the memory and CPU limit for docker containers.

## Python

### [How to iterate over DataFrame rows (and should you?)](https://www.wrighters.io/how-to-iterate-over-dataframe-rows-and-should-you/)

> One of the most searched for (and discussed) questions about pandas is how to iterate over rows in a DataFrame.

### [70+ Python Projects for Beginner, Intermediate And Experienced Developers](https://www.theinsaneapp.com/2021/06/list-of-python-projects-with-source-code-and-tutorials.html)

> Building hands-on projects will help you gain practical coding skills.

### [Cleaning up you test suite with pytest parametrize](https://sleepy.yaks.industries/posts/pytest-parametrize/?)

> I admit I jumped on the pytest ship quite late, after a few years of relying on the good ol’ unittest module, and for a good part they worked reasonably well for me, for little apparent incentive to something else.

### [How to troubleshoot memory problems in Python](https://innovation.alteryx.com/how-to-troubleshoot-memory-problems-in-python/)

> Finding out that an application is running out of memory is one of the worst realizations a developer can have. Memory problems are hard to diagnose and fix in general, but I’d argue it’s even harder in Python.

### [Typeclasses in Python](https://sobolevn.me/2021/06/typeclasses-in-python)

> Today I am going to introduce a new concept for Python developers: typeclasses. It is a concept behind our new dry-python library called classes.

## Django

### [Understanding Django Application LifeCycle.](https://sachinchaurasiya.hashnode.dev/understanding-django-application-lifecycle)

> Understanding the flow of the application is an important part of application development. Flow like when user hit a particular URL then, what action needs to be taken, what type of response we should give back to the user and all.

### [How to Build a Webhook Receiver in Django](https://adamj.eu/tech/2021/05/09/how-to-build-a-webhook-receiver-in-django/)

> A common way to receive data in a web application is with a webhook. The external system pushes data to yours with an HTTP request.
> 
> Correctly receiving and processing webhook data can be vital to your application working. In this post we’ll create a Django view to receive incoming webhook data.

### [Django on CloudRun](https://devblog.kogan.com/blog/django-on-cloudrun)

> We've recently discovered the wonders of a CloudRun stack here at Kogan.
> 
> As a fast moving business we often need to quickly spin up new projects to demonstrate new ideas. We previously used Heroku, but for low-traffic or internal sites we didn't need the application to be running constantly: we're looking for a serverless solution! 

### [Permissions in Django Rest Framework](https://testdriven.io/blog/drf-permissions/)

> This article looks at how permissions work in Django REST Framework (DRF).

### [Custom Relationships In Django](https://devblog.kogan.com/blog/custom-relationships-in-django)

> Before working with Django at Kogan I used SQLAlchemy. One of the many features I liked about SQLAlchemy was you had the freedom to join tables on any clause. This is especially useful for when you have a not-quite-normal schema and the data almost matches.

### [JWT Authentication in Django](https://code.tutsplus.com/tutorials/how-to-authenticate-with-jwt-in-django--cms-30460)

> This tutorial will give an introduction to JSON Web Tokens (JWT) and how to implement JWT authentication in Django.

### [YAGNI exceptions](https://lukeplant.me.uk/blog/posts/yagni-exceptions/)

> You Aren’t Gonna Need It — the principle that you should add features to your software.
> However, there are some things which really are easier to do earlier than later.

### [Built-in Permission Classes in Django Rest Framework](https://testdriven.io/blog/built-in-permission-classes-drf/)

> This article looks at how the built-in permission classes work in Django REST Framework (DRF).

### [How to use Python’s HTTPStatus with Django](https://adamj.eu/tech/2021/06/30/how-to-use-httpstatus-in-django)

> A “magic number” is the anti-pattern of using a number directly rather than storing it in a descriptive variable name. In web code HTTP status codes are often used as magic numbers, perhaps because web developers memorize common codes such as 200 and 404.

### [django docs:  Database access optimization¶](https://docs.djangoproject.com/en/3.2/topics/db/optimization)

> Django’s database layer provides various ways to help developers get the most out of their databases. This document gathers together links to the relevant documentation, and adds various tips, organized under a number of headings that outline the steps to take when attempting to optimize your database usage.

## Django libraries

### [django-guardian](https://github.com/django-guardian/django-guardian)

> django-guardian is an implementation of per object permissions [1] on top of Django's authorization backend.

## Tools

### [infracost](https://github.com/infracost/infracost)

> Infracost shows cloud cost estimates for infrastructure-as-code projects such as Terraform. It helps DevOps, SRE and developers to quickly see a cost breakdown and compare different options upfront.

## Cloud

### [Use multiple paths in Cloud Functions, Python and Flask](https://medium.com/google-cloud/use-multiple-paths-in-cloud-functions-python-and-flask-fc6780e560d3)

> Function as a Service, or FaaS, has been a cornerstone in app development. Popularized by AWS Lambda service, all the major Cloud Providers offer their version, with different features. And they also extend this principle to containers, with Cloud Run on Google Cloud for example.

## Other stuff

### [Free Dev Stuff](https://freestuff.dev/)

> List of free stuff or services for developer by developer to use. Some services free forever or have a free tier at least for 1 year.

### [devops-exercises](https://github.com/bregman-arie/devops-exercises)

> This repo contains questions and exercises on various technical topics, sometimes related to DevOps and SRE :)

## Podcasts

### [The Time Ferries Show = Richard Schwartz — IFS, Psychedelic Experiences without Drugs, and Finding Inner Peace for Our Many Parts (#492)](https://tim.blog/2021/01/14/richard-schwartz-internal-family-systems/)

> We are locking up these parts of us that are so wonderful and have so many talents… when they’re not locked up and when they’re not stuck in the past.
>   — Richard Schwartz

## Videos

### [PyCon US 2021 - Playlist](https://www.youtube.com/playlist?list=PL2Uw4_HvXqvYk1Y5P8kryoyd83L_0Uk5K)

> 87 talks from PyCon US 2021.

### [Python Web Conf 2021 Talks + Tutorials](https://www.youtube.com/playlist?list=PLt4L3V8wVnF4iB8pGfkR7eozIJPwCM7vv)

> The 3rd annual Python Web Conference (#PWC2021) took place virtually on March 22-26, 2021 on LoudSwarm by Six Feet Up.

### [Astronomer - [Webinar Recap] Getting Started With the Official Airflow Helm Chart](https://astronomer.wistia.com/medias/gviwd9gp2c)

> In this webinar we’ll show you how to: - Create a Kubernetes cluster with KinD in local - Deploy Airflow in a few seconds with the Official Helm Chart - Discover the first parameters to configure in the Helm Chart - Synchronize your DAGs with a Git repository.

### [Deploying Django with Docker Compose](https://www.youtube.com/watch?v=mScd-Pc_pX0)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube.com/embed/mScd-Pc_pX0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [The Level Up Hour (E35): Podman v3 and docker-compose](https://www.youtube.com/watch?v=Eahh-ZxiU4U)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube.com/embed/Eahh-ZxiU4U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [DjangoCon 2018 - Protecting Personal Data with Django (because it's the law)](https://www.youtube.com/watch?v=b6KEoNVKFxM)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube.com/embed/b6KEoNVKFxM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
