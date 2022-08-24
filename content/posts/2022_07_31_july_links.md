Title: Month summary - July 2022
Date: 2022-12-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2022
Slug: 2022-july-links
Summary: Interesting stuff from the month
Status: draft
Header_Cover: /images/posts/2022/2022_07_xx.jpg

# July 2022

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

My repository with [deployment Django on Google Cloud Platform \[GCP\]](https://github.com/TobKed/django_on_gcp)
was published in [PyCoders weekly #532](https://pycoders.com/issues/532)
and in [Django Newsletter #135](https://django-news.com/issues/135?#start).
How awesome is that! :)

I also added infra describe in Terraform for setting up Open ID Connect authorization for GitHub Actions and GCP
to my [repository](https://github.com/TobKed/github_actions_oidc) dedicated for this topic.

Talk [Making Badass Developers](https://www.youtube.com/watch?v=FKTxC9pl-WM)
and blog post [The Ferrari problem](https://vasilishynkarenka.com/the-ferrari-problem/)
makes me to realize that how important is to minimize impact of not important or less important things in our lifes.
We should not burn our llimited brain capacity to make some trivial choices like choosing t-shirt to wear today.
This is of course very trivial example but goes to the point of scarcity of computing power.
Apparently I already I got rid of t-shirt problem since 98% of my t-shirts are plain black -> no choice -> no problem.

## Articles

### [Why new Macs break your Docker build, and how to fix it](https://pythonspeed.com/articles/docker-build-problems-mac/)

> Tt can be a little confusing when you try to build your Python-based Dockerfile on a new Mac, and everything starts failing. What used to work before—on an older Mac, or on a Linux machine—fails in completely unexpected ways.

### [3 Design Patterns Every Developer Should Learn](https://blog.bitsrc.io/3-design-patterns-every-developer-should-learn-71a51568ac9d)

> Design patterns are high-level answers to problems that we as software engineers encounter frequently. It isn’t code — I repeat, IT IS NOT CODE. It’s akin to explaining how to approach these issues and come up with a solution.

### [Shipping to Production](https://blog.pragmaticengineer.com/shipping-to-production/)

> How you ship your code to production in a way that is fast and reliable, is a question more engineers and engineering leaders should educate themselves on. The teams and companies that can do both – ship quickly / frequently and with good quality – have a big advantage over competitors who struggle with either constraint.

### [10 Books Every Senior Engineer Should Read](https://semaphoreci.medium.com/10-books-every-senior-engineer-should-read-a61c1917e2a7)

> Engineers are natural readers. They take enormous pleasure in learning about new things, and books are the perfect medium to cover complex ideas in depth.

### [Monitoring tiny web services](https://jvns.ca/blog/2022/07/09/monitoring-small-web-services/)

> I’m not going to talk about how to monitor Big Serious Mission Critical websites at all, only tiny unimportant websites.

### [Morning thinking practice](https://vasilishynkarenka.com/morning-thinking/)

> A daily thinking practice that has made a tremendous impact on my life in the past 2.5y.
>
> - Vasili Shynkarenka

### [The Ferrari problem](https://vasilishynkarenka.com/the-ferrari-problem/)

> .Don’t push the pedal to the metal on problems that don’t matter.
>
> - Vasili Shynkarenka

### [Luke Smith: The hardest technical solutions are right in front of your face](https://lukesmith.xyz/articles/obvious-technical-solutions/)

> Since I was recently doing tutorials on Hugo, a static site generator, it’s funny to think that through the 90’s, no one really thought to invent a computationally simple static-site generator as they exist now. People moved pretty much directly from manually edditing HTML files manually into massive proprietary WYSIWYG editors and web “frameworks” that regenerate web pages on every single visit.
>
> This lack of vision and inability to see the simpler solution has largely produced the slow-loading, content-minimal web of today and the bizarre culture of modern “webdevs” whose diets consist in anti-patterns.

### [Tuple’s Pair Programming Guide](https://tuple.app/pair-programming-guide/)

> Tips, tutorials, and resources for thoughtful pair programmers.

### [How Docker broke in half](https://www.infoworld.com/article/3632142/how-docker-broke-in-half.html)

> The game changing container company is a shell of its former self. What happened to one of the hottest enterprise technology businesses of the cloud era?

### [12 Ways to Improve Your Monolith Before Transitioning to Microservices](https://semaphoreci.com/blog/monolith-microservices)

> A word of advice: don’t write off the monolith just yet. With some preparation, it can serve you well all the way through the transition. Here are 12 tips for making the transition to microservices as smooth as possible.

### [Workplaces are not for thinking](https://tedbauer2003.medium.com/workplaces-are-not-for-thinking-6bb23f24a86c)

> Cognitive learning basically means the same thing as “thinking,” and thinking is pretty much dead in the river at most companies.

### [What if work had mandatory “Stop And Think” periods?](https://thecontextofthings.com/2014/11/16/stop-and-think-at-work/)

> It’s just a 20-minute stop. You stop working and go talk to people, go walk around and stretch, go play some ping-pong, maybe if it’s Friday you grab a beer from the office fridge, whatever. You just stop and disconnect, and then you reconnect. Simple.

## Python

### [6 Usage Patterns for the ThreadPoolExecutor in Python](https://superfastpython.com/threadpoolexecutor-usage-patterns/)

> You can adopt one of the common usage patterns to get the most out of the ThreadPoolExecutor in Python.

### [Don't let dicts spoil your code](https://roman.pt/posts/dont-let-dicts-spoil-your-code/)

> How often do your simple prototypes or ad-hoc scripts turn into fully-fledged applications?
>
> The simplicity of organic code growth has a flip side: it becomes too hard to maintain. The proliferation of dicts as primary data structures is a clear signal of tech debt in your code. Fortunately, modern Python provides many viable alternatives to plain dicts.

### [Apache Airflow in 2022: 10 Rules to Make It Work](https://towardsdatascience.com/apache-airflow-in-2022-10-rules-to-make-it-work-b5ed130a51ad)

> Airflow is by default very permissive and without strict rules you are likely to fail in your pipeline stack implementation.

### [Design by Contract in Python](https://python.plainenglish.io/design-by-contract-in-python-44db6e899db2)

> Design by contract (DbC), also known as contract programming, programming by contract and design-by-contract programming, is an approach for designing software. It prescribes that software designers should define formal, precise and verifiable interface specifications for software components, which extend the ordinary definition of abstract data types with preconditions, postconditions and invariants.
>
> — [wikipedia.org (Design by Contract)](https://en.wikipedia.org/wiki/Design_by_contract)

### [Yes, I have opinions on your open source contributions ](https://www.b-list.org/weblog/2022/jul/11/pypi/)

> Recently the Python Package Index announced that they will be implementing new account-security policies, and hoo boy are some people ever worked up about it. This has already escalated to the author of at least one high-download-count package — one which was a dependency of pytest, thus likely to break a lot of people’s testing and CI right as the weekend started, always nice — deleting their package from PyPI out of anger and announcing they intend to stop maintaining it, though it has now, at the author’s request, been restored by the PyPI maintainers.

### [Organize Python code like a PRO](https://guicommits.com/organize-python-code-like-a-pro/)

> For every minute spent in organizing, an hour is earned.
> by Benjamin Franklin

### [It’s Time to Say Goodbye to These Obsolete Python Libraries](https://python.plainenglish.io/its-time-to-say-goodbye-to-these-obsolete-python-libraries-7c02aa77d84a)

> Forget about `os.path`, `random`, `pytz`, `namedtuple` and more and start using the latest and greatest Python libraries.

## Django

### [How to Run a Django Migration “By Hand”](https://adamj.eu/tech/2022/06/29/run-a-django-migration-by-hand/)

> In this post we’ll cover the process for running a migration by hand, and adapting it to reversing migrations.

### [Six things I do every time I start a Django project](https://brntn.me/blog/six-things-i-do-every-time-i-start-a-django-project/)

> I start a lot of projects. A lot! Django is my go-to framework for spinning up a quick personal project, and while it's a fantastic framework, a big part of the reason I love Django is that it feels familiar.

### [How to learn Django for free in 2022](https://ctrlzblog.com/how-to-learn-django-for-free-in-2022/)

> Learn Django for free with my list of recommended resources for all levels.

## Python libraries

### [TomSchimansky/CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

> A modern and customizable python UI-library based on Tkinter.

### [everythingishacked/CheekyKeys](https://github.com/everythingishacked/CheekyKeys)

> Use Python, OpenCV, and MediaPipe to control a keyboard with facial gestures.

## Django libraries

### [django-rich-logging](https://github.com/adamghill/django-rich-logging)

> A prettier way to see Django requests while developing.

## Go

### [Golang Example](https://golangexample.com/)

> A nice collection of often useful examples done in Golang.

## Tools

### [kindle2notion](https://github.com/paperboi/kindle2notion)

> Export all clippings from your Kindle device to a database in Notion.

## Cloud

### [CI/CD for GKE using Cloud Deploy](https://davelms.medium.com/automate-gke-deployments-using-cloud-build-and-cloud-deploy-2c15909ddf22)

> This tutorial will guide you through creating a CI/CD Pipeline on the Google Cloud Platform using Cloud Build and Cloud Deploy.

### [Preparing for success with the GCP Professional Cloud Network Engineer Exam](https://medium.com/google-cloud/preparing-for-success-with-the-gcp-professional-cloud-network-engineer-exam-da230f9788ed)

> If you are interested in learning networking on Google Cloud, then the Google Professional Cloud Network Engineer certification is the right challenge for you. The exam covers a lot of the core areas of networking in GCP and is rigorous enough to keep you thinking.

### [Authentication between microservices: Is it really that hard?](https://medium.com/google-cloud/authentication-between-microservices-is-it-really-that-hard-b73785510db4)

> A microservice architecture is all about services that invoke each other. But how do you keep that secure, making sure that only your own services can call each of your services? How do you authenticate?

### [Serverless Spark ETL Pipeline Orchestrated by Airflow on GCP](https://medium.com/google-cloud/serverless-spark-etl-pipeline-orchestrated-by-airflow-on-gcp-199efbf9a9f3)

> In this article, I will discuss how a Spark ETL pipeline can be executed in a completely serverless mode on GCP.

### [3 DevOps Courses You Need in 2022](https://faun.pub/3-devops-courses-you-need-in-2022-d1b076e01de3)

> These courses will make you a beast in DevOps if you’re willing to take a challenge.

### [Why I definitively switched from Cloud Functions to Cloud Run](https://medium.com/google-cloud/why-i-definitively-switched-from-cloud-functions-to-cloud-run-635d03f1eb4d)

> On Google Cloud, Cloud Functions is (was?) one of the most popular services to deploy a simple piece of code in HTTP mode or in Background mode (answer to events, like PubSub messages or Cloud Storage events).
>
> However, the introduction of Cloud Run in 2019 and the very fast and very good feature additions to the product lead me to reconsider the use of Cloud Functions and, slowly, lead me to abandon it.

### [Eventarc - Google Cloud Platform](https://cloud.google.com/eventarc)

> Eventarc lets you asynchronously deliver events from Google services, SaaS, and your own apps using loosely coupled services that react to state changes. Eventarc requires no infrastructure management — you can optimize productivity and costs while building a modern, event-driven solution.

## Other stuff

### [Every Programmer Should Know](https://github.com/mtdvio/every-programmer-should-know)

> A collection of (mostly) technical things every software developer should know about.

## Podcasts

### [The Untold Stories of Open Source - The Business Side of Open Source, with Patrick Debois](https://github.com/linuxfoundation/lf-podcast/blob/main/docs/podcasts/business-of-open-source.mdx)

> The first time Patrick Debois came into contact with Open Source was in the early stages of development of the Linux kernel, compiling it on floppies on his 486 machine. To tell you how long ago that was, the Intel 486 was introduced in 1989, It was the first chip in the line to include a built-in math coprocessor.
>
> Patrick was an early adopter of computers, but one thing he missed was a community. In those days he had to copy software over electronic bulletin board systems. But with the Linux kernel, he found it amazing that you could just get it on a cd-rom and pass it around to friends.
>
> From the Linux Foundation office in New York City, this is "The Untold Stories of Open Source". Each week we choose an open source project or a person behind a popular open source initiative, to uncover the untold stories and details about major open source initiatives. If you work with open source, and you do whether you know it or not, you're in the right place.

## Videos

### [Luke Smith: Hugo Actually Explained (Websites, Themes, Layouts, and Intro to Scripting)](https://www.youtube.com/watch?v=ZFL09qhKi5I)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/ZFL09qhKi5I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Making Badass Developers - Kathy Sierra (Serious Pony) keynote](https://www.youtube.com/watch?v=FKTxC9pl-WM)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/FKTxC9pl-WM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Randy Pausch Last Lecture: Achieving Your Childhood Dreams](https://www.youtube.com/watch?v=ji5_MqicxSo)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/ji5_MqicxSo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [The Conflict and Burnout Survival Guide: Handling When Things Go Wrong](https://www.youtube.com/watch?v=3dyVzWWerXY)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/3dyVzWWerXY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Jarek Potiuk: Contributing to Apache Airflow - Starting Your OSS Adventure](https://www.youtube.com/watch?v=Ck_Jc_95jSM)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/Ck_Jc_95jSM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Jez Humble | Continuous Delivery](https://www.youtube.com/watch?v=skLJuksCRTw)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/skLJuksCRTw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [ Why Do So Many Programmers Lose Hope? ](https://www.youtube.com/watch?v=NdA6aQR-s4U)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/NdA6aQR-s4U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Jonathan Haidt: Has Social Media Destroyed a Generation?](https://www.youtube.com/watch?v=Ocm_75ivYT0)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/Ocm_75ivYT0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [](https://www.youtube.com/watch?v=VIDEO_ID)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/VIDEO_ID" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [](https://www.youtube.com/watch?v=VIDEO_ID)

> Playback on other websites has been disabled by the video owner. [Watch on YouTube](https://www.youtube.com/watch?v=VIDEO_ID)
