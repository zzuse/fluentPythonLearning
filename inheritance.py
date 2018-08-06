class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppelDict(one=1)
print(dd)

dd['two'] = 2
print(dd)

dd.update(three=3)
print(dd)

class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict(a='foo')
print(ad['a'])
d = {}
d.update(ad)
print(d['a'])
print(d)

import collections
class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppelDict2(one = 1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)

class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict2(a='foo')
print(ad['a'])
d = {}
d.update(ad)
print(d['a'])
print(d)


class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):
    def ping(self):
        # A.ping(self)
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()
print(d.ping())
d.pong()
C.pong(d)

print(D.__mro__)
print(d.pingpong())

print('bool.__mro__\n{}\n----------'.format(bool.__mro__))


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))
print_mro(bool)

from frenchdeck2 import FrenchDeck2
print_mro(FrenchDeck2)
import numbers
print_mro(numbers.Integral)
import io
print_mro(io.BytesIO)
print_mro(io.TextIOWrapper)
import tkinter
print_mro(tkinter.Text)