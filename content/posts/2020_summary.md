Title: Year summary - 2020
Date: 2020-12-31
Category: summary
Tags: summary, year, 2020
Slug: 2020-summary
Summary: Year summary
Header_Cover: /images/posts/2020_summary.png
Status: draft


# 2020

Last year was extraordinary for obvious reasons. 
Shifting work from office to remote overnight, uncertainty about the future.
It impacted all of us, however I think despite all of these things it was a great year. 
I made a not exactly chronological list of my personal highlights of the year.


## Developing backend for [**Her impact**](https://herimpact.co/)

I participated in the creation of a web platform which empowers female entrepreneurs. 
I co-authored the backend in Django where we made a REST API to communicate with the frontend written in the React JS framework.
We used Google Kubernetes Engine for deployment and Google Cloud Storage for file storage. 
It was a great adventure to make it alive in a quite short period of time. I am happy to see that the website works smoothly and is being visited by many users.

[**Her Impact** on Bēhance.net](https://www.behance.net/gallery/94053021/Her-Impact-self-development-app-for-women)


## Privacy concerns
2020 was the year to address all sorts of privacy related issues. 

I participated in the development of Polish COVID-19 application [ProteGO](https://github.com/ProteGO-Safe) in its early days.
The noble idea was to help people to live in a normal way in times of the pandemic.
The concept was that mobile apps will emit anonymous identifiers by bluetooth and other app users could pick and collect them all together with the signal strength.
When a person is diagnosed with COVID-19 the identifiers from their app that were announced to other users could be sent to the server. Then other users may download identifiers of infected people and compare them with a saved collection of close contacts. If there is a match, information about possible infection or quarantine will be presented. 
The App attracted government attention and after some time it drifted in the direction which filled me with privacy concerns. It is not hard to imagine that if these identifiers were not so anonymous it may be possible to track people in a way I could not agree with. 
I decided to follow my inner voice and not contribute to this project anymore.
The project was continued and paid by the government authorities and its history was overwritten so there is even no sign of my early contributions to it.
I do not know what is the current state of the project as I do not follow it anymore.


## Increased Google Cloud Platform competencies

I became interested in improving competencies related to the cloud. Early in June I became Google Cloud Associate Certified Engineer.
While studying for the certificate I finished a series of tutorials on Qwiklabs and Coursera platforms. 
It solidified my knowledge about the Google Cloud Platform.

![Google Cloud Associate Engineer]({static}/images/posts/gcp_ace.png)

[Google Cloud Associate Engineer](https://www.credential.net/d47b7596-251f-45ac-8a54-4cf6d8c5a286?key=f4eed8bc7e2f25d6b2a9315f31e1a20dd7cd5ecc93caff78eb55feeafcc6be70).

[**Qwiklabs profile**](https://www.qwiklabs.com/public_profiles/102aba17-a972-4e32-865b-0e3626420e5a).

**Coursera** accomplishments:

 * [Google Cloud Platform Fundamentals: Core Infrastructure](https://www.coursera.org/account/accomplishments/verify/PLPFK2SMEHM6)
 * [Essential Google Cloud Infrastructure: Foundation](https://www.coursera.org/account/accomplishments/verify/HJMSSXPASHXX)
 * [Elastic Google Cloud Infrastructure: Scaling and Automation](https://www.coursera.org/account/accomplishments/verify/VFK3U45L8HY6)
 * [Essential Google Cloud Infrastructure: Core Services](https://www.coursera.org/account/accomplishments/verify/JJH7V2MHMKYD)
 * [Getting Started with Google Kubernetes Engine](https://www.coursera.org/account/accomplishments/verify/HAA7U93T9M9X)

In relation to the cloud infrastructure I got familiar with the idea of  _Infrastructure As Code_ and a well known tool for it, [Terraform](https://www.terraform.io/). I wrote a blog post about it: 
[Terraform Tutorial: Introduction to Infrastructure as Code](https://www.polidea.com/blog/terraform-tutorial-introduction-to-infrastructure-as-code/)


## Open Source: Apache Airflow, Apache Beam, Github Actions

I contributed to two Open Source projects: [Apache Beam](https://github.com/apache/beam) and [Apache Airflow](https://github.com/apache/airflow).

In Apache Beam I introduced GitHub Actions workflows where Java and Python cross platform test suites are being executed. 
Previously an external repository was responsible for building Python wheels. 
I introduced Github Actions workflow which builds Python wheels for Linux, Mac and Windows platforms and integrated it with the release process.

Since I was familiar with Beam, it was a natural path for me to take care of integration with [Google Dataflow](https://cloud.google.com/dataflow) In Apache Airflow (
[1](https://github.com/apache/airflow/pull/11167), [2](https://github.com/apache/airflow/pull/11374), [3](https://github.com/apache/airflow/pull/11501), [4](https://github.com/apache/airflow/pull/11726), [5](https://github.com/apache/airflow/pull/12039), [6](https://github.com/apache/airflow/pull/12249)).

In 2021, I am planning to introduce Apache Beam operators to Airflow.

My adventure with GitHub Actions resulted in creation of my own actions:

 - [github-forks-sync-action](https://github.com/TobKed/github-forks-sync-action) - GitHub Action to synchronise forks
 - [label-when-approved-action](https://github.com/TobKed/label-when-approved-action) - Label When Approved is an action that checks is Pull Request is approved and assign label to it. Label is not set or removed when Pull Request has awaiting requested changes.

TODO

[fetch-apache-ga-stats](https://github.com/TobKed/fetch-apache-ga-stats) - For The Apache Software Foundation [ASF] the limit for concurrent jobs in GitHub Actions [GA] equals 180 (usage limits). The GItHub does not provide statistics related to GA.
   


## Writing

I wanted to improve my writing skills so since March I have been writing monthly summaries where I am trying to compile a few sentences about the last month together
with articles, tools and other interesting materials I came across.

2020 summaries:

 - [March](https://tobked.github.io/blog/2020-march-links.html)
 - [April](https://tobked.github.io/blog/2020-april-links.html)
 - [May](https://tobked.github.io/blog/2020-may-links.html)
 - [June](https://tobked.github.io/blog/2020-june-links.html)
 - [July](https://tobked.github.io/blog/2020-july-links.html)
 - [August](https://tobked.github.io/blog/2020-august-links.html)
 - [September](https://tobked.github.io/blog/2020-september-links.html)
 - [October](https://tobked.github.io/blog/2020-october-links.html)
 - [November](https://tobked.github.io/blog/2020-november-links.html)
 - [December](https://tobked.github.io/blog/2020-december-links.html)

I also wrote a few blog posts that were published on the company website (reposted on Medium):

- [What’s New in Python 3.9—A Summary of New Features](https://tobiaszkedzierski.medium.com/whats-new-in-python-3-9-a-summary-of-new-features-e82dda07e85a)
- [Terraform Tutorial: Introduction to Infrastructure as Code](https://tobiaszkedzierski.medium.com/terraform-tutorial-introduction-to-infrastructure-as-code-dccec643bfdb)
- [What Is Python Used For? Most Popular Uses](https://tobiaszkedzierski.medium.com/what-is-python-used-for-most-popular-uses-a0c1019bac25)
- [What’s New in Python 3.8—A Summary of the New Features](https://tobiaszkedzierski.medium.com/whats-new-in-python-3-8-a-summary-of-the-new-features-a2b68bd7b81d)


## Promoted to regular

My growth did not go unseen, and I was promoted from Junior to Regular Software Engineer position.

## Serving at Vipassana meditation center

I participated in Vipassana course as server during 10 days course.

> Vipassana, which means to see things as they really are, is one of India's most ancient techniques of meditation.
> Vipassana is a way of self-transformation through self-observation. 
> It focuses on the deep interconnection between mind and body, which can be experienced directly by disciplined attention to the physical sensations that form the life of the body, and that continuously interconnect and condition the life of the mind.

> The technique of Vipassana Meditation is taught at ten-day residential courses during which participants learn the basics of the method, and practice sufficiently to experience its beneficial results.
> There are no charges for the courses - not even to cover the cost of food and accommodation. 
> All expenses are met by donations from people who, having completed a course and experienced the benefits of Vipassana, wish to give others the opportunity to also benefit.

Serving at a Vipassana meditation retreat is a way to give back to the organization. 

Learn more about Vipassana on [dhamma.org](https://www.dhamma.org/)

## Beskidy

![Beskidy photo]({static}/images/posts/beskidy/DSC03290.png)

![Beskidy photo]({static}/images/posts/beskidy/DSC03307.png)

![Beskidy photo]({static}/images/posts/beskidy/DSC03339.png)
