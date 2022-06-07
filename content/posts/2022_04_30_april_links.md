Title: Month summary - April 2022
Date: 2022-04-30
Category: summary
Tags: python, blog, podcast, series, aggregate, summary, month, 2022
Slug: 2022-april-links
Summary: Interesting stuff from the month
Status: draft

# April 2022

I am aggregating here some more or less interesting stuff of various IT related materials which I came across this month.
Some of them are strictly related to the things I did or am currently doing.

## Some thoughts

At the begging of month I attended workshops called ["Scrapowanie danych publicznych w Pythonie (Scraping public data in Python)"](https://medialabkatowice.eu/wydarzenia/scrapowanie-danych-publicznych-w-pythonie/).
During the first part we created simple scrapers to fetch some data from chosen websites. They lack many features like error handling or throttling. During second part we wrote them with [scrapy](https://github.com/scrapy/scrapy) which was pretty awesome because with just few adjustments we employed very nice framework which handles a lot stuff for us, like logging, storing data, following logs, error handling, throttling etc. Big thanks to [Paweł Miech](https://pawelmhm.github.io/) who conducted this amazing workshop. Materials are available on his github [github.com/pawelmhm/warsztaty-medialab](https://github.com/pawelmhm/warsztaty-medialab)

The biggest part of the month was consumed by Google Cloud Platform \[GCP\]. Almost two years ago I passed the Google Cloud Associate Certified Engineer certification exam and I thought April is a good time to improve and confirm my increasing competencies with Google Cloud Platform. I read tons of GCP documentation, and websites.I did some udemy courses and completed very good book [Official Google Cloud Certified Professional Cloud Architect Study Guide by Dan Sullivan](https://www.goodreads.com/book/show/53001024-official-google-cloud-certified-professional-cloud-architect-study-guide),  I played with the GCP infra as well to get practical experience with topics which I did not use so far. After all, I was happy to read on screen in the certification center that I passed the exam. I am especially proud because it was one of the hardest certification exams so far. I learned a lot not only from a technical perspective but also from a business point of view.

![Google Professional Cloud Architect]({static}/images/posts/2022/gcp_pca.png)

[Google  Professional Cloud Architect](https://www.credential.net/fc647c87-e199-4dd2-b34e-67dbb7bc3d10#gs.2gfa5j).

## Articles

### [Cargo Cult Software Engineering](https://stevemcconnell.com/articles/cargo-cult-software-engineering/)

> > In the South Seas there is a cargo cult of people. During the war they saw airplanes with lots of good materials, and they want the same thing to happen now. So they’ve arranged to make things like runways, to put fires along the sides of the runways, to make a wooden hut for a man to sit in, with two wooden pieces on his head for headphones and bars of bamboo sticking out like antennas—he’s the controller—and they wait for the airplanes to land. They’re doing everything right. The form is perfect. It looks exactly the way it looked before. But it doesn’t work. No airplanes land. So I call these things cargo cult science, because they follow all the apparent precepts and forms of scientific investigation, but they’re missing something essential, because the planes don’t land.
>
> — Richard Feynman

### [4 ways we use GitHub Actions to build GitHub](https://github.blog/2022-04-05-4-ways-we-use-github-actions-to-build-github/)

> From automating builds and releases to taking care of large-scale regression testing, here are a few ways we use GitHub Actions to build GitHub.

### [Hexagonal Architecture, there are always two sides to every story](https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c)

> The Hexagonal or Ports and Adapters Architecture, is not the silver bullet for all applications. It involves a certain level of complexity, that when handled with care, will bring great benefits to your system. But if broken windows are allowed, it might cause a lot of headaches.

### [BBC Online — A year with serverless](https://medium.com/bbc-design-engineering/bbc-online-a-year-with-serverless-ffc2ae474277)

> In this post I reflect on our progress so far, and some of the interesting challenges we are facing while building the BBC’s critical digital services.

### [Things I Use: Zsh - Just Abrahms](https://justin.abrah.ms/dotfiles/zsh.html#sec-2-7)

> Nice bash / zsh config explained. Source files are on gh: [justinabrahms/jlilly-bashy-dotfiles](https://github.com/justinabrahms/jlilly-bashy-dotfiles)

### [Exit Interviews Are a Trap](https://jacobian.org/2022/apr/4/exit-interviews-are-a-trap/)

> Exit interviews are a trap. Unless you know you’re immune, don’t walk into the trap.

### [Take Your Github Repository To The Next Level 🚀️](https://dev.to/eludadev/take-your-github-repository-to-the-next-level-17ge)

> I’ve been using Github for a very long time now, and along the way I’ve been gathering a step-by-step guide on creating the perfect Github repository. If you haven’t guessed already, this article is an enhanced version of that guide.

### [Writing for Engineers](https://www.heinrichhartmann.com/posts/writing/)

> Writing is key to have impact in large organizations. As a senior software engineer chances are that writing is the most important skill you have to acquire in order to increase your scope beyond the team and advance your career.

## Python

### [Does elegance matter? | Pydon't 🐍](https://mathspp.com/blog/pydonts/does-elegance-matter)

> “How do we convince people that in programming simplicity and clarity – in short: what mathematicians call "elegance" – are not a dispensable luxury, but a crucial matter that decides between success and failure?”
>
> ― Edsger W. Dijkstra, "Selected Writings on Computing: A Personal Perspective", p347.

### [Providing Multiple Constructors in Your Python Classes](https://realpython.com/python-multiple-constructors/#constructing-dictionaries-from-keys)

> Sometimes you need to write a Python class that provides multiple ways to construct objects. In other words, you want a class that implements multiple constructors. This kind of class comes in handy when you need to create instances using different types or numbers of arguments. Having the tools to provide multiple constructors will help you write flexible classes that can adapt to changing needs.

### [Bite-sized refactoring | Pydon't 🐍](https://mathspp.com/blog/pydonts/bite-sized-refactoring)

> In this Pydon't I show you why refactoring is important and show you how to do it in little steps, so that it doesn't become too overwhelming.

### [Futures and easy parallelisation](https://wrongsideofmemphis.com/2022/02/17/futures-and-easy-parallelisation/)

> Here is one small snippet that it’s very useful when dealing with quick scripts that perform slow tasks and can benefit from running in parallel.

### [20 Python Interview Questions To Challenge Your Knowledge](https://towardsdatascience.com/20-python-interview-questions-to-challenge-your-knowledge-cddc842297c5)

> A peek into data structures, programming concepts, and best practices

### [A Tour of Python's itertools Library](https://www.blog.pythonlibrary.org/2021/12/07/a-tour-of-pythons-itertools-library/)

> The tools provided by itertools are fast and memory efficient. You will be able to take these building blocks to create your own specialized iterators that can be used for efficient looping.

### [10 must-know patterns for writing clean code with Python🐍 ](https://dev.to/alexomeyer/10-must-know-patterns-for-writing-clean-code-with-python-56bf)

> Python is one of the most elegant and clean programming languages, yet having a beautiful and clean syntax is not the same as writing clean code.

### [fstring.help/](https://fstring.help/)

> Python fstring reference.

## Django

### [How to Make Django Raise an Error for Missing Template Variables](https://adamj.eu/tech/2022/03/30/how-to-make-django-error-for-undefined-template-variables/)

> It’s all too easy to forget to pass a variable to your template, or make a typo in a variable name. Unfortunately, it can be quite hard to debug such mistakes, since Django’s default behaviour is to ignore the problem and render an empty string.

### [You Probably Don’t Need Django’s `get_user_model()`](https://adamj.eu/tech/2022/03/27/you-probably-dont-need-djangos-get-user-model/)

> In most Django code, you do not need to use get_user_model(), and you can instead use a vanilla import.

### [Awesome Django Blogs](https://github.com/theArjun/awesome-django-blogs)

> List of blogs about Django and related technologies.

### [Permissions in Django](https://testdriven.io/blog/django-permissions/)

> In this article, we'll look at how to assign permissions to users and groups in order to authorize them to perform specific actions.

## Python libraries

### [fastapi-events](https://github.com/melvinkcx/fastapi-events/)

> Asynchronous event dispatching/handling library for FastAPI and Starlette

### [structlog](https://github.com/hynek/structlog)

> 'structlog' makes logging in Python faster, less painful, and more powerful by adding structure to your log entries.

### [bpython](https://github.com/bpython/bpython)

> [bpython](https://github.com/bpython/bpython) is a lightweight Python interpreter that adds several features common to IDEs. These features include syntax highlighting, expected parameter list, auto-indentation, and autocompletion.s

## Django libraries

## Go

## Tools

### [dependency-review-action](https://github.com/actions/dependency-review-action)

> A GitHub Action for detecting vulnerable dependencies in your PRs.

### [Snyk GitHub Actions](https://github.com/snyk/actions)

> A set of GitHub actions for checking your projects for vulnerabilities

### [delta](https://github.com/dandavison/delta)

> A syntax-highlighting pager for git, diff, and grep output

### [agones](https://github.com/googleforgames/agones)

> Dedicated Game Server Hosting and Scaling for Multiplayer Games on Kubernetes.

## Cloud

### [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

> Bootstrap Kubernetes the hard way on Google Cloud Platform. No scripts.

## Other stuff

### [Ivaylo Durmonski](https://durmonski.com/)

> Run exclusively by [Ivaylo Durmonski](https://durmonski.com/about/) and supported by [Library members](https://durmonski.com/membership/), the goal of this site is simple: Rigorous production of easily digestible writing to save people from drowning in chaotic information.

### [mermaid](https://github.com/mermaid-js/mermaid)

> Generation of diagram and flowchart from text in a similar manner as markdown.

### [No Code](https://github.com/kelseyhightower/nocode)

> No code is the best way to write secure and reliable applications. Write nothing; deploy nowhere.

### [justinabrahms/jlilly-bashy-dotfiles](https://github.com/justinabrahms/jlilly-bashy-dotfiles)

> This is a collection of my dotfiles not related to either vim or emacs. Mostly just bashy stuff.

### [Brendan Gregg's Homepage](https://www.brendangregg.com/index.html)

> G'Day. I use this site to share and bookmark various things, mostly my work with computers. While I currently work on large scale cloud computing performance at Netflix, this site reflects my own opinions and work from over the years.

### [Julia Evans blog](https://jvns.ca/)

> Hey! I'm Julia. Welcome to my blog. Here's every post I've ever written, organized by category. Enjoy!

### [jmutai/dotfiles](https://github.com/jmutai/dotfiles)

> My dotfiles collection used on Arch Linux box

## Podcasts

## Videos

<iframe title="Luke at Monerotopia: Crypto for Dystopia Avoidance" src="https://videos.lukesmith.xyz/videos/embed/57e9e226-c143-4608-ac39-3c0f7444dd0f" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups" width="560" height="315" frameborder="0"></iframe>

### [The Missing Semester of Your CS Education - Lecture 4: Data Wrangling (2020)](https://www.youtube.com/watch?v=sz_dsktIjt4)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/sz_dsktIjt4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [SysOps/DevOps Online MeetUp #51 - \[#347\] "Jest GIT!" - Michał Wierba](https://www.youtube.com/watch?v=WXOzggTMHck)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/WXOzggTMHck" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [Andy Baio: Cut, copy, paste](https://www.youtube.com/watch?v=9tmT80kW9Co)

<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/9tmT80kW9Co" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [](https://www.youtube.com/watch?v=VIDEO_ID)

> Playback on other websites has been disabled by the video owner. [Watch on YouTube](https://www.youtube.com/watch?v=VIDEO_ID)
