---
title: Handling exceptions with contextlib
date: '2019-02-27'
tags:
  - python
  - exception
  - exceptions
  - context
slug: contextlib-suppress
summary: Handling exceptions with contextlib
status: published
categories:
  - Python
---

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
