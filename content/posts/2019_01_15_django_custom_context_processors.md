---
title: Custom context processors in Django
date: '2019-01-15'
tags:
- python
- django
slug: django-custom-context-processors
summary: Custom context processors in Django
status: published
categories:
- Python
---
## Custom context processors in Django

In order to get the content out of database in the template the best way is usually a template tag (you can write your own template tags). However, when you want a particular variable to be available in the context of every template, creating a custom context processor could be a convenient way to achieve this.
If you have ever used `{% request %}` or `{% debug %}` you can easily wrap your head around this concept.

First, we write simple context processors.

```python
# my_app/my_context_processor.py
from datetime import datetime


def custom_context(request):
    return {"hello": "Hello World!"}


def another_custom_context(request):
    right_now = datetime.now().strftime("%b %d %Y %H:%M:%S")
    return {
        "bye": "Bye Bye!",
        "bye_user": f"Bye Bye {request.user}!",
        "right_now": right_now,
    }
```

Next, go to `settings.py` and append the context processors to the context_processors list in the templates options.

```python
# mysite/settings.py
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # add your custom context processors here
                "my_app.my_context_processor.custom_context"
                "my_app.my_context_processor.another_custom_context",
            ],
        },
    },
]
```

And there we are. We can enjoy our custom context processors!

```jinja2
{# myapp/templates/myapp/page.html #}
<p> {{ hello }} <p>
<p> {{ bye }} <p>
<p> {{ bye_user }} <p>
<p> Right now: {{ right_now }} <p>
```

They will be rendered as below.

```html
<p> Hello World! <p>
<p> Bye Bye! <p>
<p> Bye Bye AnonymousUser! <p>
<p> Right now: Jan 05 2019 18:10:25 <p>
```

<br>

______________________________________________________________________

#### Sources:

- [Django Documentation - Writing your own context processor](https://docs.djangoproject.com/en/2.1/ref/templates/api/#writing-your-own-context-processors)
