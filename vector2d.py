from array import array
import math


class Vector2d:
    # __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        print(type(self))
        class_name = type(self).__name__
        print(class_name)
        print('{}({!r}, {!r})'.format(class_name, *self))
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        print(ord(self.typecode))
        print(bytes([ord(self.typecode)]))
        print(array(self.typecode, self))
        print(bytes(array(self.typecode, self)))
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    """wrong"""
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)



v1 = Vector2d(3, 4)
print(v1.x,v1.y)
x, y=v1
print(x, y)
print(v1)
print(repr(v1))
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
print(v1)
print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))
print(format(Vector2d(1,1), 'p'))
print(format(Vector2d(1,1), '.3ep'))
print(format(Vector2d(1,1), '0.5fp'))

print(bytes(v1))
print(abs(v1))
print(bool(v1))
print(bool(Vector2d(0,0)))



v2_clone = Vector2d.frombytes(bytes(v1))
print(v2_clone)
v2 = Vector2d.frombytes(b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@')
print(v2)

print("*" * 20 + "classmethond and staticmethod")
class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())
print(Demo.klassmeth("spam"))
print(Demo.statmeth())
print(Demo.statmeth('spam'))

print("*" * 20 + "format function")

brl = 1/2.43
print(brl)
print(format(brl,'0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
print(format(42, 'b'))
print(format(2/3, '.1%'))


from datetime import datetime

now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))

print("*" * 20 + "angle")
print(Vector2d(0, 0).angle())
print(Vector2d(1, 0).angle())
epsilon = 10 ** -8
print(abs(Vector2d(0, 1).angle()-math.pi/2) < epsilon)
print(abs(Vector2d(1, 1).angle()-math.pi/4) < epsilon)

print("*" * 20 + "hashable function")
v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))
print(set([v1, v2]))
print(len(set([v1, v2])))

print("*" * 20 + "not immutable")

print(v1.__dict__)
v1._Vector2d__x = 7.0
print(v1)