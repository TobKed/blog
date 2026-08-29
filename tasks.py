# -*- coding: utf-8 -*-

import os
import shutil

from invoke import task

CONFIG = {
    # Local path configuration
    "deploy_path": "public",
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])


@task
def build(c):
    """Build local version of site"""
    c.run("hugo --gc")


@task
def serve(c):
    """Serve site locally at http://localhost:1313 (with drafts)"""
    # -M renders to memory: without it the server serves public/ from disk, so a
    # concurrent build overwrites it with production (blog.tobked.dev) URLs.
    c.run("hugo server -D -M")


@task
def publish(c):
    """Build production version of site (deploys happen in CI)"""
    c.run("hugo --gc --minify")
    c.run("npx -y pagefind --site {deploy_path}".format(**CONFIG))
