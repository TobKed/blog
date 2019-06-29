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

Enum is useful when you need immutable name-value pairs enclosed in an iterable object.


The Enum class is callable, providing the following functional API:
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

What is special in Enum? It's metaclass EnumMeta provides dunder methods *(dunder methods: double underscores at the beginning and the end, also called magic methods)* which allow to use Enum class which will fail on a typical class. 

```python
# __iter__
>>> list(Cards)                     
[<Cards.clubs: 1>, <Cards.diamonds: 2>, <Cards.hearts: 3>, <Cards.spades: 4>]
>>> for card in Cards:
>>>     print(card)
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
>>> from enum import Enum
>>> class Color(Enum):
>>>     RED = 1
>>>     GREEN = 2
>>>     BLUE = 3
    
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
