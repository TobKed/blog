Title: Month summary - June 2023
Date: 2023-06-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2023
Slug: 2023-june-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2023/2023_06_xx.jpg
Status: published

# June 2023

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

Over the past month, I have been working on a highly scalable app on the Google Cloud Platform.
I used Cloud Run and Cloud SQL (PostgreSQL) to provision the application code and database, respectively.

Cloud Run is a serverless compute platform that allows me to run my code without having to worry about managing servers.
Cloud SQL is a managed database service that provides a reliable and scalable database for my app.

I also used PubSub messaging to decouple APIs that need to be very fast from more time-consuming processes.
PubSub is a messaging service that allows me to send and receive messages between different parts of my app.
This decoupling allows me to scale my app more easily, as I can add or remove background worker instances without affecting the performance of the APIs.

Finally, I used a load balancer to expose my app to consumers.
A load balancer distributes traffic across multiple instances of my app, which helps to improve performance and reliability.
The load balancer also allows me to redirect country-specific load to the instances closest to the users, which improves the user experience.

It is very rewarding when you see that an app scales well and handles traffic peaks without impacting latency.

## Articles

### [A few words on communication](https://event-driven.io/en/a_few_words_on_communication/)

> It’s clear that even if we don’t want to talk to humans, we need to do it, which won’t change whether we like that.

### [Slack System Design](https://systemdesign.one/slack-architecture/)

> The key takeaway from building Slack is that optimality is contingent and should be adapted with growth.
> It is crucial to identify the end-to-end part of the problem to build a distributed system.

### [Unleashing Engineering Excellence: Proven Methods to Tackle Tech Debt and Supercharge Your Engineering Team](https://betterprogramming.pub/unleashing-engineering-excellence-proven-methods-to-tackle-tech-debt-and-supercharge-your-team-21463cdca19f)

> A head of engineering’s guide to conquering tech debt and empowering engineering excellence.

### [DevOps is Bullshit](https://blog.massdriver.cloud/posts/devops-is-bullshit/)

> A Critique of How We've Fooled Ourselves for Years.

### [Google Cloud blog: The Modernization Imperative: Shifting left is for suckers. Shift down instead](https://cloud.google.com/blog/products/application-development/richard-seroter-on-shifting-down-vs-shifting-left)

> As an industry, we need to help out. First, instead of telling devs (and their managers!) to shift everything left, we need to encourage them to “shift down” by taking full advantage of the technology available to them, and push more workloads down onto the platforms they’re already using.

## Productivity

### [Harvard Business Review: Remote Work Should Be (Mostly) Asynchronous](https://hbr.org/2021/12/remote-work-should-be-mostly-asynchronous)

> A move to a better way of working remotely is desperately needed.
> If your digital transformation is going to be successful, you need to give your employees the right tools and systems to work in a digital, distributed, virtual environment.

### [Awesome Quantified Self](https://github.com/woop/awesome-quantified-self)

