7.
from datetime import datetime as dt; print (dt.now())
import math
8.
def public_names(m):
    names = []
    for name in dir(m):
        if name[0] != '_':
            names.append(name)
    names.sort()
    return names
9.
def add_item(item, bag=None):
    if bag is None:
        bag = []
    bag.append(item)
    return bag
10.
import geometry 
print(geometry.circle.area(5))
print(geometry.rectangle.area(4, 6))







