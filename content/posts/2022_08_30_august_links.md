Title: Month summary - August 2022
Date: 2022-08-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2022
Slug: 2022-august-links
Summary: Interesting stuff from the month
Status: draft
Header_Cover: /images/posts/2022/2022_08_xx.jpg

# August 2022

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

I setup deployment of [Saleor](https://saleor.io/) on Google Kubernetes Engine with [Terraform](https://www.terraform.io/).
Additionally, I learnt and used [Terragrunt](https://terragrunt.gruntwork.io/) (wrapper for terraform).
Saleor is an open-source e-commerce platform.
It consists of three services: Core, Dashboard and Storefront.
The Core is written in Python (Django) and exposes GraphQL API which is consumed by Dashboard and Storefront (both written in React).

## Articles

### [Protestware on the rise: Why developers are sabotaging their own code](https://techcrunch.com/2022/07/27/protestware-code-sabotage/)

> A developer can, on a whim, change their mind and do whatever they want with their open source code that, most of the time anyway, comes “as is” without any warranty.
> Or, as seen by a growing trend this year, developers deliberately sabotaging their own software libraries as a means of protest — turning software into “protestware.”

### [How to support open-source software and stay sane](https://www.nature.com/articles/d41586-019-02046-0)

> Releasing lab-built open-source software often involves a mountain of unforeseen work for the developers.

### [7 Github Actions Tricks I Wish I Knew Before I Started](https://yonatankra.com/7-github-actions-tricks-i-wish-i-knew-before-i-started/)

> Here are 7 tricks with github actions that changed my life (or at least my CI/CD pipeline).
> These tricks helped me create a more maintainable workflows code as well as boosted performance of the whole CI/CD process.

### [Introducing GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html)

> [GitFlow](http://nvie.com/posts/a-successful-git-branching-model/) is a branching model for Git, created by Vincent Driessen.
> It has attracted a lot of attention because it is very well suited to collaboration and scaling the development team.

## Python

### [Everything you need to know about involuntary borgs in Python](https://bas.codes/posts/python-involuntary-borgs)

> Python, in general, is a pass-by-reference language. What does that mean, and what do you need to look out for?

### [Building an authenticated Python CLI](https://www.notia.ai/articles/building-an-authenticated-python-cli)

> We are going to be building an interactive, authenticated Python CLI that uses the Twitter API to fetch the top Machine Learning tweets of the week!

### [7 things I've learned building a modern TUI framework](https://www.textualize.io/blog/posts/7-things-about-terminals)

> I've be working on [Textual](https://github.com/Textualize/textual) for over a year now. Here's a few things I've discovered (or re-discovered) regarding terminals in Python, and software development in general.

> — Will McGugan (CEO / Founder) @willmcgugan

### [Uncommon Uses of Python in Commonly Used Libraries](https://eugeneyan.com/writing/uncommon-python/)

> To learn how to build more maintainable and usable Python libraries, I’ve been reading some of the most widely used Python packages. Along the way, I learned some things about Python that are off the beaten path. Here are a few things I didn’t know before.

### [Understanding async Python for the web](https://www.b-list.org/weblog/2022/aug/16/async)

> But this raises a lot of questions, like: just what is “async” Python? Why do people care about it so much? And is it really that useful for building web apps? What are all these new frameworks and other tools about?

### [Python F-Strings Number Formatting Cheat Sheet](https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting/)

> Contains formulas, tables, and examples showing patterns and options focused on number formatting for Python's Formatted String Literals -- i.e., F-Strings.

## Django

### [How to use elided pagination in Django and solve too many pages problem](https://nemecek.be/blog/105/how-to-use-elided-pagination-in-django-and-solve-too-many-pages-problem)

> Since Django 3.2 there is a way to handle big pagination with large number of pages.

### [Django Hosting & Deployment Options](https://learndjango.com/tutorials/django-hosting-deployment-options)

> Django websites can be deployed on any number of hosting providers. The first choice is deciding whether to use a Platform-as-a-service (PaaS) option or a virtual private server (VPS). A PaaS is an easier albeit more expensive option that can handle many deployment issues with minimal configuration. A VPS is less expensive and provides total control but requires more knowledge and effort to setup.

### [How to Test Django Models (with Examples)](https://ctrlzblog.com/how-to-test-django-models-with-examples/)

> Learn how to test Django models.

### [Django: How to let user download a file](https://nemecek.be/blog/165/django-how-to-let-user-download-a-file)

> Creating file download links with the help of a FileResponse.

## Python libraries

### [lowbar](https://github.com/AnnikaV9/lowbar)

> The simplest no-nonsense progress bar for python.

## Django libraries

### [django-q](https://github.com/Koed00/django-q)

> A multiprocessing distributed task queue for Django

## Tools

### [MonitorControl](https://github.com/MonitorControl/MonitorControl)

> Control your display's brightness & volume on your Mac as if it was a native Apple Display. Use Apple Keyboard keys or custom shortcuts.
> Shows the native macOS OSDs.

### [pls](https://github.com/dhruvkb/pls)

> 'pls' is a prettier and powerful 'ls' for the pros.

### [musikcube](https://github.com/clangen/musikcube)

> a cross-platform, terminal-based audio engine, library, player and server written in c++.

### [firefox-csshacks](https://github.com/MrOtherGuy/firefox-csshacks/tree/master/chrome)

> Collection of random CSS hacks for Firefox

### [hidden](https://github.com/dwarvesf/hidden)

> An ultra-light MacOS utility that helps hide menu bar icons.

## Cloud

### [Kubernetes Components Simplified for Beginners](https://dev.to/iarchitsharma/kubernetes-components-simplified-for-beginners-19op)

> In this article we are going to understand the main Kubernetes Components that we as Kubernetes Administrators or users will be working with most of the time.

### [Exposing GKE applications leveraging the built-in ingress](https://medium.com/google-cloud/exposing-gke-applications-leveraging-the-built-in-ingress-e87b78e23e90)

> Today I decided to play a bit with GKE and see how to expose a simple demo application through the default GKE ingress.

### [Analysing Git repository activities with BigQuery SQL](https://medium.com/google-cloud/analysing-a-git-repository-activities-with-bigquery-sql-e40a6d85d667)

> Reports generated from git platforms are great, but what if we need more flexibility towards creating git log reports?
> In this article we explore exporting logs from a git repository into BigQuery and apply some analysis queries with SQL.

### [Preparing for the Google Cloud Professional Cloud DevOps Engineer Exam](https://medium.com/google-cloud/preparing-for-the-google-cloud-professional-cloud-devops-engineer-exam-30e9d5fe07e4)

> Site reliability Engineer is an interesting topic and taking time to learn about it would definitely be a valuable experience. The saying goes class SRE implements DevOps.

## Podcasts

### [POIT #165: Jak hostować aplikacje w GCP](https://porozmawiajmyoit.pl/poit-165-jak-hostowac-aplikacje-w-gcp/)

> Dziś moim gościem jest Piotr Gocłowski – w branży technologii od 10 lat, początkowo związany z automatyką przemysłową, a konkretnie sieciami, IoT i komunikacją szeregową.
> Cloud Architekt w GCP, posiadacz kilku certyfikatów GCP, na co dzień doradza i pomaga klientom rozwiązywać problemy związane z chmurą GCP.
> Fan Raspberry PI, Nintendo a prywatnie szczęśliwy mąż i ojciec 2 żywiołowych córek.
