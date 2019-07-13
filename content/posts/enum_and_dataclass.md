Title: Enum and dataclass
Date: 2019-06-23
Category: Python
Tags: python, enum, dataclass, data, OOP
Slug: enum-and-dataclass
Summary: Few words about enum and dataclass


### Enum

> "An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over."
>
> -- <cite>https://docs.python.org/3/library/enum.html</cite>

`Enum` is useful when you need immutable name-value pairs enclosed in an iterable object.
What is special in `Enum`? Its metaclass `EnumMeta` provides dunder methods *(dunder methods: double underscores at the beginning and the end, also called magic methods)* which allow to use `Enum` class which will fail on a typical class. 

The `Enum` class is callable, providing the following functional API:
```python
>>> Cards = Enum('Cards', ['clubs', 'diamonds', 'hearts', 'spades'])
>>> Cards
<enum 'Cards'>
>>> Cards.clubs                     
<Cards.clubs: 1>
>>> Cards.clubs.name                
'clubs'
>>> Cards.clubs.value               
1
>>> isinstance(Cards.clubs, Cards)
True 
```

```python
# __iter__
>>> list(Cards)                     
[<Cards.clubs: 1>, <Cards.diamonds: 2>, <Cards.hearts: 3>, <Cards.spades: 4>]
>>> for card in Cards:
        print(card)
        
Cards.clubs
Cards.diamonds
Cards.hearts
Cards.spades

# __len__
>>> len(Cards)
# 4

# __contains__
>>> 'spades' in Cards 
False
>>> 4 in Cards 
False
>>> Cards.spades in Cards 
True

# __dir__  notice that member names are in definiton order
>>> dir(Cards)['__class__', '__doc__', '__members__', '__module__', 'clubs', 'diamonds', 'hearts', 'spades']
```

Class syntax:
```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
```python    
>>> repr(Color.RED))
'<Color.RED: 1>'
>>> type(Color.RED)          
<enum 'Color'>

# access
>>> Color(1)        # __call__ method is invoked
<Color.RED: 1>
>>> Color(3)
<Color.BLUE: 3>
>>> Color['RED']
<Color.RED: 1>
>>> Color['GREEN']
<Color.GREEN: 2>

>>> member = Color.RED 
>>> member.name                     
'RED'
>>> member.value                    
1
```


### Dataclasses



> "Data Classes can be thought of as "mutable namedtuples with defaults."
>
> -- <cite>https://www.python.org/dev/peps/pep-0557/#abstract</cite>

Dataclasses were introduced in Python3.7 (PEP 557). They provide elegant syntax for creating mutable data holder objects.
They are based on `attrs` package "    that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods)."


```python
from dataclasses import dataclass, asdict, astuple, replace

@dataclass
class Color:
    hue: int
    saturation: float
    lightness: float = 0.5
```
```
# __init__
>>> c = Color(33, 1.0)
>>> c
Color(hue=33, saturation=1.0, lightness=0.5)

>>> c.hue
33
>>> c.saturation
1.0
>>> c.lightness
0.5

>>> replace(c, hue=120)
Color(hue=120, saturation=1.0, lightness=0.5)
>>> asdict(c)
{'hue': 33, 'saturation': 1.0, 'lightness': 0.5}
>>> astuple(c)
(33, 1.0, 0.5)
```


Dataclass by default generates special methods like:  `__init__`, `__doc__`, `__eq__`.

Some additional methods are created as well: `__annotations__`, `__dataclass_fields__`, `__dataclass_params__`.

Default values are treated as class variables.

```python
# __doc__
>>> Color.__doc__
'Color(hue: int, saturation: float, lightness: float = 0.5)'

# __repr__
>>> repr(c)
'Color(hue=33, saturation=1.0, lightness=0.5)'

# __eq__
>>> Color(12, 2) == Color(12, 2)

# defaults as class variable
>>> Color.lightness
0.5
>>> Color.hue
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Color' has no attribute 'hue'

# __annotations__
>>> Color.__annotations__
{'hue': <class 'int'>, 'saturation': <class 'float'>, 'lightness': <class 'float'>}

# __dataclass_params__
>>> Color.__dataclass_params__
_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)

