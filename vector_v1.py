from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools

class MySeq:
    def __getitem__(self, index):
        return index


s = MySeq()
print("s[1]\n{}\n----------".format(s[1]))
print("s[1:4]\n{}\n----------".format(s[1:4]))
print("s[1:4:2]\n{}\n----------".format(s[1:4:2]))
print("s[1:4:2, 9]\n{}\n----------".format(s[1:4:2, 9]))
print("s[1:4:2, 7:9]\n{}\n----------".format(s[1:4:2, 7:9]))
print("dir(slice)\n{}\n----------".format(dir(slice)))

print("slice(None, 10, 2).indices(5)\n{}\n----------".format(slice(None, 10, 2).indices(5)))

print("slice(-3, None, None).indices(5)\n{}\n----------".format(slice(-3, None, None).indices(5)))


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        # if len(self) != len(other):
        #     return False
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        # return True
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        # hashes = (hash(x) for x in self._components)
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a+b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

print("Vector([3.1, 4.2])\n{}\n----------".format(Vector([3.1, 4.2])))
print("Vector((3, 4, 5))\n{}\n----------".format(Vector((3, 4, 5))))
print("Vector(range(10))\n{}\n----------".format(Vector(range(10))))
v1 = Vector([3, 4, 5])
print("len(v1)\n{}\n----------".format(len(v1)))
print("v1[0], v1[-1]\n{} {}\n----------".format(v1[0], v1[-1]))
v7 = Vector(range(7))
print("v7[1:4]\n{}\n----------".format(v7[1:4]))
print("v7[-1]\n{}\n----------".format(v7[-1]))
print("v7[-1:]\n{}\n----------".format(v7[-1:]))
v = Vector(range(10))
print("vector has attribute v.x = {}".format(v.x))
print("v.y, v.z, v.t = {0}, {1}, {2}".format(v.y, v.z, v.t))
# print(v.b) # raise error
v = Vector(range(5))
print(v)
print("v.x\n{}\n----------".format(v.x))
v.A = 10
print("assign v.x to 10: \nv.x is {}\n----------".format(v.x))
print("tricky v is not changed: {}\n----------".format(v))
v1 = Vector([3, 4])
print("format(v1) {}\n----------".format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))
print("----------")
v3 = Vector([3, 4, 5])
print(format(v3))
print(format(Vector(range(7))))
print("----------")
print(format(Vector([1, 1]), 'h'))
print(format(Vector([1, 1]), '.3eh'))
print(format(Vector([1, 1]), '.5fh'))
print("----------")
print(format(Vector([1, 1, 1]), 'h'))
print(format(Vector([2, 2, 2]), '.3eh'))
print(format(Vector([0, 0, 0]), '.5fh'))
print("----------")
print(format(Vector([-1, -1, -1, -1]), 'h'))
print(format(Vector([2, 2, 2, 2]), '.3eh'))
print(format(Vector([0, 1, 0, 0]), '.5fh'))
print("----------")


print("functools.reduce 5! is {}\n----------".format(functools.reduce(lambda a,b: a*b, range(1, 6))))

n = 0
for i in range(1, 6):
    n ^= i

print("xor from 0 to 5 is {}\n----------".format(n))

print("functools.reduce(lambda a, b: a^b, range(6)) is {}\n----------".format(functools.reduce(lambda a, b: a^b, range(6))))

print("functools.reduce(operator.xor, range(6)) is {}\n----------".format(functools.reduce(operator.xor, range(6))))

print("zip(range(3), 'ABC') is {}\n----------".format(zip(range(3), 'ABC')))

print("list(zip(range(3), 'ABC')) is {}\n----------".format(list(zip(range(3), 'ABC'))))

print("list(zip(range(3), 'ABC', [0.0, 1.1, 2,2, 3.3])) is {} \n----------".format(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))))

from itertools import zip_longest
print("list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue = -1)) is {}\n----------".format(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue = -1))))

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
a = functools.reduce(lambda a, b: a+b[1], my_list, 0)
print("lambda sum second value {}".format(a))

import numpy as np
my_array = np.array(my_list)
a = np.sum(my_array[:, 1])
print("using numpy to sum second value {}".format(a))

a = functools.reduce(operator.add, [sub[1] for sub in my_list], 0)
print("using operator to sum second value {}".format(a))


import decimal
ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal('1')/decimal.Decimal('3')
print("decimal.Decimal('1')/decimal.Decimal('3')  = {}\n".format(one_third))
print("one_third = +one_third = {}\n".format(one_third == +one_third))
ctx.prec = 28
print("ctx.prec = 28 one_third = +one_third = {}\n-------------".format(one_third == +one_third))
print("+one_third= {}\n--------------".format(+one_third))

v1 = Vector([3, 4, 5])
v2 = Vector([6, 7, 8])
print(v1 + v2)
print(v1 + v2 == Vector([3+6, 4+7, 5+8]))

v1 = Vector([3, 4, 5])
print(v1 + (10, 20, 30))

from vector2d_v3 import Vector2d
v2d = Vector2d(1, 2)
print(v1 + v2d)

print((10, 20, 30) + v1)

from vector2d_v3 import Vector2d
v2d = Vector2d(1, 2)
print(v2d + v1)

print(v1 + 1)
print(v1 + 'ABC')