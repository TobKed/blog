Title: Month summary - July 2021
Date: 2021-07-31
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2021, git
Slug: 2021-July-links
Summary: Interesting stuff from the month
Status: draft


# July 2021

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

During my work in the office I found out that many times the use of Git is discussed during quick chats or coffee breaks.
There is nothing wrong with this, however short discussions do not give space for deeper explanation or analysis.
I decided that a presentation about Git will fill this gap which resulted in **Brival Tech Talk - tips & tricks**.
I've expanded topics from my post on Git: [Changing history in Git]({filename}/posts/2019_08_12_git_change_history.md).

I talked about:
<ul>
    <li>git config </li>
    <li>pre-commit </li>
    <li>fast-forward or not </li>
    <li>git add --patch </li>
    <li>git commit -a, -m </li>
    <li>git adog </li>
    <li>git log master..@ </li>
    <li>git reflog </li>
    <li>git revert </li>
    <li>git commit --amend </li>
    <li>git rebase </li>
    <li>git rebase --interactive </li>
    <li>git rebase --interactive --autosquash --autostash </li>
    <li>git rebase --exec </li>
</ul>

I hope it is helpful and shows some less obvious ways of using Git.
I spent some significant time reading related articles and documentation.
I tested commands and concepts in the field as well because the presentation was conducted hand in hand with a live demo.
I found it helpful.

![Brival Tech Talk - tips & tricks]({static}/images/posts/brival_tech_talk_git.jpg)


## Articles

### [How to Study for Data-Structures and Algorithms Interviews at FAANG](https://medium.com/swlh/how-to-study-for-data-structures-and-algorithms-interviews-at-faang-65043e00b5df)

> I went from 0 → 100 in just a few months and I didn’t do anything special aside from studying consistently. That’s why I strongly believe any engineer can get good at these DS & Algo questions and get into F.A.A.N.G. or similar high paying roles.

### [How I Made a Giant Mistake with Terraform (and How Azure Made It Worse)](https://www.craigstuntz.com/posts/2021-07-08-how-i-made-a-giant-mistake-with-terraform.html)

> I made a huge mistake a while back, resulting in all preproduction environments being deleted from a client’s Azure subscription. That’s actually not so bad – we use terraform to create the environments, so we could just run the terraform again to put them back. And better preproduction than production, right? But Azure quirks and client rules made this considerably worse.

### [The 17 Ways to Run Containers on AWS](https://www.lastweekinaws.com/blog/the-17-ways-to-run-containers-on-aws/)

> As I mentioned on Twitter last week, there are 17 ways to run containers on AWS. While I pulled the number “17” out of the air, I have it on good faith that this caused something of a “meme explosion” inside of AWS.

### [Keeping your GitHub Actions and workflows secure: Preventing pwn requests](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/)

> TL;DR: Combining pull_request_target workflow trigger with an explicit checkout of an untrusted PR is a dangerous practice that may lead to repository compromise.

### [What I learned from Software Engineering at Google](https://swizec.com/blog/what-i-learned-from-software-engineering-at-google/)

> When I first picked up Software Engineering at Google I thought it was another one of those FAANG books full of lessons that make no sense at human scale. I was surprised, the lessons apply to teams as small as 5.

## Python

### [Python Type Hints - How to Avoid “The Boolean Trap”](https://adamj.eu/tech/2021/07/10/python-type-hints-how-to-avoid-the-boolean-trap/)

> “The Boolean Trap” is a programming anti-pattern where a boolean argument switches behaviour, leading to confusion. In this post we’ll look at the trap in more detail, and several ways to avoid it in Python, with added safety from type hints.

## Django

### [One Database Transaction Too Many](https://hakibenita.com/django-nested-transaction)

> How I told hundreds of users they got paid when they didn't!

### [PAGNIs: Probably Are Gonna Need Its](https://simonwillison.net/2021/Jul/1/pagnis/)

> Any of the ideas I’ve shown here could take an engineering team weeks (if not months) to add to an existing project—but with the right tooling they can represent just an hour (or less) work at the start of a project. And they’ll pay themselves off many, many times over in the future.

### [Efficient Pagination in Django and Postgres](https://pganalyze.com/blog/pagination-django-postgres)

> Django is an excellent framework for building web applications, but its default pagination method falls into this trap at scale. In this article, I’ll help you understand Django’s pagination limitations and offer three alternative methods that will improve your application’s performance. Along the way, you’ll see the tradeoffs and use cases for each method so you can decide which is the best fit for your application.

## Tools

### [calibre](https://github.com/kovidgoyal/calibre)

> calibre is an e-book manager. It can view, convert, edit and catalog e-books in all of the major e-book formats. It can also talk to e-book reader devices. It can go out to the internet and fetch metadata for your books. It can download newspapers and convert them into e-books for convenient reading. It is cross platform, running on Linux, Windows and macOS.

## Other stuff

### [MacOS setup](https://github.com/vol24pl/MacOS-setup)

> Scripts for setting up a brand new MacOS, and getting it ready to work in no time.

### [Survivorship bias](https://en.wikipedia.org/wiki/Survivorship_bias)

> Survivorship bias or survival bias is the logical error of concentrating on the people or things that made it past some selection process and overlooking those that did not, typically because of their lack of visibility. This can lead to some false conclusions in several different ways. It is a form of selection bias.
