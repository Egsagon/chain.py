# chain.py
Chained lists in python

This is a very simple module that allows you to have a chained list in python, aka a list that loops over when the index is bigger than its lenght.
It works just like a simple list for the other features.

### Features

```python
from chain import Chain

# Initialisation
li = Chain([1, 2, 3])

# Printing out an element
print(li[10])

# Slices also work
print(li[1:100])
print(li[1:100:4])
```
