Title: Month summary - November 2020
Date: 2020-11-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2020 
Slug: 2020-november-links
Summary: Interesting stuff from the month
Status: published


# November 2020

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.


## Some thoughts

This month I spent some time on getting statistics of GitHub Actions [GA] usage within The Apache Software Foundation [ASF] repositories. 
The ASF organisation has more than 2000 repositories and more than 200 of them use GA. 
The limit for concurrent GA jobs for ASF equals 180 ([usage limits](https://docs.github.com/en/free-pro-team@latest/actions/reference/usage-limits-billing-and-administration#usage-limits)) and may be exhausted quite quickly. 
This could lead to long queues. 
The GItHub does not provide statistics related to GA so I created a repository [Fetch Apache GitHub Actions Statistics](https://github.com/TobKed/fetch-apache-ga-stats). 
Within this repository, the statistics data is fetched by a GA workflow scheduled to run every 15 minutes. 
This workflow makes a series of "snapshots" of GA workflow runs in `in_progress` and `queued` statuses for every ASF repository which uses GA. 
Since verifying which one of more than 2000 repositories use GA is expensive because of exhausting api rate limits, this list is stored in a file within the repository. 
The other GA workflow scheduled to run once a week is fetching this list and committing changes to the repository.

Within Apache Airflow I introduced asynchronous execution of Dataflow jobs. 
It allows starting a data processing pipeline without having to wait until it finishes. 
The status of the pipeline may be monitored by new sensors ([DataflowJobStatusSensor](https://github.com/apache/airflow/pull/11726), [DataflowJobMetricsSensor](https://github.com/apache/airflow/pull/12039), [DataflowJobMessagesSensor and DataflowAutoscalingEventsSensor](https://github.com/apache/airflow/pull/12249)).


## Articles

### [10 Things to Do After Installing Ubuntu 20.10](https://www.omgubuntu.co.uk/2020/10/things-to-do-after-installing-ubuntu-20-10-groovy-gorilla)

> A new Ubuntu release means a new rundown of the most important post-install procedures you should perform.

### [Get started with 2-minute rule](https://centrum-probalans.erecepcja24.pl/?action=myVisits)

> Scale any task down into a 2-minute version to make it easier to get started.

### [Good morning, bad morning](https://vasilishynkarenka.com/good-morning-bad-morning/)

> “If you want to change the world, start off by making your bed.” – William H. McRaven

### [Talking, Typing, Thinking: Software Is Not a Desk Job](https://daniel.fone.net.nz/blog/2020/10/21/talking-typing-thinking-software-is-not-a-desk-job/)

> Developers over-optimise for the ergonomics of typing and not enough for the ergonomics of thinking.

### [How to be more productive working from home: 9 rules for the “now normal”](https://www.atlassian.com/blog/productivity/more-productive-working-from-home)

> Science-backed, expert-approved tactics you can start using today.

### [Maker's schedule, manager's schedule](http://www.paulgraham.com/makersschedule.html)

> "...the mere consciousness of an engagement will sometimes worry a whole day."
> – Charles Dickens 

### [7 Cognitive Biases That Make Us Suck at Time Management](https://blog.doist.com/cognitive-biases-time-management/)

> Our brains are hardwired to sabotage our productivity. Can we do anything about it? 

### [The Top 7 Best Practices For Leading Effective Virtual Team Meetings](https://weworkremotely.com/the-top-7-best-practices-for-leading-effective-virtual-team-meetings)

> Stop wasting your remote team’s time. These best practices for virtual meetings will help you run more efficient calls and boost employee engagement. 

### [8 questions for writing](https://vasilishynkarenka.com/8questions/)

> The secret to good writing, as to any kind of knowledge work, is deliberate planning.

### [Time Blocking](https://todoist.com/productivity-methods/time-blocking)

> ...and its cousins task batching and day theming. Control your schedule so it doesn't control you

### [The Weekly Review](https://todoist.com/productivity-methods/weekly-review)

> 10x your productivity with just one hour a week

### [The Complete Guide to Deep Work](https://blog.doist.com/deep-work/)

> How to master the #1 job skill that will never be obsolete

### [The Complete Guide to Planning Your Day](https://blog.doist.com/how-to-plan-your-day/)

> The 10-minute productivity practice for achieving more in work and life

### [You should expect "equal pay for equal work" at your new remote job](https://www.nityesh.com/equal-pay-for-equal-work-at-a-remote-company/)

> Tough questions to ask your remote employer who gives you Cost Of Living based compensation and some thoughts on how remote compensation will work in the future

### [How to Avoid Zoom Fatigue in Your Weekly Virtual Meetings](https://weworkremotely.com/how-to-avoid-zoom-fatigue-in-your-weekly-virtual-meetings)

> Zoom virtual meetings dragging you down? Discover what Zoom fatigue is, why it happens, and what you can do to lessen its effects in this guide

### [We tried not looking at our screens first thing in the morning. It helped.](https://zapier.com/blog/no-screens-in-the-morning/)

> Want to feel stressed, anxious, and/or completely exhausted before you even have breakfast? I highly recommend looking at your phone right when you wake up.

### [Remote Work Productivity Hacks: 33 Best Tips From Experts](https://arc.dev/blog/remote-work-productivity-tips-ad27ns7c15)

> Supercharge your workday with these remote work productivity tips from some of the best in the business.

## Django

### [How to Setup Django with React](https://mattsegal.dev/django-react.html)

> A detailed guide to the various steps required to have React play well with Django.

## Tools

### [asciinema](https://asciinema.org/)

> Record and share your terminal sessions, the right way

### [pipdeptree](https://github.com/naiquevin/pipdeptree)

> `pipdeptree` is a command line utility for displaying the installed python packages in form of a dependency tree

### [LocalStack - A fully functional local AWS cloud stack](https://github.com/localstack/localstack)

> LocalStack provides an easy-to-use test/mocking framework for developing Cloud applications.

## Cloud

### [O chmurze w biznesie (i nie tylko) z Krzysztofem Zalasą z Google](https://oceandanych.pl/o-chmurze-w-biznesie-z-krzysztofem-zalasa/)

> Krzysiek z zamiłowania jak i wykonywanej pracy bardzo dużo pracuje z technologiami chmurowymi. Dzięki temu możesz przeczytać o doświadczeniach osoby, która długo siedzi w branży oraz posiada dużo historii „z placu boju”

### [Google Cloud – Improving Security with Impersonation](https://www.jhanley.com/google-cloud-improving-security-with-impersonation/)

>  The contents of the service account remain in Google Cloud. Instead of providing users with a service account file, we provide the user authorization to use the service account (impersonation). 
