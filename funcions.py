print("------------factorial------------")
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(42))

print(factorial.__doc__)
print(type(factorial))
fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))
print(list(map(fact, range(11))))
print(dir(factorial))

print("------------sorted------------")

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key = len))


def reverse(word):
    return word[::-1]


print(sorted(fruits, key=reverse))
print(sorted(fruits, key=lambda word: word[::-1]))


print("------------map filter reduce------------")

print(list(map(fact,range(6))))
print([fact(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))

print("------------callable---------------")
print([callable(obj) for obj in (abs, str, 13)])
print("------------bingo---------------")

import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))

print("-----------function and class object difference--------")
class C: pass
obj= C()
def func(): pass
print("dir(func):{}".format(set(dir(func))))
print("dir(obj):{}".format(set(dir(obj))))
print("dir(func)-dir(obj):{}".format(sorted(set(dir(func)) - set(dir(obj)))))

print("-----------function and class object difference--------")


def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class']=cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str=''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name="img"))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))

def f(a,*,b):
    return a,b

print(f(1,b=2))
