Title: Month summary - September 2024
Date: 2024-09-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2024
Slug: 2024-september-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2024/2024_09_xx.jpg
Status: draft

# September 2024

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

This month I delved deep into the world of [GitHub Actions](https://github.com/features/actions), a tool that I've grown to love and become an expert in.
Previously I've not only worked extensively with GitHub Actions but also created my own custom actions, such as the [GitHub Forks Sync Action](https://github.com/TobKed/github-forks-sync-action) and the [Label When Approved Action](https://github.com/TobKed/label-when-approved-action).

In addition to this I utilized GitHub Actions for scraping data related to GitHub Actions for the Apache Software Foundation.
This allowed me to calculate valuable statistics.
My dedication to mastering GitHub Actions led me to pass a certification exam with minimal preparation, earning the badge of a certified GitHub Actions expert, which I proudly display [here](https://www.credly.com/badges/6b96a6c9-28cb-47dd-9dfa-13dd7a37d543).

<a target="\_blank" rel="noopener noreferrer" href="https://www.credly.com/badges/6b96a6c9-28cb-47dd-9dfa-13dd7a37d543">
    <img src="{static}/images/posts/2024/2024_09_github_actions.png" alt="GitHub Actions Certification" style="display: block; margin-left: auto; margin-right: auto;">
</a>

Me a while back, full of hair and excitement, giving a presentation on GitHub Actions:

<img src="{static}/images/posts/2022/2022_10_brival.jpg" alt="Brival Tech Talk - tips & tricks" style="display: block; margin-left: auto; margin-right: auto;">

After achieving this milestone, I decided to channel my expertise into a personal project.
One weekend evening I finally created a photoblog using [Hugo](https://gohugo.io/) and GitHub Actions.
To maintain the privacy of the original-size photos and their metadata I kept the source code in a private repository.
With the help of a GitHub Actions workflow, a static website was generated using **Hugo** and pushed to a public repository, where my photoblog is now available for viewing at [photos.tobked.dev](https://photos.tobked.dev).

`gh-pages.yaml`

```yaml
name: github pages

on:
  push:
    branches:
      - master
  pull_request:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@75d2e84710de30f6ff7268e08f310b60ef14033f  # v3
        with:
          hugo-version: '0.134.3'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Setup Exiftool
        uses: woss/exiftool-action@f592e36cc8d653b8f8ac3084b34403d0911236a3  # v12.87

      - name: Remove Exif data from images
        run: exiftool -r -all= -ext jpg -ext jpeg -ext png -ext webp -overwrite_original public

      - name: Deploy
        uses: peaceiris/actions-gh-pages@4f9cc6602d3f66b9c108549d475ec49e8ef4d45e  # v4
        if: github.ref == 'refs/heads/master'
        with:
          deploy_key: ${{ secrets.ACTIONS_PHOTOS_DEPLOY_KEY }}
          external_repository: TobKed/photos
          publish_dir: ./public
          cname: photos.tobked.dev
```

In addition to my GitHub Actions adventures, I also dived into learning tmux, a tool that brought me a lot of joy.
I customized a configuration file to tailor the tmux experience to my liking, enabling features like mouse support and setting new panes to open in the current directory.

`.tmux.conf`

```shell
set -g mouse on
setw -g mode-keys vi

# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

set -g @continuum-restore 'on'

# Set new panes to open in current directory
bind c new-window -c "#{pane_current_path}"
bind '"' split-window -c "#{pane_current_path}"
bind % split-window -h -c "#{pane_current_path}"
```

I'm excited to share some interesting materials I've gone through. Check them out below.

## Articles

### [High Growth Engineer: My Tech Promotion Algorithm](https://read.highgrowthengineer.com/p/my-tech-promotion-algorithm)

> Guest post by ex-Amazon Principal Engineer, Steve Huynh.

### [Architecture Weekly: Using S3 but not the way you expected. S3 as strongly consistent event store](https://www.architecture-weekly.com/p/using-s3-but-not-the-way-you-expected)

> [Amazon S3 now supports conditional writes](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes).

### [I will f(l)ail at your tech interviews, here's why you should care](https://fraklopez.com/noodlings/2024-08-25-i-will-fail-your-technicals/)

> In this post, I will attempt to break down my perspective on technical interviews (techs).
> What I see to be their real value and application.
> By the end of this, I hope you will know why as a Hiring Manager I’ve pushed back on using them and what I prefer to do instead.

### [Using your own product is a superpower](https://newsletter.posthog.com/p/using-your-own-product-is-a-superpower)

> Why you should dogfood your product and how we do it at PostHog

### [I just crossed $1 million on GitHub Sponsors. 💰🎉](https://calebporzio.com/i-just-cracked-1-million-on-github-sponsors-heres-my-playbook)

> Want some tangible strategy? Do you too want to make a million bucks in open source? It's easy! 🙄 Let's dive in

### [Your company needs Junior devs ](https://softwaredoug.com/blog/2024/09/07/your-team-needs-juniors)

> Getting coffee with a bunch of local tech leaders, I surprised myself with how stridently I argued why companies should hire junior engineers.

### [I've Built My First Successful Side Project, and I Hate It](https://switowski.com/blog/i-have-built-my-first-successful-side-project-and-i-hate-it/)

> In 2020, I built my first side project.
> I scratched my own itch, then started selling it, and since then, the project has earned me over $15,000.
> But a few months after releasing it, I was so tired of the maintenance that I wanted to shut it down.
> Here is a story about my short entrepreneurial adventure.

### [Advice From a Software Engineer With 8 Years of Experience](https://betterprogramming.pub/advices-from-a-software-engineer-with-8-years-of-experience-8df5111d4d55)

> Practical tips for those who want to advance in their careers

### [The Most Heated Tech Job Market in History: Advice for Software Engineers](https://blog.pragmaticengineer.com/advice-for-tech-workers-to-navigate-a-heated-job-market/)

> This piece covers advice for tech workers to make the most out of this heated market: whether you want to make a job change or not.
> A market where demand for employees outstrips supply is one where employees can do well for themselves with less-than-usual effort.

### [7 Must-Know Lessons To Be A Better Engineer From Top Industry Leaders](https://read.highgrowthengineer.com/p/month-of-collabs-recap-2024)

> 2024 Month of Collabs: Best lessons to take your career forward

### [Why Not Comments](https://buttondown.com/hillelwayne/archive/why-not-comments/)

> Why not "why not" comments? Not why "not comments"

### [Release fatigue 😫 and going static](https://levit.be/blog/release-fatigue.html)

> By virtue of being statically generated, the code for our website doesn't need to be kept up-to-date with the latest security release of every package and tool we use, it's just HTML!

### [Why Scrum is Stressing You Out](https://rethinkingsoftware.substack.com/p/why-scrum-is-stressing-you-out)

> Back then, things would get crazy around deadlines, but at other times, I recall feeling pretty even. These days, however, the pressure seems omnipresent.

### [Makefiles for Web Work](https://rosszurowski.com/log/2022/makefiles)

> `make` is a build tool that’s been around since the 1970s. It was originally designed for automating the building of C programs: installing dependencies, running tests, and compiling binaries.

### [The Art of War Applied To Software Development](https://www.toptal.com/agile/art-of-war-software-development)

> In this post, Toptal Freelance Software Engineer Jose F. Maldonado explains why many of these ancient teachings still matter, and what you can do to make them work for you and your team.

### [A Life Engineered: The #1 Mistake You're Making with Your Mentor (And How You Can Avoid It)](https://alifeengineered.substack.com/p/the-1-mistake-youre-making-with-your)

> Tips and resources on how to make the most out of your mentorship.

### [Using Bloom’s Taxonomy to Write Effective Learning Outcomes](https://tips.uark.edu/using-blooms-taxonomy/)

> Bloom’s Taxonomy is a classification of the different objectives and skills that educators set for their students (learning outcomes).

## Productivity

### [Good software development habits](https://zarar.dev/good-software-development-habits/)

> This post is not advice, it's what's working for me.

### [How to understand/retain complex concepts 10x better](https://learnhowtolearn.org/how-to-understand-and-retain-any-concept-10x-better/)

> The whole idea: compress the concept by repeatedly practicing explaining it until you understand it from first principles.

## AI

### [danielmiessler/fabric](https://github.com/danielmiessler/fabric)

> fabric is an open-source framework for augmenting humans using AI.
> It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere.

### [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)

> real time face swap and one-click video deepfake with only a single image

### [DataLine](https://dataline.app/)

> DataLine is an AI-driven open source and privacy-first platform for data exploration.
> Your data is accessed using your device and stored on your device.
> No clouds, only sunshine.

### [How to Get Samantha from Her or TARS from Interstellar on Your iPhone/Android](https://danielmiessler.com/p/get-samantha-tars-interstellar-iphoneandroid)

> Change your AI from Siri to an interactive and realistic AI from Her or Interstellar that you can have long conversations with.

### [MacGPT](https://www.macgpt.com/)

> ChatGPT on your Mac and Menubar.

### [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper)

> Quickly and easily transcribe audio files into text with OpenAI's state-of-the-art transcription technology Whisper.

## Security

### [Hacking misconfigured AWS S3 buckets: A complete guide](https://blog.intigriti.com/hacking-tools/hacking-misconfigured-aws-s3-buckets-a-complete-guide)

> You've probably already come across an AWS S3 bucket, maybe even a misconfigured one too, and if you ignored them before, we hope this article shines some light on the most common security misconfigurations present in this storage bucket service.

### [Fake recruiter coding tests target devs with malicious Python packages](https://www.reversinglabs.com/blog/fake-recruiter-coding-tests-target-devs-with-malicious-python-packages)

> RL found the VMConnect campaign continuing with malicious actors posing as recruiters, using packages and the names of financial firms to lure developers.

## Python

### [Why I Still Use Python Virtual Environments in Docker](https://hynek.me/articles/docker-virtualenv/)

> As an overarching theme, my goal is not to mindlessly follow some ~best practices~ that add complexity for questionable payoffs because a big tech developer advocate said so at a conference.
> But I spend a lot of time thinking about the secondary effects of what I do.

### [SuperFastPython!: Asyncio gather() Limit Concurrency](https://superfastpython.com/asyncio-gather-limit-concurrency/)

> We can limit concurrency when using asyncio.gather() via a semaphore.
>
> In this tutorial, you will discover how to limit concurrency with asyncio.gather().

### [How to Build a Perfect Docker Image for a Poetry Project](https://codemageddon.me/post/poetry-docker/)

> This article describes how to build a perfect Docker image for your Poetry-based project

### [Docker images using uv's python](https://mkennedy.codes/posts/python-docker-images-using-uv-s-new-python-features/)

> uv has changed the landscape

## Django

### [This post is part of Create A One-Product Shop With Django, Htmx, and Stripe Series](https://blog.appsignal.com/2024/08/28/build-a-one-product-shop-with-the-python-django-framework-and-htmx.html)

> This is the first of a two-part series using Django, htmx, and Stripe to create a one-product e-commerce website.
> In this part, we'll start our Django project and integrate it with htmx.

### [Django-allauth: Site Matching Query Does Not Exist](https://learndjango.com/tutorials/django-allauth-site-matching-query-does-not-exist)

> The issue is that the [quickstart guide](https://docs.allauth.org/en/latest/installation/quickstart.html) leaves ou pullt a critical piece of configuration: setting a `SITE_ID` in the `settings.py file`.

### [Custom Error Messages on Model Deletion in the Django Admin](https://startcodingnow.com/custom-django-admin-messages)

> I have been working on a project where we might want to delete models even just for testing purposes, but we don't want to accidentally delete models.

### [Django: hoist repeated decorator definitions](https://adamj.eu/tech/2024/09/08/django-repeated-decorators/)

> Django provides us with a rich set of view decorators.
> In this post, we’ll look at a technique for hoisting repeated use of these decorators to reduce repetition.

## Python libraries

### [cbfa](https://github.com/pomponchik/cbfa)

> Class-based views for the FastAPI

### [humanize](https://github.com/python-humanize/humanize)

> This modest package contains various common humanization utilities, like turning a number into a fuzzy human-readable duration ("3 minutes ago") or into a human-readable size or throughputs

## Django libraries

### [radiac/nanodjango](https://github.com/radiac/nanodjango)

> Full Django in a single file - views, models, API ,with async support. Automatically convert it to a full project.

## Tools

### [pigsty](https://github.com/Vonng/pigsty)

> Battery-Included, Local-First PostgreSQL Distribution as a Free & Better RDS Alternative!
>
> ```
> "PostgreSQL In Great STYle": Postgres, Infras, Graphics, Service, Toolbox, it's all Yours.
> ```

### [C4 model](https://c4model.com/)

> The C4 model for visualising software architecture

### [Exiftool Github action](https://github.com/woss/exiftool-action)

> Action for Exiftool. Include it in the path without installing, run multiple versions

## Cloud

### [Technical Guide: End-to-End CI/CD DevOps with Jenkins, Terraform, Docker, Kubernetes, SonarQube, ArgoCD, AWS EC2, EKS, and GitHub Actions (Django Deployment)](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e)

> Building an end-to-end CI/CD pipeline for Django applications using Jenkins, Docker, Kubernetes, EKS, ArgoCD, GitHub Actions, AWS EC2, and Terraform can be quite a robust setup. In this article, we will guide you through setting up a comprehensive CI/CD pipeline using AWS EC2, AWS EKS, Jenkins, Github actions, Docker, trivy scan, SonarQube, ArgoCD, Kubernetes cluster of your choice, and terraform.

### [Architecture Weekly: Show me the money! Practically navigating the Cloud Costs Complexity](https://www.architecture-weekly.com/p/show-me-the-money-practically-navigating?publication_id=579466&post_id=148674128&isFreemail=true&r=1rko2t&triedRedirect=true)

> Today, we’ll grab a calculator to discuss the costs of building an event store on S3.

### [Announcing IAM group authentication in Cloud SQL](https://cloud.google.com/blog/products/databases/announcing-iam-group-authentication-in-cloud-sql)

> IAM group authentication extends existing IAM database authentication functionality by allowing database access to be managed at the group level instead of the individual user level.

### [Stevey's Google Platforms Rant](https://gist.github.com/chitchcock/1281611)

> Yegge wrote this in 2011 and posted it on Google+. He intended to make it visible internally to Google only, but accidentally made it public.

### [What are the main Cloud Design Patterns?](https://newsletter.techworld-with-milan.com/p/what-are-the-main-cloud-design-patterns)

> and how they help fighting with fallacies of Distributed Computing

## Other stuff

### [The 512KB Club](https://512kb.club/)

> The 512KB Club is a collection of performance-focused web pages from across the Internet.

## Videos

### [Zasypiaj z poczuciem, że to był dobry dzień. Startujemy Productivity by Heart! 💚](https://www.youtube.com/watch?v=cKcGG3JakZQ)

> Playback on other websites has been disabled by the video owner. [Watch on YouTube](https://www.youtube.com/watch?v=cKcGG3JakZQ)

### [How to Negotiate a Big Tech Offer as a Software Engineer - with ‪@RahulPandeyrkp‬](https://www.youtube.com/watch?v=cbngWLr7BC4)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/cbngWLr7BC4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Fireship: Tmux in 100 Seconds](https://www.youtube.com/watch?v=vtB1J_zCv8I)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/vtB1J_zCv8I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [NetworkChuck: you need to learn tmux RIGHT NOW!!](https://www.youtube.com/watch?v=nTqu6w2wc68)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/nTqu6w2wc68" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [NetworkChuck: 18 Weird and Wonderful ways I use Docker](https://www.youtube.com/watch?v=RUqGlWr5LBA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/RUqGlWr5LBA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [NetworkChuck:  You've been using AI Wrong ](https://www.youtube.com/watch?v=UbDyjIIGaxQ)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/UbDyjIIGaxQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [DjangoCon US: Django & Celery - A love story of async proportions - Hugo Bessa](https://www.youtube.com/watch?v=2GhZWzeipWA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/2GhZWzeipWA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Unsupervised Learning: Introducing Fabric — A Human AI Augmentation Framework](https://www.youtube.com/watch?v=wPEyyigh10g)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/wPEyyigh10g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
