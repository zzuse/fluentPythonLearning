def clip(text, max_len=80):
    """
    Return text clipped at the last space before or after max_len
    :param text:
    :param max_len:
    :return:
    """
    end=None
    if len(text) > max_len:
        space_before = text.rfind(' ',0,max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end=space_after
    if end is None:
        end=len(text)
    return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

from inspect import signature
sig = signature(clip)
print(sig)
for name,param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

print('-' * 20)
print('binding signature')

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

import inspect
sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard','src':'sunset.jpg', 'cls':'framed'}
bound_args = sig.bind(**my_tag)
print(bound_args)
for name, value in bound_args.arguments.items():
    print(name, '=', value)

del my_tag['name']
#bound_args = sig.bind(**my_tag)

print('-' * 20)
print('annotation clip')

def anno_clip(text:str, max_len:'int > 0'=80) -> str:
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

sig = signature(anno_clip)
print("annotation clip signature {}".format(sig.return_annotation))
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)

print('-' * 20)
print('fact')


from functools import reduce
from operator import mul


def fact1(n):
    return reduce(mul, range(1, n+1))

def fact2(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

print(fact1(5))
print(fact2(5))


print('-' * 20)
print('itemgetter')


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', '21.935', (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.43333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

print('-' * 20)
print('attrgetter')

from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
                for name, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])
print("metro_areas[0].coord.lat = {}".format(metro_areas[0].coord.lat))

from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

print('-' * 20)
print('operator methodcaller')

import operator
print([name for name in dir(operator) if not name.startswith('_')])

from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print("upcase(s) {}".format(upcase(s)))
hiphenate = methodcaller('replace', ' ', '-')
print("hiphenate(s) {}".format(hiphenate(s)))

print('-' * 20)
print('functools.partial')

from functools import partial
triple = partial(mul, 3)
print("triple(7) = {}".format(triple(7)))
a = list(map(triple, range(1, 10)))
print("list(map(triple, range(1, 10))) = {} ".format(a))

import unicodedata, functools
nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))

picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)