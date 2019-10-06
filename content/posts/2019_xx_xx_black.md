Title: Black
Date: 2019-10-07
Category: python
Tags: python, pep8
Slug: black
Summary: Python code formatter
Status: draft
Header_Cover: /images/posts/black-cover.png


## Author

The author of Black is Łukasz Langa, Pythonista from Poznań in Poland.
He is a Python core developer and Python 3.8 release manager.

## Black

A PEP-8 is a just style guide so there are many ways, which are correct, to format the same part of the code.

```python
class GoogleCloudBaseHook(BaseHook):
    def __init__(self, gcp_conn_id: str = 'google_cloud_default', delegate_to: Optional[str] = None) -> None:
        pass
        
class GoogleCloudBaseHook(BaseHook):
    def __init__(self,
                 gcp_conn_id: str = 'google_cloud_default',
                 delegate_to: Optional[str] = None) -> None:
        pass

class GoogleCloudBaseHook(BaseHook):
    def __init__(
        self,
        gcp_conn_id: str = 'google_cloud_default',
        delegate_to: Optional[str] = None) -> None:
        pass

class GoogleCloudBaseHook(BaseHook):
    def __init__(
        self,
        gcp_conn_id: str = 'google_cloud_default',
        delegate_to: Optional[str] = None
    ) -> None:
        pass
```

Linters give the information which part of a code violates PEP-8, but they do not give any solutions.
Usually it is quite easy to fix it, but it is annoying and consumes time.
It leaves space for opinionated discussions.
The good formatter can help a lot in this matter.

> Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.
> 
> -- black documentation

Black uses subset of PEP-8 as a code style where every decision was preceded with discussion, supported by solid arguments and concrete parts of PEP-8.
Under the hood code is parsed to Concrete Syntax Tree (CST) and Abstract Syntax Tree (AST). You can learn more about this concepts from sources at the end of text.

#### Pros:
* Fast.
* Deterministic.  
  _When run multiple times, result will be always the same._
+ Save time during review.  
  _No more discussions about where line should be broken._
+ Code reading is easier.  
  _As Uncle Bob said, code is read ten times more often than written. Due to this fact, when code is styled in consistent way (
  and Black provides consistent output) it minimizes effort while reading it. You can fully focus on syntax and logic, and not on style._
+ No additional (unneseccary?) refactoring during coding.  
  _During working on some part of code sometimes you may want to change (and sometimes you do it) some adjecent
  areas which are not well formatted (at least you think they are not). Black get rids off this additional refactors._
+ Minimal configuration.

#### Cons:
* Requires python 3.6+.  
  _Older versions can be formatted but for working version 3.6+ is required._
* Does not touch strings.  
  _Long strings will never be broken._
* Does not touch imports.
* Sometimes it is PITA to configure with ISORT.
* Still in beta.

### Using Black

#### Install Black

To use it out of the box:
```bash
pip install black
black {source_file_or_directory}
```
Do you want to format Python by using Python? Uno problemo:
```python
import black

black.format_file_in_place(
    "path/to/file.py,
    mode=black.FileMode(line_length=110),
    fast=False,
    write_back=black.WriteBack.YES,
)
```
<br>

#### pyproject.toml

If you need change sensible defaults you can do it by defining them in `pyproject.toml` file (this file is described in <nobr>PEP-518</nobr>).

Example `pyproject.toml`:
```toml
[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'
exclude = '''

(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  | foo.py           # also separately exclude a file named foo.py in
                     # the root of the project
)
'''
```
<br>

#### pre-commit

If you don't use pre-commit in your projects, you should start using it immediately. Pre-commit framework makes configuring
pre-commit hooks pleasant and convenient. Hook for Black parses files to be commited and if any of them changed during it, hook fails and prevents commit to be done. It means the code was not compliant with the code style.
Drawback of this is that you have to add to staging area formatted files and run commit command again.

Example `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/ambv/black
    rev: 19.3b0
    hooks:
      - id: black
        name: Formats python files using black
        language_version: python3.6
```
<br>

#### PyCharm/IntelliJ IDEA - External Tools

In IDE you can define handful external tools which are available in `Tools -> External Tool` and under right-click menu.

![External Tools with Black]({static}/images/posts/black-external-tool.png)


**Install black and check where locate installation folder.**

```bash
pip install black
which black
```

**Set External Tool in IDE.**

On macOS:

```PyCharm -> Preferences -> Tools -> External Tools```

On Windows / Linux / BSD:

```File -> Settings -> Tools -> External Tools```

**Click the + icon to add a new external tool.**

Official documentation suggests the following values:

```
Name: Black
Description: Black is the uncompromising Python code formatter.
Program: <install_location_from_step_2>  
Arguments: "$FilePath$"  
```

I personally modified them to better suits my needs:

Version which reads settings from project `pyproject.toml` is same as above with addtional `Working Directory` property:

```
Working directory: $ProjectFileDir$
```
  
Version with specific line length:

```
Arguments: "$FilePath$" --line-length 110
```
  

#### File-watcher in IDE


<br>

----------------
#### Sources:
* [black](https://github.com/psf/black)
* [black playground](https://black.now.sh/)
* [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PEP 518 - Specifying Minimum Build System Requirements for Python Projects](https://www.python.org/dev/peps/pep-0518/)
* [The latest with BLACK, so you can stop worrying about Formatting - Łukasz Langa - PyBay 2019](https://youtu.be/nnKvBwRt72Q)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%"' src="https://www.youtube.com/embed/nnKvBwRt72Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
* [Paint it black - wdrożenie autoformatera - Marcin Jaroszewski - PyWaw #87](https://youtu.be/GymkJlqaD3Q)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%"' src="https://www.youtube.com/embed/GymkJlqaD3Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
* [Emily Morehouse-Valcarcel - The AST and Me - PyCon 2018](https://youtu.be/XhWvz4dK4ng)
<div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
    <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%"' src="https://www.youtube.com/embed/XhWvz4dK4ng" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
* [Understanding and using Python's AST - Episode #152 - talkpython.fm](https://talkpython.fm/episodes/show/152/understanding-and-using-python-s-ast)
* [Abstract vs. Concrete Syntax Trees - Eli Bendersky's website](https://eli.thegreenplace.net/2009/02/16/abstract-vs-concrete-syntax-trees/)
* [pre-commit](https://pre-commit.com/)