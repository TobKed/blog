Title: Month summary - October 2020
Date: 2020-10-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2020 
Slug: 2020-october-links
Summary: Interesting stuff from the month
Status: published

# October 2020

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

This month I worked on improving Google Cloud Dataflow within [Apache Airflow](https://github.com/apache/airflow) project.
It was not an easy task since Dataflow is a quite complex service itself and has limited API.
I helped to introduce operators for [SQL Queries](https://github.com/apache/airflow/pull/8553) and [Flex Templates](https://github.com/apache/airflow/pull/8550).
I successfully added [`drain` option when cancelling Dataflow pipelines](https://github.com/apache/airflow/pull/11374) and helped community with [Google Cloud Memorystore Memcached Operators](https://github.com/apache/airflow/pull/10121).

I am quite interested in CI and GitHub Actions and I created an action called [Label When Approved action](https://github.com/TobKed/label-when-approved-action). It sets a label on an approved Pull Request and removes it when changes are requested.
It supports checking if approvals (or change requests) are authored by people with write access to the target repository.
It was created specifically for [Apache Airflow](https://github.com/apache/airflow) where it is used for labeling
pull requests approved by committers.
These labels (or equivalent action outputs) are used to optimise the use of CI resources since [not approved pull requests run only a subset of tests](https://github.com/apache/airflow/pull/11828). It was introduced because the number of GitHub Actions jobs running in parallel is limited to 180 for all Apache projects so running full test suite every time seemed to be a waste.
It was made in cooperation with [Jarek Potiuk](https://github.com/potiuk) who is Apache Airflow Commiter and PMC Member. It was also my first time with TypeScript which I enjoyed a lot.

Meanwhile my blog post about Terraform and Infrastructure as Code was published \[IaC\]. If you want to know why IaC and Terraform is so popular, feel free to read it: [Terraform Tutorial: Introduction to Infrastructure as Code](https://tobiaszkedzierski.medium.com/terraform-tutorial-introduction-to-infrastructure-as-code-dccec643bfdb).

## Articles

### A Short Story for Engineers (link not valid anymore)

> You don’t have to be an engineer to appreciate this story.

### [The red-flag signs you may be burning out while working from home](https://www.fastcompany.com/90554935/the-red-flag-signs-you-may-be-burning-out-while-working-from-home)

> In a remote-work world, setting up clear boundaries is integral to protecting your mental health and personal well-being.

### [Google updates Android smartphones to listen to houses for suspect sounds](https://www.independent.co.uk/life-style/gadgets-and-tech/google-android-smartphone-update-listen-house-sounds-b906331.html)

> Google says the update will make it easier for people with hearing issues to be notified of events.

### [How to Change Your Brain With Dr. Andrew Huberman (+ Utkarsh!)](https://thisten.co/y7qdc/qoLk8j26DKJ0FdUrv5EF4Z4ft3AShasQ8tiEFuYb)

> Dr. Huberman is here to school us on all things neuroplasticity---and how we can use it to our advantage through intense focus, mindfulness, and restorative sleep. Enjoy!

### [Git scraping: track changes over time by scraping to a Git repository](https://simonwillison.net/2020/Oct/9/git-scraping/)

> We already have a great tool for efficiently tracking changes to text over time: Git. And GitHub Actions (and other CI systems) make it easy to create a scraper that runs every few minutes, records the current state of a resource and records changes to that resource over time in the commit history.

### [How to take meeting notes](https://barehands.substack.com/p/how-to-take-meeting-notes)

> Author does not take notes during the meeting. Instead, he takes notes after the meeting and shares tips how to do it.

### ['I'll Never Work The Same Way Again:' One Co-Founder's Remote Work Experiments](https://www.entrepreneur.com/article/354226)

> There's a lot of talk about structure and boundaries, but there's something to be said for flexibility, and embracing the messiness of your "life's work."

### [10 Tips From CEOs on Working From Home Effectively and Happily](https://www.entrepreneur.com/article/347479)

> Far beyond getting out of your pajamas, these tips encourage wellness when you are working from home.

### [How Google Drive Can Make Every Corner of Your Life Easier](https://forge.medium.com/how-google-drive-can-make-every-corner-of-your-life-easier-9f3cc1acbb68)

> The ultimate self-improvement tool is something you already have

### [Why Life Can’t Be Simpler](https://fs.blog/2020/10/why-life-cant-be-simpler/)

> We’d all like life to be simpler. But we also don’t want to sacrifice our options and capabilities. Tesler’s law of the conservation of complexity, a rule from design, explains why we can’t have both.

### [You Don’t Have to Use Docker Anymore](https://towardsdatascience.com/its-time-to-say-goodbye-to-docker-5cfec8eff833)

> Docker is not the only containerization tool out there and there might just be better alternatives…

### [How Harvard’s Star Computer-Science Professor Built a Distance-Learning Empire](https://www.newyorker.com/news/our-local-correspondents/how-harvards-star-computer-science-professor-built-a-distance-learning-empire)

> David Malan, of the hit class CS50, was working to perfect online teaching long before the pandemic. Is his method a model for the future of higher education?

### [Surprising __getattr__ recursion](https://nedbatchelder.com/blog/201010/surprising_getattr_recursion.html)

> It’s well-known that you have to be careful in __getattr__ not to use an attribute that might be missing. That would cause an infinite recursion.

### [The psychology of learning to code](https://vasilishynkarenka.com/the-psychology-of-learning-to-code/)

> Build a habit of learning, find what you’re obsessed with, and crawl your way through The Suck.

### [16 Everyday Habits of Highly Productive People](https://www.lifehack.org/articles/productivity/16-everyday-habits-highly-productive-people.html)

> A list of 16 tips and tricks that will help guide you to a more fulfilled life.

## Django

[Modern JavaScript for Django Developers](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/)

> Working with Django in the modern JavaScript ecosystem without giving up the things that make it great

[Django Day Copenhagen 2020](https://www.youtube.com/playlist?list=PLEpW1LzVyQWhqb_OoWtURF5cfKSGof0It)

> Videos from Django Day Copenhagen.

### [A Django REST API in a Single File](https://adamj.eu/tech/2020/10/15/a-single-file-rest-api-in-django)

> The third in a series of writing Django apps in a single file, following previous posts on synchronous and asynchronous use cases.

## Tools

### [Triage Party: massively multi-player GitHub triage](https://github.com/google/triage-party)

> Triage Party is a stateless web app to optimize issue and PR triage for large open-source projects using the GitHub API.

### [terraform-docs](https://github.com/terraform-docs/terraform-docs)

> A utility to generate documentation from Terraform modules in various output formats.

### [terraformer](https://github.com/GoogleCloudPlatform/terraformer)

> A CLI tool that generates tf/json and tfstate files based on existing infrastructure (reverse Terraform).

### [terragrunt](https://github.com/gruntwork-io/terragrunt)

> Terragrunt is a thin wrapper for Terraform that provides extra tools for keeping your Terraform configurations DRY, working with multiple Terraform modules, and managing remote state.

### [Terraform Best Practices](https://github.com/ozbillwang/terraform-best-practices)

> Terraform Best Practices for AWS users.

### [Bringing-Old-Photos-Back-to-Life](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life)

> Old Photo Restoration (Official PyTorch Implementation)

### [Darling](https://www.darlinghq.org/)

> Darling is a translation layer that lets you run macOS software on Linux

### [Qubes OS](https://www.qubes-os.org/)

> Qubes OS is a free and open-source, security-oriented operating system for single-user desktop computing.

### [Tails](https://tails.boum.org/)

> Tails is a portable operating system that protects against surveillance and censorship.

### [dockle](https://github.com/goodwithtech/dockle)

> Dockle - Container Image Linter for Security, Helping build the Best-Practice Docker Image, Easy to start

### [trivy](https://github.com/aquasecurity/trivy)

> A Simple and Comprehensive Vulnerability Scanner for Containers and other Artifacts, Suitable for CI.

### [devops-exercises](https://github.com/bregman-arie/devops-exercises)

> This repo contains questions and exercises on various technical topics, sometimes related to DevOps and SRE

### [python-cheatsheet](https://github.com/gto76/python-cheatsheet)

> Comprehensive Python Cheatshee

### [boundary-layer](https://github.com/etsy/boundary-layer)

> boundary-layer is a tool for building Airflow DAGs from human-friendly, structured, maintainable yaml configuration.

## Other stuff

### [Computer Stuff They Didn't Teach You - youtube playlist](https://www.youtube.com/playlist?list=PL0M0zPgJ3HSesuPIObeUVQNbKqlw5U2Vr)

> Videos that will help you to fill in the gaps on all those little things that we should have learned in school but no one really sat down and took the time.

### [terraform-switcher](https://github.com/warrensbox/terraform-switcher/)

> The tfswitch command line tool lets you switch between different versions of terraform.

## Videos

### ["On a shoe-string and a t2.small: scaling on a \[zero\] budget." - Tom Eastman (PyConline AU 2020)](https://www.youtube.com/watch?v=A-3zc1CABqM)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/A-3zc1CABqM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Praca w korporacji - jakie ponosimy szkody zdrowotne? - prof. Paweł Januszewicz](https://www.youtube.com/watch?v=H9CJCVyD6mQ)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/H9CJCVyD6mQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [I used the reasonably-secure Qubes OS for 6 months and survived - Matty McFatty \[@themattymcfatty\]](https://www.youtube.com/watch?v=sbN5Bz3v-uA)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/sbN5Bz3v-uA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Reuven M. Lerner - Practical decorators - PyCon 2019](https://www.youtube.com/watch?v=MjHpMCIvwsY)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/MjHpMCIvwsY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