# __dataclass_fields__
>>> Color.__dataclass_fields__
{'hue': Field(
    name='hue',
    type=<class 'int'>,
    default=<dataclasses._MISSING_TYPE object at 0x7f69fcc428d0>,
    default_factory=<dataclasses._MISSING_TYPE object at 0x7f69fcc428d0>,
    init=True,
    repr=True,
    hash=None,
    compare=True,
    metadata=mappingproxy({}),
    _field_type=_FIELD),
'saturation': Field(
    name='saturation',
    type=<class 'float'>,
    default=<dataclasses._MISSING_TYPE object at 0x7f69fcc428d0>,
    default_factory=<dataclasses._MISSING_TYPE object at 0x7f69fcc428d0>,
    init=True,
    repr=True,
    hash=None,
    compare=True,
    metadata=mappingproxy({}),
    _field_type=_FIELD),
'lightness': Field(
    name='lightness',
    type=<class 'float'>,
    default=0.5,
    default_factory=<dataclasses._MISSING_TYPE object at 0x7f69fcc428d0>,
    init=True,
    repr=True,
    hash=None,
    compare=True,
    metadata=mappingproxy({}),
    _field_type=_FIELD)
}
```

If default dataclass does not suit you, you can easily modify it by passing parameters to dataclass decorator (init, repr, order, unsafe_hash, frozen).

```python
from pprint import pprint

@dataclass(order=True, frozen=True)
class Color:
    hue: int
    saturation: float
    lightness: float = 0.5
```
```python
>>> colors = [Color(5, 5.9), Color(1, 2.5), Color(1, 2.5), Color(3, 4.1)]

>>> pprint(sorted(colors))
[Color(hue=1, saturation=2.5, lightness=0.5),
 Color(hue=1, saturation=2.5, lightness=0.5),
 Color(hue=3, saturation=4.1, lightness=0.5),
 Color(hue=5, saturation=5.9, lightness=0.5)]


 >>> pprint(set(colors))
 {Color(hue=1, saturation=2.5, lightness=0.5),
  Color(hue=3, saturation=4.1, lightness=0.5),
  Color(hue=5, saturation=5.9, lightness=0.5)}
```

#### Custom fields

* field factories - instance of collection, instead of fixed default value
* custom methods - no different than for any other class
* limiting hashing  - limit to immutable fields by `field(hash=False)`
* limiting field which are displayed - `field(repr=False)`
* limiting for comparison - if dataclass has an `oredr=True` all fileds are included in comparison. Exclusion of filed is provided by `filed(compare=False)`
* metadata - more informations about the field, e.g. `salary = field(metadata={'units': 'bitcoin'})`
```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(order=True, unsafe_hash=True)
class Employee:
    emp_id: int = field()
    name: str = field()
    gender: str = field()
    salary: int = field(hash=False, repr=False, metadata={'units': 'bitcoin'})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, viewer_id):
        self.viewed_by.append((viewer_id, datetime.now()))
```
```python
>>> from pprint import pprint

>>> e1 = Employee(emp_id='12345',
>>>               name="Rachel Green",
>>>               gender='female',
>>>               salary = 20,
>>>               age = 20
>>> )

>>> e2 = Employee(emp_id='67890',
                  name="Ross From Friends",
                  gender='male',
                  salary = 30,
                  age = 30
    )

>>> e1.access('Changler Bing')
>>> e1.access('Joey T.')
>>> pprint(e1.viewed_by)
[('Changler Bing', datetime.datetime(2019, 7, 8, 19, 49, 58, 706455)),
 ('Joey T.', datetime.datetime(2019, 7, 8, 19, 49, 58, 706458))]

>>> pprint(sorted([e1, e2]))
[Employee(emp_id='12345', name='Rachel Green', gender='female', age=20),
 Employee(emp_id='67890', name='Ross From Friends', gender='male', age=30)]

>>> assignments = {e1: 'be pretty', e2: 'be anxious'}
>>> pprint(assignments)
{Employee(emp_id='12345', name='Rachel Green', gender='female', age=20): 'be pretty',
 Employee(emp_id='67890', name='Ross From Friends', gender='male', age=30): 'be anxious'}


>>> (fields(e1)[3])
Field(name='salary',
      type=<class 'int'>,
      default=<dataclasses._MISSING_TYPE object at 0x7fc094c06e80>,
      default_factory=<dataclasses._MISSING_TYPE object at 0x7fc094c06e80>,
      init=True,
      repr=False,
      hash=False,
      compare=True,
      metadata=mappingproxy({'units': 'bitcoin'}),
      _field_type=_FIELD
)
```

Sources:  
* [enum — Support for enumerations - Python Documentation](https://docs.python.org/3/library/enum.html)  
* [dataclasses — Data Classes - Python Documentation](https://docs.python.org/3/library/dataclasses.html)  
* [Cool New Features in Python 3.7 #Data Classes - realpython.com](https://realpython.com/python37-new-features/#data-classes)  
* [The Ultimate Guide to Data Classes in Python 3.7 - realpython.com](https://realpython.com/python-data-classes/)  
* [PEP 557 -- Data Classes](https://www.python.org/dev/peps/pep-0557/)  
* [attrs: Classes Without Boilerplate](https://github.com/python-attrs/attrs)  
* [Raymond Hettinger - Dataclasses: The code generator to end all code generators - PyCon 2018](https://www.youtube.com/watch?v=T-TwcmT6Rcw)  
