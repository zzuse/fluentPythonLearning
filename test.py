a = 3
b = 4
a, b = b, a
print(a)
print(b)


class Foo:
    def __getitem__(self, pos):
        return range(0,30,10)[pos]

f = Foo()
print(f[1])
for i in f: print(i)

print(20 in f)
print(15 in f)

from random import shuffle
l = list(range(10))
shuffle(l)
print(l)

from frenchdeck import FrenchDeck

deck = FrenchDeck()

def set_card(deck, position, card):
    deck._cards[position] = card

# monkey patching
FrenchDeck.__setitem__ = set_card
print(len(deck))
shuffle(deck)
print(deck[:5])


def record_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):  # <3>
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):  # <4>
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):  # <5>
        values = ', '.join('{}={!r}'.format(*i) for i
                           in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__=field_names,  # <6>
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)

    return type(cls_name, (object,), cls_attrs)