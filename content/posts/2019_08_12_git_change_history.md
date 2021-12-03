Title: Changing history in Git
Date: 2019-08-19
Category: Git
Tags: git, vcs
Slug: git-history
Summary: Fix mistakes and clean git repository
Status: published

## Changing history

Many times when working with Git you want change something in the history and Git is great about that.
I strongly recomend to read [Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
You can find there information how to use `git ammend` and `git rebase --interactive` (`git rebase -i`) commands.
By using them you can change the last commit, the order of the commits, the messages or modify files in a commit,
squash together or split them apart, or remove some of them entirely.

### What and why?

I wanted to present how I rewrite history, which commands do I use and how do I configure Git for it.

### Setting up Git

Here are some Git settings which are useful during rewriting history:

- `git config --global merge.ff false`

> By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to false, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the --no-ff option from the command line)."
>
> -- <cite>[merge.ff - Git documentation](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeff)</cite>

- `git config --global rebase.autostash true`

> "When set to true, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts."
>
> -- <cite>[rebase.autostash - Git documentation](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseautoStash)</cite>

- `git config --global rebase.autosquash true`\
  this one is very important because it is useful for `fixups` which I use a lot.

> "If set to true enable --autosquash option by default."
>
> -- <cite>[rebase.autosquash - Git documentation](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseautoSquash)</cite>

### Amending

As the previously mentioned article says, amending is used for changing the last commit. You do it by adding changes to the staging area and executing:

```bash
git commit --amend
```

It loads previous command message where you can make changes. After saving the message it makes it your new last commit. Be careful because amending changes SHA1 of the commit.
I use it a lot but usually I don't want to edit the message, hence one of my most favorite command:

```bash
git commit --amend --no-edit
```

### Interactive rebasing

I will not discuss interactive rebasing in details due the fact that it has a great description in the Git documentation so I hope you are already familiar with it.
A `git rebase -i` as a parameter takes the parent of the last commit to be edited.
Usually I don't mind to performing interactive rebasing on all commits on a given branch so to do this I pass as a parameter the parent branch e.g.

```bash
git rebase -i master
```

### Fixup

You made a few commits already but you found there is a bug in the second commit.
It will be much more convenient to fix this second commit than to create another one.
You can do this by making a commit with changes and then, during interactive rebasing you can choose the `f` or `fixup` action for the fixup commit and move it in the todo list below the commit you want to fix.

It can be done even better by using my other favourite command, the `git commit --fixup`.
As an argument it takes the SHA1 of commit to be fixed-up.
Initially, a commit will be added and the message will be the same as the message of the commit to be fixed-up with the suffix `fixup!`.
During interactive rebasing, this commit will be put in order after the commit to be fixed-up with option `fixup`, so it saves a little bit of your time and energy for reordering and editing it manually.
My workflow for fixup usually looks like that:

```bash
git add -u
git commit --fixup bas341d
git rebase -i master   # add --autosquash when rebase.autosquash is not set to true
```

The important thing is that for making it without adding the `--autosquash` argument you should set `rebase.autosquash` in configuration to _true_ (as I mentioned in <b>Setting up Git</b> section).
In case you want to edit the commit message you can use `git commit --squash` as well.

<br>

______________________________________________________________________

#### Sources:

- [Git homepage](https://git-scm.com/)
- [Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
- [merge.ff - Git documentation](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeff)
- [rebase.autostash - Git documentation](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseautoStash)
- [rebase.autosquash - Git documentation](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseautoSquash)
- [Git autostash - praqma.com](https://www.praqma.com/stories/git-autostash/)
- [Auto-squashing - thoughtbot](https://thoughtbot.com/blog/autosquashing-git-commits)
