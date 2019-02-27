Title: Handling exceptions with contextlib
Date: 2019-02-27
Category: Python
Tags: python, exception, exceptions, context
Slug: contextlib-suppress
Summary: Handling exceptions with contextlib


### Handling exceptions with contextlib.supress()

```python
import contextlib

with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')
```

This is equivalent to the following try/except clause:
 
```python
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass have ever used ```{% request %}``` or ```{% debug %}``` you can easily wrap your head around this concept.
```


Sources:

* [Python Tricks Email series form RealPython.org ](https://realpython.com/)
