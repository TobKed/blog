Title: Git branching
Date: 2019-02-13
Category: Git
Tags: git, branching, vcs
Slug: git-branching
Summary: Git branching


### Git branching

I want to present you how do I perform branching. When I develop some feature I am used to create branch for it to separate it from master. When I decide I am satisfied with the changes and some chapter is finished feature branch shall be merged into master. At the beginning I had the problem with merging because when it's done directly it squash commits from feature branch into master.

```shell   
# | *   (feature) new feature finish
# | *   (feature) new feature in progress
# | *   (feature) new feature start
# |/
# *     (master)  initial commit

$ git checkout master
$ git merge feature branch

# *   (feature) new feature finish
# *   (feature) new feature in progress
# *   (feature) new feature start
# |
# *     (master)  initial commit
```

To keep it separate no-fast-forward option come in handy. It also creates new commit.

```shell   
$ git checkout master
$ git merge --no-ff feature branch

# *     (master)  merge branch feature
# |\
# | *   (feature) new feature finish
# | *   (feature) new feature in progress
# | *   (feature) new feature start
# |/
# *     (master)  initial commit
```

What if want to develop this feature without creating new branch?

```shell   
$ git checkout feature
$ git commit -m "polishing"

# | *   (feature) polishing
# * |   (master)  update readme
# * |   (master)  merge branch feature
# |\|
# | *   (feature) new feature finish
# | *   (feature) new feature in progress
# | *   (feature) new feature start
# |/
# *     (master)  initial commit
```

What happened? Feature branch does not know what is going in master. Maybe someone should tell her before? Rebase! Let's rewind.

```shell   
$ git checkout feature
$ git rebase master
$ git commit -m "polishing"

# | *   (feature) polishing
# |/
# *     (master)  update readme
# *     (master)  merge branch feature
# |\ 
# | *   (feature) new feature finish
# | *   (feature) new feature in progress
# | *   (feature) new feature start
# |/
# *   
```

I hope it helps to you to keep your ducks in a row.

Sources:

* [A successful Git branching model - Vincent Driessen blog](https://nvie.com/posts/a-successful-git-branching-model/)
