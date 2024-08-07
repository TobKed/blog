Title: git: when ignorance is a bliss
Date: 2024-06-04
Category: programming
Tags: git, programming
Slug: declutter-git-status
Summary: Focus on what matters: decluterring `git status`
Header_Cover: /images/posts/2024/2024_06_04_declutter_git_status.jpg
Status: published

## Focus on what matters: decluterring `git status`

The saying "ignorance is bliss" might hold some truth in everyday life, but in the world of **git** version control, a cluttered terminal output can be a major headache.
A tidy `git status` command output is heplful for smooth and efficient development.

This post explores some helpful commands that will empower you to manage untracked files and selectively track changes within your `git` repositories.

## Focusing on tracked files

By default, the `git status` command displays both tracked files (those already added to the Git index) and untracked files (those not yet added).
However, there might be times when you only care about changes to existing tracked files.
For instance, I've encountered projects where the list of untracked files can take up the entire terminal screen!
In such situations, where you primarily focus on existing files and desire a clutter-free overview, the following commands come in handy:

```bash
git status --untracked-files=no
git status -uno
```

These commands display the status of your tracked files but conveniently hide untracked files from the output.

If you frequently prefer a clean `git status` output, you can configure **git** to hide untracked files by default:

- `git config --global status.showUntrackedFiles no`: this sets the preference **globally** for all your **git** repositories.
- `git config --local status.showUntrackedFiles no`: this sets the preference for the current repository only, allowing for project-specific configurations.

## Marking files for skipping changes

There might be times when you have files in your working directory that you don't want **git** to track for changes. This command helps with that:

```bash
git update-index --assume-unchanged <filename>
```

This command instructs **git** to assume that the specified files (e.g., `docker-compose.yml`, `Dockerfile`) are unchanged, even if their content is modified.
This can be useful for configuration files that might be adjusted only for your local environment or files managed by external tools.

Knowing which files are marked as assumed-unchanged can be helpful. Use this command to list them:

```bash
git ls-files -v | grep '^h'
```

- `git ls-files -v`: This command lists all files managed by **git**, including their status codes.
- `grep '^h'`: This filters the output to show only lines starting with the letter `h`, which indicates assumed-unchanged files.

If you decide to track changes in a previously assumed-unchanged file, you can reverse the effect using:

```bash
git update-index --no-assume-unchanged <filename>
```

To efficiently remove all files from `assume-unchanged` status, you can combine these commands into a single pipeline:

```bash
git ls-files -v | grep '^h' | awk '{print $2}' | xargs git update-index --no-assume-unchanged
# or if you don't like xargs
git update-index --no-assume-unchanged $(git ls-files -v | grep '^h' | awk '{ORS=" "} {print $2}')
```

**Commands list:**

```bash
# add
git update-index --assume-unchanged docker-compose.yml Dockerfile

# list
git ls-files -v | grep '^h'

# remove
git update-index --no-assume-unchanged docker-compose.yml Dockerfile

# bulk remove
git ls-files -v | grep '^h' | awk '{print $2}' | xargs git update-index --no-assume-unchanged
# or
git update-index --no-assume-unchanged $(git ls-files -v | grep '^h' | awk '{ORS=" "} {print $2}')
```

## Summary

By mastering these commands, you can effectively hide clutter in your **git** status output and selectively exclude specific files from version control.
This keeps your `git status` focused on the changes that truly matter, promoting a clean and efficient workflow.
