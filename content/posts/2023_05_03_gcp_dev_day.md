Title: Google Cloud Developer Day Warsaw 2023
Date: 2023-05-03
Category: cloud
Tags: cloud, developer, google, gcp, 2023
Slug: google-cloud-developer-day-warsaw-2023
Summary: My notes from Google Cloud Developer Day Warsaw 2023
Header_Cover: /images/posts/2023/2023_05_gcp_dev_day/2023_05_gcp_dev_day.jpg
Status: published

# Google Cloud Developer Day Warsaw 2023

I attended Google Cloud Developer Day Warsaw 2023 on April 27th, 2023. It was a free event organized by Google Cloud at their [Warsaw Campus](https://www.campus.co/warsaw/).
It was a full-day event with 12 presentations.
I attended all of them and found all of them to be very interesting.
Especially mind-blowing was the showcase of AI capabilities.
I chose just a few of them to write down my notes.
I picked them since they are related to my current work and I found them interesting.

[TOC]

### Service to Service Communication with Serverless ([Christoph Grotz](https://christoph-grotz.medium.com/))

Christoph presented how to use Envoy to communicate between two instances of Cloud Run with minimal overhead of authentication and authorization.
No JWT, no headers, no tokens. Just plain HTTP requests.
In a very simple example, the only change between the local setup and cloud environments is the URL of the service.
Moreover, the URL for the cloud environment is the same for different environments like staging, testing, production.
Correct routing is done by the service mesh.

### Code-centric IaC with Pulumi (Artur Kuliński)

Artur presented Pulumi - a tool for Infrastructure as Code.
I am a huge fan of IaC and have been using Terraform for a while now.
I had heard about Pulumi before, but I never had a chance to try it.
It is especially interesting since Pulumi uses "regular" programming languages like Python, which seems more natural to me than HCL.
Now, I am definitely going to give it a try after what I saw.

### Secrets and Serverless (Anna Muscarella)

Anna gave a great presentation about how to manage secrets in a serverless environment.
She presented different approaches and their pros and cons.
In short, there are three approaches:

- environment variables
- volume mounts
- secret manager

While environment variables are the easiest to use, they are not the most secure for obvious reasons I will not mention here.
Volume mounts are also not the best practice and sometimes cumbersome to use or even not supported by some services.
The best way to manage secrets is to use a secret manager within your app so secrets are not exposed to the environment.

I used this approach in my [repository](https://github.com/TobKed/django_on_gcp) and [blog post]({filename}/posts/2021_12_30_django_on_gcp.md) where I showed how to run [Django application on Google Cloud Platform]({filename}/posts/2021_12_30_django_on_gcp.md).
As you can see below, secrets are pulled from [Google Secret Manager](https://cloud.google.com/secret-manager) if the app is running on Google Cloud Platform.
In my case, they are pulled only during app initialization, so to use the latest secret, you need to restart the app.
For the sake of simplicity, the secrets with the `latest` tag are used. However, it may not be the best fit for the production environment where we want to pin the version of the secret.

```python
import io
import os
from pathlib import Path

import environ
from google.cloud import secretmanager

BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env(DEBUG=(bool, False))
env_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(env_file):
    env.read_env(env_file)
# Pull secrets from Google Secret Manager
elif os.environ.get("GOOGLE_CLOUD_PROJECT", None):
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")
    env.read_env(io.StringIO(payload))
else:
    raise Exception("No local .env or GOOGLE_CLOUD_PROJECT detected. No secrets found.")
```

Here is the link to the code which I used in my example: [github.com/TobKed/django_on_gcp/blob/master/mysite/settings.py#L14](https://github.com/TobKed/django_on_gcp/blob/4e25321d856f09a15a58f54cc273abf1e879126d/mysite/settings.py#L14)

### From Prototype to Production: Going Faster on Cloud Run (Roman Seibel)

Roman made promoting the app between different environments as easy as a piece of cake.
Tt was astonishing.
Now, I am an even bigger fan of Cloud Run.

## Extras

### `gcurl`

`gcurl` is a nice alias for `curl` that allows for quick hitting of Google Cloud endpoints with authorization using your gcloud [identity token](https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token):

```shell
gcurl='curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json"'
```

### [music by Rytmik](https://soundcloud.com/rytmikmusic)

At the lounge area, there was a DJ named Rytmik playing some delightful house music. You can check out his music on [soundcloud.com/rytmikmusic](https://soundcloud.com/rytmikmusic) and [mixcloud.com/Rytmik](https://www.mixcloud.com/Rytmik/).

![Rytmik]({static}/images/posts/2023/2023_05_gcp_dev_day/2023_05_gcp_dev_day_rytmik.jpg)

### Links

- [Cloud Developer Day - Warsaw](https://inthecloud.withgoogle.com/cloud-developer-days-warsaw-23/register.html#agenda)
- [Google for Startups - Warsaw Campus](https://www.campus.co/warsaw/)
- [Service Weaver](https://serviceweaver.dev/)
- [github.com/ServiceWeaver/weaver](https://github.com/ServiceWeaver/weaver)
- [GKE Policy Automation](https://github.com/google/gke-policy-automation)
- [Auditing GKE Clusters across the entire organization - blog post](https://cloud.google.com/blog/topics/developers-practitioners/auditing-gke-clusters-across-entire-organization)
- [github.com/liquibase/liquibase-bigquery](https://github.com/liquibase/liquibase-bigquery)
- [Continuously deploy your apps AND data? Let’s try to use Liquibase for BigQuery changes - blog post](https://seroter.com/2022/11/17/continuously-deploy-your-apps-and-data-lets-try-to-use-liquibase-for-bigquery-workloads/)
- [github.com/GoogleCloudPlatform/cloud-run-mesh](https://github.com/GoogleCloudPlatform/cloud-run-mesh)
- [Envoy - an open source edge and service proxy, designed for cloud-native applications](https://www.envoyproxy.io/)

## Summary

It was a great event, and I am looking forward to the next one. I learned a lot of new things and met interesting people. Great job Google Cloud team!
