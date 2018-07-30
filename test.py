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

try:
    field_names = field_names.replace(',', ' ').split()
except AttributeError:
    pass
field_names = tuple(field_names)