# -*- coding: utf-8 -*-

import datetime
import os
import shutil

from invoke import task

CONFIG = {
    # Local path configuration
    "deploy_path": "public",
    # Github Pages configuration
    "github_pages_branch": "gh-pages",
    "commit_message": "'Publish site on {}'".format(datetime.date.today().isoformat()),
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])


@task
def build(c):
    """Build local version of site"""
    c.run("hugo")


@task
def serve(c):
    """Serve site locally (with drafts)"""
    c.run("hugo server -D")


@task
def publish(c):
    """Publish to production (minified)"""
    c.run("hugo --minify")


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    publish(c)
    c.run(
        "ghp-import -b {github_pages_branch} "
        "-m {commit_message} "
        "{deploy_path} -p".format(**CONFIG)
    )
