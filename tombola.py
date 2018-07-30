import abc
import random


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random"""

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class Fake(Tombola):
    def pick(self):
        return 13

class Struggle:
    def __len__(self): return 23



class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


from collections import abc
print('isinstance(Struggle(), abc.Sized)\n{}\n----------'.format(isinstance(Struggle(), abc.Sized)))
print('issubclass(Struggle, abc.Sized)\n{}\n----------'.format(issubclass(Struggle, abc.Sized)))

Tombola.register(TomboList)
print('issubclass(TomboList, Tombola)\n{}\n----------'.format(issubclass(TomboList, Tombola)))
t = TomboList(range(100))
print('isinstance(t, Tombola)\n{}\n----------'.format(isinstance(t, Tombola)))
print('TomboList is not inherited from Tombola -- TomboList.__mro__\n{}\n----------'.format(TomboList.__mro__))


TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'

import doctest

def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()
    virtual_subclasses = list(Tombola._abc_registry)
    print(real_subclasses + virtual_subclasses)
    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)

def test(cls, verbose=False):
    print("*******************"*10 + cls.__name__)
    res = doctest.testfile(TEST_FILE, globs={'ConcreteTombola': cls},
                           verbose=verbose,
                           optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))

if __name__ == '__main__':
    import sys
    main(sys.argv)

# python3 tombola.py -v