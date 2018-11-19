class Dog:
    def __init__(self, name, weight, owner):
        self.name = name
        self.weight = weight
        self.owner = owner

rex = Dog('Rex', 30, 'Bob')
print("rex {}\n----------".format(rex))

print("'spam'.__class__ {}\n----------".format('spam'.__class__))
print("str.__class__ {}\n----------".format(str.__class__))
from bulkfood_v6 import LineItem
print("LineItem.__class__ {}\n----------".format(LineItem.__class__))
print("type.__class__ {}\n----------".format(type.__class__))

import collections
import abc
print("collections.Iterable.__class__ {}\n----------".format(collections.Iterable.__class__))
print("abc.ABCMeta.__class__ {}\n----------".format(abc.ABCMeta.__class__))
print("abc.ABCMeta.__mro__ {}\n----------".format(abc.ABCMeta.__mro__))
