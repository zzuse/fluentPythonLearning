from array import array
import reprlib
import math
import numbers
import functools
import operator

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




