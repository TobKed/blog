---
title: Model property in Django
date: '2019-02-03'
tags:
  - python
  - django
slug: django-model-property
summary: Model property in Django
categories:
  - Python
---

## Model property in Django

When you want to associate field with some function you can override save() method. Another convenient way to do this is to use Python property getter/setter to run some custom code. Important thing is that you don't have to run migrations to do this (if tables are not changed of course)

```python
class TestCase(models.Model):
    TEST_STATUS_CHOICES = (
        ("passed", "passed"),
        ("failed", "failed"),
        ("unknown", "unknown"),
        ("error", "error"),
    )

    _status = models.CharField(
        max_length=9, choices=TEST_STATUS_CHOICES, default="unknown", db_column="status"
    )

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in ["passed", "failed", "unknown"]:
            self._status = value
        else:
            self.scenario.status = "error"
            self._status = "error"
        self.save()
```

<br>

______________________________________________________________________

#### Sources:

- [@property - Python Documentation](https://docs.python.org/3.7/library/functions.html#property)
- [STAVROV'STUFF - How to replace a Django model field with a property](https://www.stavros.io/posts/how-replace-django-model-field-property/)
- [Corey Schafer - Property Decorators - Getters, Setters, and Deleters (youtube)](https://www.youtube.com/watch?v=jCzT9XFZ5bw)

{{<youtube-lite id="jCzT9XFZ5bw" title="Corey Schafer - Property Decorators - Getters, Setters, and Deleters (youtube)">}}
