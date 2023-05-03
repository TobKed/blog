Title: Month summary - April 2023
Date: 2023-04-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2023
Slug: 2023-april-links
Summary: Interesting stuff from the month
Status: published
Header_Cover: /images/posts/2023/2023_05_gcp_dev_day/2023_05_gcp_dev_day.jpg

# April 2023

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

#### `git rebase --interactive` and `fixups`

I have seen how different people use Git, and each person has their own way of using it.
However, I did not see many people using git `rebase interactive` and `fixups`.
For a long time, I have been thinking about presenting how I use `git rebase`, `git rebase interactive`, and my beloved `fixups`.
A long time ago, I wrote a short blog post about it ([Changing history in Git]({filename}/posts/2019_08_12_git_change_history.md)), but I felt it was not enough.
I wanted to show it in action and explain why I do it.
Because of that, I decided to prepare a presentation about it.
I presented it during one of the internal meetings at work, and I think it went well.
I am planning to present it during one of the meetups in the future.

I was a little bit frustrated with Google Slides and how it handles code snippets.
I decided to keep the text of the presentation in the repository, so it is easier to track changes, publish and share it.
Inspired by [Raymond Hettinger](https://www.youtube.com/playlist?list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA) I decided to use the documentation generator [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
The presentation is available as a website under my domain: [tobked.dev/git_rebase_interactive](https://tobked.dev/git_rebase_interactive).
Its source is on my Github: [github.com/TobKed/git_rebase_interactive](https://github.com/TobKed/git_rebase_interactive).

#### [Google Cloud Developer Day Warsaw 2023]({filename}/posts/2023_05_03_gcp_dev_day.md)

I attended Google Cloud Developer Day Warsaw 2023 on April 27th, 2023. It was a free event organized by Google Cloud at their [Warsaw Campus](https://www.campus.co/warsaw/).
I wrote more about it in a separate blog post: [Google Cloud Developer Day Warsaw 2023]({filename}/posts/2023_05_03_gcp_dev_day.md).

______________________________________________________________________

## Articles

### [How to Make a Great Conference Talk](https://switowski.com/blog/how-to-make-a-great-conference-talk/)

> I have decided to write this guide to assist my readers who aspire to be conference speakers.
> I hope it will help you prepare for your first presentation or improve your talks further.

### [CAN Injection: keyless car theft](https://kentindell.github.io/2023/04/03/can-injection/)

> This is a detective story about how a car was stolen - and how it uncovered an epidemic of high-tech car theft.

### [Programista – pytania rekrutacyjne – bazy danych](https://devszczepaniak.pl/programista-pytania-rekrutacyjne-bazy-danych/)

> Tematem tego wpisu są bazy danych.
> Z uwagi na ich popularność, głównym tematem wpisu będą relacyjne bazy danych i zagadnienia z nimi związane.

### [Saving Energy: Home Server That Automatically Suspends to RAM and Wakes Up Again which is used for Plex media streaming and Time Machine backups.](https://maximiliangolla.com/blog/2022-10-wol-plex-server/)

> It does not sound like much, but running a 24/7 home server that draws 43 watts in idle is quiet expensive, considering the latest electricity prices of about 49 euro cent/kWh here in Germany (as of October, 2022).
> A simple solution to this problem is a script that automatically suspends the server, when it is not used, and another script to wake the server up again, in case there is work to do.
> To my surprise I could not find any out-of-the-box solution, so I thought, it is a worthwhile effort to write about it.

### [69 Ways to F\*\*\* Up Your Deploy](https://kellyshortridge.com/blog/posts/69-ways-to-mess-up-your-deploy/)

> We hear about all the ways to make your deploys so glorious that your pipelines poop rainbows and services saunter off into the sunset together.
> But what we don’t see as much is folklore of how to make your deploys suffer.

### [I failed 3 job applications, here's what I learned](https://blog.alexewerlof.com/p/3-job-applications)

> Tips and mistakes to avoid when applying software engineering jobs at top tech.

### [TikTok is a Time Bomb](https://gurwinder.substack.com/p/tiktok-may-be-a-chinese-bio-weapon)

> The ultimate weapon of mass distraction

### [Bicycle by Bartosz Ciechanowski](https://ciechanow.ski/bicycle/)

> In this article, I’ll focus on the delicate interplay between many of the forces that act on a bicycle and its parts when riding.
> We’ll witness how forces applied through tires make a bicycle accelerate, brake, and turn, and we’ll also investigate how the wheels and the frame handle those different forces without breaking.

### [Zmiana pracy w IT – kiedy warto się na to zdecydować?](https://programistanaswoim.pl/zmiana-pracy-w-it-kiedy-warto-sie-na-to-zdecydowac/)

> Czy to czas, żeby zmienić coś w swoim życiu, czy lepiej zostać w obecnej firmie i poczekać na bardziej sprzyjający moment?

## Productivity

### [The age of Agile must end](https://uxdesign.cc/the-age-of-agile-must-end-bc89c0f084b7)

> 30 years ago the technology industry attempted to import Lean practices — it failed.
> Instead of “continuous improvement,” progress halted.
> Agile is incompatible with UX research, design, and scalable development.
> It always will be. It’s time to create a new operational standard.

## AI

### [March 20 ChatGPT outage: Here’s what happened](https://openai.com/blog/march-20-chatgpt-outage)

> An update on our findings, the actions we’ve taken, and technical details of the bug.

### [librarian-ai.com/](https://www.librarian-ai.com/)

> Discover your next favorite book effortlessly with the help of AI.

### [🧠 Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)

> This is a collection of prompt examples to be used with the ChatGPT model.

### [AI Incident Database](https://incidentdatabase.ai/)

> The AI Incident Database is dedicated to indexing the collective history of harms or near harms realized in the real world by the deployment of artificial intelligence systems.

### [TED: Greg Brockman - The inside story of ChatGPT's astonishing potential](https://www.ted.com/talks/greg_brockman_the_inside_story_of_chatgpt_s_astonishing_potential/)

> In a talk from the cutting edge of technology, OpenAI cofounder Greg Brockman explores the underlying design principles of ChatGPT and demos some mind-blowing, unreleased plug-ins for the chatbot that sent shockwaves across the world.

### [regex.ai](https://regex.ai/)

> AI-Powered Regular Expression Solver

## Security

### [Sekurat: Jak narzędzia AI zmieniają OSINT \[Czwartki z OSINTem\]](https://sekurak.pl/jak-narzedzia-ai-zmieniaja-osint-czwartki-z-osintem/)

> Powstaje bowiem pytanie, czy ChatGPT, a także narzędzia generujące bardzo realistyczne obrazy, jak Midjourney czy DALL-E, zmienią sposób, w jaki prowadzone są działania OSINT-owe.

## Python

### [Python Monorepo: an Example. Part 1: Structure and Tooling](https://www.tweag.io/blog/2023-04-04-python-monorepo-1/)

> For a software team to be successful, you need excellent communication.
> That is why we want to build systems that foster cross-team communication.
> Using a monorepo is an excellent way to do that

### [syntactic sugar blog posts by Tall, Snarky Canadian (Brett Cannon)](https://snarky.ca/tag/syntactic-sugar/)

> "In computer science, syntactic sugar is syntax within a programming language that is designed to make things easier to read or to express.
> It makes the language "sweeter" for human use: things can be expressed more clearly, more concisely, or in an alternative style that some may prefer."
> -- https://en.wikipedia.org/wiki/Syntactic_sugar

### [The different uses of Python type hints](https://lukeplant.me.uk/blog/posts/the-different-uses-of-python-type-hints/)

> There isn’t really a point of this post other than to say “be aware of these different use cases”.
> This awareness can be very important when you are in any discussion about the usefulness or necessity of type hints — which scenarios are you thinking about?

### [A Gentle Introduction to the Python Match Statement](https://www.wrighters.io/intro-to-python-match-statement/)

> When new features are added to Python, sometimes it can take a while to learn about and start using the feature. For me, the Python match statement (a.k.a. structural pattern matching) is a good example.
> Some features are very easy to grasp and use (for example, f-strings), but structural pattern matching is a bit more complex.

### [5 Common Asyncio Errors in Python (and how to avoid them)](https://superfastpython.com/asyncio-common-errors/)

> In this tutorial, you will discover the most common errors encountered by beginners in asyncio in Python.

### [ Google: Assured Open Source Software - List of supported Java and Python packages](https://cloud.google.com/assured-open-source-software/docs/supported-packages#python)

> Help reduce the risk to your software supply chain by using the same OSS packages that Google uses and secures in your own developer workflows.

### [authentik on Django: 500% slower to run but 200% faster to build](https://goauthentik.io/blog/2023-03-16-authentik-on-django-500-slower-to-run-but-200-faster-to-build)

> With the arrival of funding and the requirement to build a business that could sustain itself now and scale as the company evolved,
> I had to confront some of the technical choices I made when building authentik – in particular, the choice to build authentik using Python and Django.

### [Dependency Injection in Python](https://itnext.io/dependency-injection-in-python-a1e56ab8bdd0)

> Building flexible and testable architectures in Python

## Django

### [Django Performance Optimization Tips](https://testdriven.io/blog/django-performance-optimization-tips/)

> This article addresses different aspects of Django performance and showcases some of the practices you can use to speed up your app.
> On top of that, it provides links to additional resources for further reading.

### [Ban 1+N in Django](https://suor.github.io/blog/2023/03/26/ban-1-plus-n-in-django/)

> I always thought of 1+N as a thing that you just keep in your head, catch on code reviews or via performance regressions.
> This worked well for a long time, however, the less control we have over our SQL queries the more likely it will sneak through those guards.

### [Building an Intelligent Education Platform with OpenAI, ChatGPT, and Django](https://testdriven.io/blog/python-openai-chatgpt/)

> In this tutorial, you'll learn how artificial intelligence (AI) can empower us to create educational platforms that are smarter, more personalized,
> and more effective than ever by leveraging the latest advancements in AI technology such as GPT-3 and ChatGPT.

### [Python/Django AsyncIO Tutorial with Examples ](https://djangostars.com/blog/asynchronous-programming-in-python-asyncio/)

> If for some reason you or your team of Python developers have decided to discover the asynchronous part of Python, welcome to our quick tutorial on using Async IO in Python/Django.

### [Running Tasks Concurrently in Django Asynchronous Views ](https://fly.io/blog/running-tasks-concurrently-in-django-asynchronous-views/)

> Mariusz Felisiak, a Django and Python contributor and a Django Fellow, explores how to use recent async improvements in Django to run multiple async tasks in an asynchronous view!

### [How to have Python show warnings when running Django](https://www.untangled.dev/2023/04/26/py-django-warnings/)

> I usually look for deprecation warnings when I see a newer Django version being prepared for release.

## Tools

### [git-sim](https://github.com/initialcommit-com/git-sim)

> Visually simulate Git operations in your own repos with a single terminal command.

## Cloud

### [Why I think GCP is better than AWS](https://nandovillalba.medium.com/why-i-think-gcp-is-better-than-aws-ea78f9975bda)

> AWS is the best platform to showcase how great GCP is…

### [Cloud Functions Best Practices (3/4) : Secure the Cloud Functions](https://medium.com/google-cloud/cloud-functions-best-practice-3-4-secure-the-cloud-functions-1c9642c4706)

> Protect your Function perfectly.

### [Best practices and a tutorial for using Google Cloud Functions with MongoDB Atlas](https://cloud.google.com/blog/products/databases/best-practices-and-tutorial-using-google-cloud-functions-mongodb-atlas)

> Connect your serverless functionality to your third-party databases for efficient and cost-effective cloud applications.

### [Hosting successful live events with Google Cloud](https://cloud.google.com/blog/products/networking/hosting-successful-live-events-with-google-cloud)

> Hosting a live event requires a significant level of planning and preparedness.
> At Google Cloud, we've supported customers that delivered live tentpole events at planet scale, most recently, football matches for FIFA World Cup 2022 using Media CDN for worldwide distribution.

### [Promoting pre-prod to production in Cloud Run with Google Cloud Deploy](https://cloud.google.com/blog/products/devops-sre/using-cloud-deploy-to-promote-pre-prod-to-production-in-cloud-run)

> Deploying your first container to Cloud Run is famously intuitive.
> The magic of typing gcloud run deploy and watching your container run never really gets old for me.

### [How to identify and reduce costs of your Google Cloud observability in Cloud Monitoring](https://cloud.google.com/blog/products/management-tools/learn-to-understand-and-reduce-cloud-monitoring-costs)

> If it matters, you should measure it! This adage underpins an explosion of growth in the monitoring and observability market over the last decade.
> Unfortunately, many organizations struggle to realize the benefits of their tooling, leading to budget bloat without gaining much additional insight.

### [Klaster K8s na Raspberry Pi, czyli K3s na nowo](https://kaluzny.io/klaster-k8s-na-raspberry-pi-czyli-k3s-na-nowo/)

> Mój domowy klaster K8s na Raspberry Pi

### [Defining Labelling strategy in GCP for gaining granularity into cloud costs](https://medium.com/google-cloud/defining-labelling-strategy-in-gcp-for-gaining-granularity-into-cloud-costs-9110018d356b)

> Labels act as metadata which lets you filter resources in Cloud Billing console. It’s important to note that labels and tags hold different meanings in GCP, refer [this](https://cloud.google.com/resource-manager/docs/tags/tags-overview) to know more.

### [AwesomeGCP \[YouTube Channel\]](https://www.youtube.com/@AwesomeGCP)

> Preparation of GCP certifications

### [How I Keep Myself Up-to-Date on Google Cloud Platform: A Personal Journey](https://medium.com/google-cloud/how-i-keep-myself-up-to-date-on-google-cloud-platform-a-personal-journey-dc334f733c0f)

> As a GCP user, it’s important to stay up-to-date with the latest changes and advancements in the platform.

### [OWASP Kubernetes Top 10](https://sysdig.com/blog/top-owasp-kubernetes/)

> The OWASP Kubernetes Top 10 puts all possible risks in an order of overall commonality or probability.

### [CloudSkills/Terraform-Projects](https://github.com/CloudSkills/Terraform-Projects)

## Other stuff

### [KNOW YOUR HTTP * WELL](https://github.com/for-GET/know-your-http-well)

> HTTP encodings, headers, media types, methods, relations and status codes, all summarized and linking to their specification.

### [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

> Python is the main dynamic language used at Google. This style guide is a list of dos and don’ts for Python programs.

### [Awesome Software and Architectural Design Patterns](https://github.com/DovAmir/awesome-design-patterns)

> A curated list of software and architecture related design patterns.

### [IPTV](https://github.com/iptv-org/iptv#database)

> Collection of publicly available IPTV channels from all over the world.

### [America Against America (USA) - Wang Huning](https://ia601806.us.archive.org/12/items/america-against-america/America%20Against%20America.pdf)

> America critique.

## Podcasts

### [The Real Python Podcast Episode 150: Lessons Learned From Four Years Programming With Python](https://realpython.com/podcasts/rpp/150/)

> What are the core lessons you’ve learned along your Python development journey?
> What are key takeaways you would share with new users of the language?
> This week on the show, Duarte Oliveira e Carmo is here to discuss his recent talk, “Four Years of Python.”

## Videos

### [#FOSSBack: Wolfgang Gehring – A Vision of FOSS @MercedesBenz](https://www.youtube.com/watch?v=6uHJodpllpA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/6uHJodpllpA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [OMH 2021: Służby, wpadki i OSIntowe kwiatki - Kamil Goryń](https://www.youtube.com/watch?v=dlyIeJijh7E)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/dlyIeJijh7E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
