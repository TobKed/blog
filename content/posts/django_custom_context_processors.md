Title: Custom context processors in Django
Date: 2019-01-05
Category: Python
Tags: python, django
Slug: django-custom-context-processors
Summary: Custom context processors in Django


### Custom context processors in Django


```python
# mysite/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'my_app.my_context_processor.custom_context'
                'my_app.my_context_processor.another_custom_context'
            ],
        },
    },
]
```

```python
# my_app/my_context_processor.py
def custom_context(request):
    return {"hello": "Hello World!"}
    
def another_custom_context(request):
    return {
        "bye": "Bye Bye!",
        "bye_user": f"Bye Bye {request.user}!"
    }
```

```jinja2
{# myapp/templates/myapp/page.html #}
<p> {{ hello }} <p>
<p> {{ bye }} <p>
<p> {{ bye_user }} <p>
```

```html
<p> Hello World! <p>
<p> Bye Bye! <p>
<p> Bye Bye AnonymousUser! <p>
```

[Django Documentation - Writing your own context processor](https://docs.djangoproject.com/en/2.1/ref/templates/api/#writing-your-own-context-processors)
