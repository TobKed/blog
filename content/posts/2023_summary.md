Title: Year summary - 2023
Date: 2023-01-01
Category: summary
Tags: summary, year, 2023
Slug: 2023-summary
Summary: Ups and downs of 2023
Header_Cover: /images/posts/2023/2023_08_xx.jpg
Status: draft

# 2023

## Highlights

#### `git rebase --interactive` and `fixups`

Presented a well-received talk at work on mastering `git rebase --interactive` with a focus on `fixups`.
Inspired by [Raymond Hettinger](https://www.youtube.com/playlist?list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA) I decided to use the documentation generator [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
The presentation is available as a website under my domain: [tobked.dev/git_rebase_interactive](https://tobked.dev/git_rebase_interactive).
Its source is on my Github: [github.com/TobKed/git_rebase_interactive](https://github.com/TobKed/git_rebase_interactive).

![git rebase](https://tobked.dev/git_rebase_interactive/img/explain.png)

#### [Google Cloud Developer Day Warsaw 2023]({filename}/posts/2023_05_03_gcp_dev_day.md)

I attended Google Cloud Developer Day Warsaw 2023 on April 27th, 2023. It was a free event organized by Google Cloud at their [Warsaw Campus](https://www.campus.co/warsaw/).
I wrote more about it in a separate blog post: [Google Cloud Developer Day Warsaw 2023]({filename}/posts/2023_05_03_gcp_dev_day.md).

#### GitOps and [Flux](https://fluxcd.io/flux/)

I dived into the world of [flux](https://fluxcd.io/flux/), a game-changer for GitOps deployments.
This powerful tool automates keeping your Kubernetes cluster in sync with your **git** configuration.
It goes beyond just watching for changes in configuration files - Flux can also identify new Docker images and update both configurations and the cluster itself.
Learning Flux has been a blast, and it's a valuable addition to my DevOps toolkit.

#### Taking ML Pipelines to Production: Journey with Kubeflow and Vertex Pipelines

I embarked on a journey to automate and streamline my machine learning workflows.
Kubeflow Pipelines, a powerful open-source platform allows for building and managing complex ML pipelines, encompassing everything from data ingestion to model training and deployment.

The real magic happened when I integrated Kubeflow Pipelines with Vertex Pipelines on Google Cloud.
Vertex Pipelines is a managed service that makes running Kubeflow Pipelines in a production environment a breeze.
This powerful combination allowed me to successfully deploy and run ML pipelines in production, ensuring scalability and reliability.

By leveraging Kubeflow Pipelines and Vertex Pipelines, I've gained the ability to automate ML workflows, improve their reproducibility, and confidently run them in a production setting.
This has significantly boosted my machine learning development efficiency.

#### Google Cloud and Pycon CZ 2023 presentation

One of the highlights was diving deep into [Google Cloud Platform (GCP)](<(https://cloud.google.com/?hl=en)>) to build a highly scalable application.
[CloudRun](https://cloud.google.com/run) streamlined code deployment, while **Cloud SQL** (PostgreSQL) provided a robust and scalable foundation for my app's data.
[PubSub](https://cloud.google.com/pubsub) messaging became a game-changer, decoupling APIs for independent scaling and boosting overall performance.
A load balancer added the finishing touch, ensuring smooth traffic distribution and regional optimization.
Seeing the app handle traffic peaks with minimal latency was incredibly rewarding.

I had the pleasure of attending the incredible [PyCon CZ](https://cz.pycon.org/2023/) conference in Prague.
The excitement began even before I arrived in Prague, as I had the chance to meet John and Judy from the USA during my train journey.
John, a retired programmer, shared stories of his work with natural language, SQL-Windows, and COBOL.
It felt like I was meeting a living legend!

During the train ride, I also had the pleasure of getting to know Piotr, the organizer of [PyKonik](https://www.pykonik.org/).
The conference itself was a fantastic experience, with a multitude of great people and captivating presentations.

One of the best moments of the conference for me was when I put myself on the list for the Lightning Talks.
This was a huge challenge for me as I am usually quite nervous when it comes to public speaking, but I was determined to push myself out of my comfort zone.
The title of my presentation was "**ML (Fast)API below 100ms (on GCP)**".
The presentation, as well as all the resources related to it, can be found in [my repository](https://github.com/TobKed/fastapi_cloudrun_pubsub).
I have provided an end-to-end working example on Google Cloud that demonstrates how to defer load from FastAPI (served by [CloudRun](https://cloud.google.com/run)) to a background worker (also on CloudRun) via a queueing system ([PubSub](https://cloud.google.com/pubsub)).
After practicing my presentation numerous times in my hotel room, I finally stepped onto the stage and gave it my all.
It was a personal victory over my fear of public speaking.

![PyCon CZ.]({static}/images/posts/2023/2023_09_pyconcz.jpg)

[Python API and background workers on Google Cloud Platform repo](https://github.com/TobKed/fastapi_cloudrun_pubsub)

## Writing

I wanted to improve my writing skills so since March I have been writing monthly summaries where I am trying to compile
a few sentences about the last month together with articles, tools and other interesting materials I came across.

Every month is decorated with picture made by me.

2023 summaries:

- [January]({filename}/posts/2023_01_30_january_links.md)
- [February]({filename}/posts/2023_02_28_february_links.md)
- [March]({filename}/posts/2023_03_31_march_links.md)
- [April]({filename}/posts/2023_04_30_april_links.md)
- [May]({filename}/posts/2023_05_31_may_links.md)
- [June]({filename}/posts/2023_06_30_june_links.md)
- [July]({filename}/posts/2023_07_31_july_links.md)
- [August]({filename}/posts/2023_08_31_august_links.md)
- [September]({filename}/posts/2023_09_30_september_links.md)
- [October]({filename}/posts/2023_10_31_october_links.md)
- [November]({filename}/posts/2023_11_30_november_links.md)
- [December]({filename}/posts/2023_12_31_december_links.md)

I also wrote one additional blog posts:

- [Google Cloud Developer Day Warsaw 2023]({filename}/posts/2023_05_03_gcp_dev_day.md)

## Summary

This year has been a fantastic journey of learning, pushing boundaries, and contributing to the programming community.
I'm excited to see what the next year holds!

## Photos

![2023_01]({static}/images/posts/2023/2023_01_xx.jpg)

![2023_04]({static}/images/posts/2023/2023_05_gcp_dev_day/2023_05_gcp_dev_day.jpg)

![2023_05]({static}/images/posts/2023/2023_05_xx.jpg)

![2023_06]({static}/images/posts/2023/2023_06_xx.jpg)

![2023_07]({static}/images/posts/2023/2023_07_xx.jpg)

![2023_08]({static}/images/posts/2023/2023_08_xx.jpg)

![2023_09]({static}/images/posts/2023/2023_09_xx.jpg)

![2023_10]({static}/images/posts/2023/2023_10_xx.jpg)

![2023_11]({static}/images/posts/2023/2023_11_xx.jpg)

![2023_12]({static}/images/posts/2023/2023_12_xx.jpg)
