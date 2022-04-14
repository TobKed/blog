Title: Month summary - February 2022
Date: 2022-02-28
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2022
Slug: 2022-february-links
Summary: Interesting stuff from the month
Header_Cover: /images/posts/2022/2022_02_xx.jpg
Status: draft

# February 2022

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

I watched a very nice talk about structuring a Django application ([Radoslav Georgiev - Django structure for scale and longevity](https://www.youtube.com/watch?v=yG3ZdxBb1oo))
and analyzed the repository complementary to that talk ([Django Styleguide](https://github.com/HackSoftware/Django-Styleguide/)).
TLDR/TLDW: the whole idea behind it is that all business logic **should NOT** live in:

- APIs and Views.
- Serializers and Forms.
- Form tags.
- Model save method.
- Custom managers or querysets.
- Signals

but in:

- **Services** - functions that mostly take care of writing things to the database.
- **Selectors** - functions that mostly take care of fetching things from the database.
- **Model properties** (with some exceptions).
- **Model clean method** for additional validations (with some exceptions).

This seems to be a pretty awesome idea. Often,
the business logic is spread across Django in views or serializers and with a growing project it is easy to fall into some redundancy here and there.
Afterwards, with updates and further growth it is getting harder to keep track of where scattered logic parts live.
The proposed structure helps to keep all crucial logic in an intuitive place (like service) and reuse it in views, serializers etc.
This Django Styleguide speaks to me since I had the pleasure to work on a project which was written in Flask but also facilitated services.
For more details watch the talk and check the repo.

Other highlights of the month: I made some improvements to my GitHub Action [TobKed/github-forks-sync-action](https://github.com/TobKed/github-forks-sync-action).
In addition to bug fixes I put together an example of syncing multiple branches.
It emerged from the discussion on the [issue](https://github.com/TobKed/github-forks-sync-action/issues/13).

## Python

### [cmd](https://docs.python.org/3/library/cmd.html#module-cmd)

> The Cmd class provides a simple framework for writing line-oriented command interpreters. These are often useful for test harnesses, administrative tools, and prototypes that will later be wrapped in a more sophisticated interface.

## Django

### [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide/)

> Django styleguide that we use in HackSoft.
>
> 1. We have a [Styleguide-Example](https://github.com/HackSoftware/Styleguide-Example) to show most of the styleguide in an actual project.
>    2, You can watch Radoslav Georgiev's [Django structure for scale and longevity](https://www.youtube.com/watch?v=yG3ZdxBb1oo) for the philosophy behind the styleguide.

## Tools

### [Lurnby](https://github.com/Roznoshchik/Lurnby)

> A tool for active reading and personal knowledge management.

### [gitstats](https://github.com/bagder/gitstats)

> git history statistics generator

## Go

### [How We Write GitHub Actions in Go](https://full-stack.blend.com/how-we-write-github-actions-in-go.html)

> Below, we’ll share the set of unique challenges for running and releasing actions written in Go and outline our strategies for solving these problems.

### [github.com/fatih/vim-go](https://github.com/fatih/vim-go)

> Go development plugin for Vim

## Other stuff

### [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)

> Classes teach you all about advanced topics within CS, from operating systems to machine learning, but there’s one critical subject that’s rarely covered, and is instead left to students to figure out on their own: proficiency with their tools. We’ll teach you how to master the command-line, use a powerful text editor, use fancy features of version control systems, and much more!

## Videos

### [Marty Lobdell - Study Less Study Smart](https://www.youtube.com/watch?v=IlU-zDU6aQ0)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/IlU-zDU6aQ0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Radoslav Georgiev - Django structure for scale and longevity](https://www.youtube.com/watch?v=yG3ZdxBb1oo)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/yG3ZdxBb1oo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Inside Security - S01E17 | The creator of Curl, Daniel Stenberg, joins the show for an interview](https://www.youtube.com/watch?v=06Xfa2AvQrw)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/06Xfa2AvQrw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
