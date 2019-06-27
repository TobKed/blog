Title: Enum and dataclass
Date: 2019-06-23
Category: Python
Tags: python, branching, vcs
Slug: enum-and-dataclass
Summary: Few words about enum and dataclass


### Enum

> "An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over."
>
> -- <cite>https://docs.python.org/3/library/enum.html</cite>

```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
str(Color.RED)                  # -> 'Color.RED'
print(repr(Color.RED))          # -> '<Color.RED: 1>'
type(Color.RED)                 # -> <enum 'Color'>
isinstance(Color.GREEN, Color)  # -> True
print(Color.RED.name)           # -> RED


# iteration
for color in Color:
    print(color)
                                # -> Color.RED
                                # -> Color.GREEN
                                # -> Color.BLUE

# access
Color(1)                        # -> <Color.RED: 1>
Color(3)                        # -> <Color.BLUE: 3>
Color['RED']                    # -> <Color.RED: 1>
Color['GREEN']                  # -> <Color.GREEN: 2>

member = Color.RED 
member.name                     # -> 'RED'
member.value                    # -> 1
```


### Data Class

```python
@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```
Will add, among other things, a __init__() that looks like:
```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int=0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
```


Sources:

* [enum — Support for enumerations - Python Documentation](https://docs.python.org/3/library/enum.html)

* [dataclasses — Data Classes - Python Documentation](https://docs.python.org/3/library/dataclasses.html)

* [Cool New Features in Python 3.7 #Data Classes - realpython.com](https://realpython.com/python37-new-features/#data-classes)

* [The Ultimate Guide to Data Classes in Python 3.7 - realpython.com](https://realpython.com/python-data-classes/)