> The [Quantified Self](https://en.wikipedia.org/wiki/Quantified_Self) is a movement to incorporate technology into data acquisition on aspects of a person's daily life in terms of inputs (e.g. food consumed, quality of surrounding air), states (e.g. mood, arousal, blood oxygen levels), and performance (mental and physical).

## AI

### [Short Course ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

> This short course taught by Isa Fulford (OpenAI) and Andrew Ng (DeepLearning.AI) will describe how LLMs work, provide best practices for prompt engineering, and show how LLM APIs can be used in applications for a variety of tasks.

### [GPT Engineer](https://github.com/AntonOsika/gpt-engineer)

> Specify what you want it to build, the AI asks for clarification, and then builds it.

## Python

### [The Many Problems with Celery](https://steve.dignam.xyz/2023/05/20/many-problems-with-celery/)

> Celery is the de facto solution for background workers and cron jobs in the Python ecosystem, but it’s full of footguns.

### [Makefile tricks for Python projects](https://ricardoanderegg.com/posts/makefile-python-project-tricks/)

> I like using Makefiles.
> They work great both as simple task runners as well as build systems for medium-size projects.
> This is my starter template for Python projects.

### [The Right Way to Run Shell Commands From Python](https://martinheinz.dev/blog/98)

> In this article we will look at all the options you have in Python for running other processes - the bad; the good; and most importantly, the right way to do it.

### [Interacting with Kubernetes Deployments and Services using Python SDK](https://www.faizanbashir.me/interacting-with-kubernetes-deployments-and-services-using-python-sdk)

> This article will demonstrate how to interact with Kubernetes Deployments and Services using Python and the official Kubernetes Python client.

### [AsyncIO: Why I Hate It](https://charlesleifer.com/blog/asyncio/)

> I hope it will encourage some readers (especially in the web development crowd) to question whether asyncio is appropriate for their project, and if so, look into alternatives like [gevent](http://www.gevent.org/).

### [ Pro-Tip – pytest fixtures are magic!](https://www.revsys.com/tidbits/pytest-fixtures-are-magic/)

> The more of our codebase that is covered by meaningful tests the faster we can develop new features and refactor cruft.
> It is not just about bug-free code.
> It's about the speed at which you can develop good code.

## Python libraries

### [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)

> Opinionated list of best practices and conventions we used at our startup.

### [JSON to Pydantic Converter](https://jsontopydantic.com/)

> To generate a Pydantic model from a JSON object, enter it into the JSON editor and watch a Pydantic model automagically appear in the Pydantic editor.

## Go

### [Google Cloud Platform Go Samples](https://github.com/GoogleCloudPlatform/golang-samples)

> This repository holds sample code written in Go that demonstrates the Google Cloud Platform.

## Tools

### [HariSekhon/SQL-scripts](git.io/SQL)

> 100+ SQL Scripts - PostgreSQL, MySQL, Google BigQuery, MariaDB, AWS Athena. DevOps / DBA / Analytics / performance engineering. Google BigQuery ML machine learning classification.

### [HariSekhon/DevOps-Bash-tools](https://github.com/HariSekhon/DevOps-Bash-tools)

> 1000+ DevOps Bash Scripts - AWS, GCP, Kubernetes, Docker, CI/CD, APIs, SQL, PostgreSQL, MySQL, Hive, Impala, Kafka, Hadoop, Jenkins, GitHub, GitLab, BitBucket, Azure DevOps, TeamCity, Spotify, MP3, LDAP, Code/Build Linting, pkg mgmt for Linux, Mac, Python, Perl, Ruby, NodeJS, Golang, Advanced dotfiles: .bashrc, .vimrc, .gitconfig, .screenrc, tmux..

### [The C4 model for visualising software architecture](https://c4model.com/)

> Context, Containers, Components, and Code

## Cloud

### [GitOps](https://www.gitops.tech/)

> This site aggregates the essence of GitOps to help clear up the confusion about the topic.

### [Argo CD - Declarative Continuous Delivery for Kubernetes](https://github.com/argoproj/argo-cd)

> Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.

### ["Sealed Secrets" for Kubernetes](https://github.com/bitnami-labs/sealed-secrets)

> **Problem**: "I can manage all my K8s config in git, except Secrets."
>
> **Solution**: Encrypt your Secret into a SealedSecret, which is safe to store - even inside a public repository. The SealedSecret can be decrypted only by the controller running in the target cluster and nobody else (not even the original author) is able to obtain the original Secret from the SealedSecret.

### [k3s](https://github.com/k3s-io/k3s/)

> Lightweight Kubernetes. Production ready, easy to install, half the memory, all in a binary less than 100 MB.

### [pydevops/gcloud-cheat-sheet.md](https://gist.github.com/pydevops/cffbd3c694d599c6ca18342d3625af97)

> gcp gcloud cheat sheet

## Other stuff

### [Torrent 🧲 Parts](https://github.com/leoherzog/TorrentParts)

> A website to inspect and edit what's in your Torrent file or Magnet link.

## Podcasts

### [The Privacy, Security, & OSINT Show – Episode 299 - Self-Hosted Part I](https://inteltechniques.com/blog/2023/06/02/the-privacy-security-osint-show-episode-299/)

> This week I begin the conversation about self-hosting everything, plus offer the latest privacy news.

### [The Privacy, Security, & OSINT Show – Episode 300 - Self-Hosted 2: Offline Knowledge](https://inteltechniques.com/blog/2023/06/16/the-privacy-security-osint-show-episode-300/)

> This week I continue the self-hosted series with several easy options from which anyone can benefit. Let's archive some powerful data for offline use.

## Videos

### [PyCon US 2023](https://www.youtube.com/playlist?list=PL2Uw4_HvXqvY2zhJ9AMUa_Z6dtMGF3gtb)

> PyCon US 2023 YouTube Playlist

### [Wykorzystanie Chmur Publicznych w instytucji finansowej | Devagacje](https://www.youtube.com/watch?v=u8uJzGhPKIg)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/u8uJzGhPKIg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Single-node Kubernetes Clusters Using K3s with Benefits of GitOps • Lasse Højgaard • GOTO 2021](https://www.youtube.com/watch?v=ePyFJ7Hd57Q)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/ePyFJ7Hd57Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Rockstar Developers Are THE WORST Developers](https://www.youtube.com/watch?v=mVY2rFninp8)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/mVY2rFninp8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Deviant: Elevator Hacking: From the Pit to the Penthouse](https://www.youtube.com/watch?v=ZUvGfuLlZus)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/ZUvGfuLlZus" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Top 5 techniques for building the worst microservice system ever - William Brander - NDC London 2023](https://www.youtube.com/watch?v=88_LUw1Wwe4)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/88_LUw1Wwe4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
