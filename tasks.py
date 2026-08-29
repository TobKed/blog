# -*- coding: utf-8 -*-

import datetime
import os
import shutil
import sys

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
def rebuild(c):
    """`build` with the delete switch"""
    clean(c)
    build(c)


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run("hugo server -w")


@task
def serve(c):
    """Serve site locally"""
    c.run("hugo server")


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    c.run("hugo --minify")


@task
def publish(c):
    """Publish to production via rsync"""
    c.run("hugo --minify")
    # If rsync is still used, this preserves the original logic
    if "production" in CONFIG and "dest_path" in CONFIG:
        c.run(
            'rsync --delete --exclude ".DS_Store" -pthrvz -c '
            "{} {production}:{dest_path}".format(
                CONFIG["deploy_path"].rstrip("/") + "/", **CONFIG
            )
        )


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    preview(c)
    c.run(
        "ghp-import -b {github_pages_branch} "
        "-m {commit_message} "
        "{deploy_path} -p".format(**CONFIG)
    )
