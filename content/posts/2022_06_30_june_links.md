Title: Month summary - June 2022
Date: 2022-12-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2022
Slug: 2022-june-links
Summary: Interesting stuff from the month
Status: published
Header_Cover: /images/posts/2022/2022_06_xx.JPG

# June 2022

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

This month I did a lot of sport, Kubernetes, Terraform and GitHub Actions. Not necessarily in that order.
Maybe even too much since I did not have energy to read or watch too many interesting things,
however I made an internal presentation about the last one: GitHub Actions.
I am a huge fan of this CI/CD and I am pretty experienced with it.
`Sharing is caring` so I wanted to share some hints and tips which may not be obvious and/or not documented very well.
For this purpose I created a repository [TobKed/github_actions_demo](https://github.com/TobKed/github_actions_demo)
and some slides. It was a light tech talk and took me approximately 10 minutes which was a pretty fun experience all in all.

## Articles

### [„Otaczałem się drogimi, niepotrzebnymi rzeczami” – rozmowa z Wojtkiem Zającem](https://geek.justjoin.it/wojtek-zajac-na-zdalniaku-wywiad)

> Zwiedził 50 krajów, pracował zdalnie z wielu miejsc na całym świecie. Od najbardziej przyziemnych, po te absolutnie egzotyczne. W 2015 roku po prostu kupił bilet w jedną stronę i nie wyobraża już sobie, że można żyć inaczej. Wojtek Zając to inspirujący programista, który chętnie dzieli się wiedzą i swoimi doświadczeniami.

## Python

### [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)

> “Format specifications” are used within replacement fields contained within a format string to define how individual values are presented (see Format String Syntax and Formatted string literals).

### [Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)

> The syntax is related to that of formatted string literals, but it is less sophisticated and, in particular, does not support arbitrary expressions.

### [Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

> A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.

### [How to Create a Command-line Application with argparse](https://www.blog.pythonlibrary.org/2022/05/19/how-to-create-a-command-line-application-with-argparse/)

> Python comes with a built-in library called argparse that you can use to create a command-line interface.

## Django

### [Django: How to send email without Celery](https://nemecek.be/blog/158/django-how-to-send-email-without-celery)

> Lightweight emails without Celery. And without a request-response cycle.

## Cloud

### [Protect sensitive info in logs using Google Cloud](https://medium.com/google-cloud/protect-sensitive-info-in-logs-using-google-cloud-4548211d4654)

> Application logs may capture information that includes sensitive or proprietary data. As a result, this data may be available to unauthorized personnel that have access to application logs but should not be able to access that sensitive data

### [6 Important things you need to run Kubernetes in production](https://www.pionative.com/post/6-important-things-you-need-to-run-kubernetes-in-production)

> Kubernetes is a very complex platform, but setting up a Kubernetes cluster is fairly easy as long as you choose a managed cloud solution. I would never advise self-managing a Kubernetes cluster unless you have a very good reason to do so.
