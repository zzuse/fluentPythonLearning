import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7','diamonds')
print("beer_card {}\n----------".format(beer_card))

deck = FrenchDeck()

print("len(deck) {}\n----------".format(len(deck)))

print("deck[0] {}\n----------".format(deck[0]))

print("deck[-1] {}\n----------".format(deck[-1]))

print("choice(deck) {}\n----------".format(choice(deck)))

print("deck[:3] {}\n----------".format(deck[:3]))

print("deck[12::13] {}\n----------".format(deck[12::13]))

print("every cards")
for card in deck:
    print(card)

print("every cards reversed:")
for card in reversed(deck):
    print(card)
print(" {}\n----------".format(""))

print("Card('Q','hearts') in deck {}\n----------".format(Card('Q','hearts') in deck))

print()
print("Card('7','beasts') in deck {}\n----------".format(Card('7','beasts') in deck))


suit_values = dict(spades=3 ,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) +suit_values[card.suit]

print("sorted {}\n----------".format(""))
for card in sorted(deck,key = spades_high):
    print(card)