Title: Month summary - September 2023
Date: 2023-09-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2023
Slug: 2023-september-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2023/2023_09_xx.jpg
Status: published

# September 2023

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

This month, I had the pleasure of attending the incredible [PyCon CZ](https://cz.pycon.org/2023/) conference in Prague.
The excitement began even before I arrived in Prague, as I had the chance to meet John and Judy from the USA during my train journey.
John, a retired programmer, shared stories of his work with natural language, SQL-Windows, and COBOL.
It felt like I was meeting a living legend!

During the train ride, I also had the pleasure of getting to know Piotr, the organizer of [PyKonik](https://www.pykonik.org/).
The conference itself was a fantastic experience, with a multitude of great people and captivating presentations.

One of the best moments of the conference for me was when I put myself on the list for the Lightning Talks.
This was a huge challenge for me as I am usually quite nervous when it comes to public speaking, but I was determined to push myself out of my comfort zone.
The title of my presentation was "**ML (Fast)API below 100ms (on GCP)**".
The presentation, as well as all the resources related to it, can be found in [my repository](https://github.com/TobKed/fastapi_cloudrun_pubsub).
I have provided an end-to-end working example on Google Cloud that demonstrates how to defer load from FastAPI (served by [CloudRun](https://cloud.google.com/run)) to a background worker (also on CloudRun) via a queueing system ([PubSub](https://cloud.google.com/pubsub)).
After practicing my presentation numerous times in my hotel room, I finally stepped onto the stage and gave it my all.

Overall, it was an incredible experience that allowed me to learn new skills, connect with amazing individuals and showcase my capabilities as a developer. I am grateful for these opportunities and look forward to what the future holds!

![PyCon CZ.]({static}/images/posts/2023/2023_09_pyconcz.jpg)

I also refreshed my [Google Associate Cloud Engineer certificate](https://www.credential.net/profile/tobiaszkdzierski610060/wallet) and revisited the fundamentals.

![Google Associate Cloud Engineer certficate]({static}/images/posts/2023/2023_09_gcp_ace.png)\]

## Articles

### [Should That Be a Microservice? Keep These Six Factors in Mind](https://tanzu.vmware.com/content/blog/should-that-be-a-microservice-keep-these-six-factors-in-mind)

> The road to microservices is paved with good intentions.
> But more than a few teams are jumping on the bandwagon without analyzing their needs first.
> Microservices are powerful, and they should absolutely be in your toolbox! Just make sure you consider the tradeoffs.

### [Shopify: 10 Tips for Building Resilient Payment Systems](https://shopify.engineering/building-resilient-payment-systems)

> It’s hard to learn something when you don’t know what you don’t know.
> As I learned things over the years—sometimes the hard way—I eventually found myself passing on these lessons to others.
> I distilled these topics into a presentation I gave to my team and boiled that down into this blog post

### [You don't need UUID](https://henvic.dev/posts/uuid/)

> I’ve experienced first-hand how using UUID hurts the usability of computer systems, and I want you to understand why you certainly don’t need it.

### [Tracing: structured logging, but better in every way](https://andydote.co.uk/2023/09/19/tracing-is-better/#evolving-logs)

> I figured it was time to write down why I think logs are bad, why tracing should be used instead, and how we get from one to the other.

### [The 10 Types of Authorization](https://www.osohq.com/post/ten-types-of-authorization)

> So, here we’ve outlined ten definitions to help engineers pattern match and advance the state of thinking on the authorization domain.
> There are likely more patterns, but for now this is a start

### [Understanding networking in Kubernetes](https://www.learncloudnative.com/blog/2023-05-31-kubeproxy-iptables)

> In this article, we'll look into how networking works in Kubernetes and explain how the pods can communicate with each other and the outside world.

## AI

### [Kurasiński - Darmowy kurs tworzenia grafik AI – Hello Midjourney!](https://blog.kurasinski.com/2023/06/darmowy_kurs_midjourney_grafika_ai/)

> Kurs jest przewidziany dla osób, które nie mają doświadczenia z AI, programami graficznymi i mają tzw „dwie lewe ręce” jeśli chodzi o kreacje i grafikę ;)

## Security

### [25 Hard-Hitting Lessons from 17 Years in Cybersecurity](https://www.returnonsecurity.com/p/25-cybersecurity-industry-truths)

> Dive into the no-filter truths from a 17-year cybersecurity career.
> These straight-shooting insights will help you navigate the intricacies and paradoxes of the cybersecurity industry.

## Python

### [The easy way to concurrency and parallelism with Python stdlib ](https://www.bitecode.dev/p/the-easy-way-to-concurrency-and-parallelism)

> Because life doesn't have to be hard all the time

### [Advanced Python Mastery](https://github.com/dabeaz-course/python-mastery)

> An exercise-driven course on Advanced Python Programming that was battle-tested several hundred times on the corporate-training circuit for more than a decade.

### [Weekly Report, EuroPython 2023 - Łukasz Langa](https://lukasz.langa.pl/b2f7ec83-a65d-4ab8-aa03-0212a299d7fd/)

> This conference was intense!
> Countless positive interactions, deeply technical conversations, and the notoriously vegetable-free Czech food (+beer!) combined into a very positive experience.

## Videos

### [Google Cloud Next '23—Developer Keynote](https://www.youtube.com/watch?v=268jdNwH6AM)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/268jdNwH6AM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
