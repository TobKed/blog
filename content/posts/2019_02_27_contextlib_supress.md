Title: Handling exceptions with contextlib
Date: 2019-02-27
Category: Python
Tags: python, exception, exceptions, context
Slug: contextlib-suppress
Summary: Handling exceptions with contextlib
Status: published

## Handling exceptions with contextlib.supress()

```python
import contextlib

with contextlib.suppress(FileNotFoundError):
    os.remove("somefile.tmp")
```

This is equivalent to the following try/except clause:

```python
try:
    os.remove("somefile.tmp")
except FileNotFoundError:
    pass
```

<br>

______________________________________________________________________

#### Sources:

- [Python Tricks Email series from RealPython.com ](https://realpython.com/)
