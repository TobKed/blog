Title: Month summary - December 2020
Date: 2020-12-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2020 
Slug: 2020-december-links
Summary: Interesting stuff from the month
Status: published

# December 2020

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

This month was quite limited due to the long Christmas holidays during which I did not spend too much time in front of the computer.

Some time ago in one of the projects I came across the problem of too long response time on one of the websites. The form on this website is responsible for triggering operations dependent on external APIs.
The request timeout on Heroku where it is deployed is limited to thirty seconds and apparently, from time to time handling this form exceeds that limit.
Not only does it spell very poor user experience, it also causes server error when timeout is exceeded and the requested task is only partially completed.

Inspired by the blog post about [using Celery with Flask](https://blog.miguelgrinberg.com/post/using-celery-with-flask),
written by a great developer [Miguel Grinberg](https://blog.miguelgrinberg.com), I made something similar in Django.
The proposed solution is to trigger a long-running task on the website. The task will be performed asynchronously by the Celery worker and a dynamic progress bar will inform about its status.
In the repository [django_celery_progress_bar](https://github.com/TobKed/django_celery_progress_bar) I created a simple Django app with two Celery workers. The first worker called `celeryworker`  is responsible for executing scheduled periodic tasks,
while the second one, called `celeryworker_highprio` is responsible for handling tasks triggered by the web form. The response from the app is returned immediately with initial task status. Then the progress bar updates are handled by a javascript function executed in a loop until it finishes.

![Progress Bar](https://raw.githubusercontent.com/TobKed/django_celery_progress_bar/main/images/progress_bar.gif)

On another note, I have been tracking my expenditures for many years. At the beginning I used spreadsheets but updating it was cumbersome and inconvenient. To make it more friendly I wrote a web app for it in Flask some time ago: [Home-Budgeting-App](https://github.com/TobKed/Home-Budgeting-App).
I have used it for a year approximately. I decided to rewrite it to Django to be able to use its powerful admin panel. This is how
([yet_another_home_budgeting_app](https://github.com/TobKed/yet_another_home_budgeting_app)) was created.

## Articles

### [Always leave the code better than you found it](https://letterstoanewdeveloper.com/2020/11/23/always-leave-the-code-better-than-you-found-it/)

> What are some ways to improve the code when you are in it?

### [Build the Perfect Productivity System with Paper Notebooks and Digital Tools](https://zapier.com/blog/digital-and-paper-note-taking-systems/)

> Combine the Bullet Journal and other note-taking methods with your favorite apps

### [Productivity: Meaning, Concept, Formulas, Techniques, Measurement and Advantages](https://www.economicsdiscussion.net/management/productivity-meaning-concept-formulas/32324)

> Productivity refers to the physical relationship between the quantity produced (output) and the quantity of resources used in the course of production (input).

### [How I Hired a Freelance Editor for My Blog](https://mtlynch.io/editor/)

> “Hey, you had great ideas in that post, but I never read them because your repetitive sentence structure lost my attention, and I closed the tab.” An editor actually can give me that kind of feedback.

### [Laziness Does Not Exist](https://humanparts.medium.com/laziness-does-not-exist-3af27e312d01)

> But unseen barriers do

### [The Complete Guide to Effective Reading](https://maartenvandoorn.nl/reading-guide/)

> Learning is a heavily misunderstood concept.

### [How to Prioritize When There’s Always More To Do](https://blog.doist.com/how-to-prioritize/)

> Advice for managing life's chaos and focusing on what's important

### [How much I made as a really good Engineer at Facebook](https://medium.com/@anyengineer/how-much-i-made-as-a-really-good-engineer-at-facebook-9366151b52db)

> When I moved to US to join Facebook a decade back, I had no idea whether the offer I was given was good or bad.

### [How to Make Your Code Reviewer Fall in Love with You](https://mtlynch.io/code-review-love/)

> This article describes best practices for participating in a code review when you’re the author.

### [Warren Buffett’s “2 List” Strategy: How to Maximize Your Focus and Master Your Priorities](https://jamesclear.com/buffett-focus)

> Let's talk about the simple 3-step productivity strategy that Warren Buffett uses to help his employees determine their priorities and actions.

### [If You Commit to Nothing, You’ll Be Distracted By Everything](https://jamesclear.com/mental-toughness-marathon-monks)

> The Kaihogyo is a 1,000 day challenge that takes place over seven years.

### [This Is Water: Overcoming Bias and How to Think Real Good](https://maartenvandoorn.nl/this-is-water-overcoming-bias-and-how-to-think-real-good/)

> Once upon a time, there used to be a great and acrimonious debate in philosophy about whether people had “mental imagery” — whether or not people actually see a little picture of an elephant when they think about an elephant.

### [Google Cloud (over)Run: How a free trial experiment ended with a $72,000 bill overnight](https://www.theregister.com/2020/12/10/google_cloud_over_run/)

> Billing budget? Free plan? All useless when buggy code went into overdrive

### [Shifting to a remote mindset](https://increment.com/remote/remote-work-mindset/)

> On moving away from the in-office default and considering how to achieve what you value.

### [How to Think: The Skill You’ve Never Been Taught](https://fs.blog/2015/08/how-to-think/)

> “I’ve spent my life trying to undo habits—especially habits of thinking. They narrow your interaction with the world. They’re the phrases that come easily to your mind, like: ‘I know what I think,’ or ‘I know what I like,’ or ‘I know what’s going to happen today.’ If you just replace ‘know’ with ‘don’t know,’ then you start to move into the unknown. And that’s where the interesting stuff happens.”
> — Humans of New York

## Python

### [Using Python's bisect module ](https://johnlekberg.com/blog/2020-11-21-stdlib-bisect.html)

> The goal of the bisect module is to allow you to efficiently search and update sorted lists.

### [Build a Flask microservice with OpenFaaS](https://www.openfaas.com/blog/openfaas-flask/)

> Which is better Flask or serverless-style Python functions? Why not have both?

## Tools

### [ripgrep (rg)](https://github.com/BurntSushi/ripgrep)

> ripgrep is a line-oriented search tool that recursively searches your current directory for a regex pattern. By default, ripgrep will respect your .gitignore and automatically skip hidden files/directories and binary files.

### [todo.txt-cli](https://github.com/todotxt/todo.txt-cli)

> A simple and extensible shell script for managing your todo.txt file.

### [fastai/ghapi](https://github.com/fastai/ghapi)

> A delightful and complete interface to GitHub's amazing API

### [Typer](https://github.com/tiangolo/typer)

> Typer, build great CLIs. Easy to code. Based on Python type hints.

### [diagrams](https://github.com/mingrammer/diagrams)

> Diagram as Code.

## Videos

### [The Art of Code - Dylan Beattie](https://www.youtube.com/watch?v=6avJHaC3C2U)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/6avJHaC3C2U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [YAML Tips for Kubernetes](https://www.youtube.com/watch?v=1rwCkFTjikw)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/1rwCkFTjikw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Peter Norvig: How Computers Learn](https://www.youtube.com/watch?v=T1O3ikmTEdA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/T1O3ikmTEdA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Czy leci z nami DevOps? Webinar](https://www.youtube.com/watch?v=UGwayrJiFAA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/UGwayrJiFAA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [DjangoCon US 2017 - End-to-End Django on Kubernetes by Frank Wiles](https://www.youtube.com/watch?v=4LpaxvKsSlo)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/4LpaxvKsSlo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
