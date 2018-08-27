import re
import reprlib
import itertools

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


    # method 1
    # def __iter__(self):
    #     return SentenceIterator(self.words)

    # method 2
    def __iter__(self):
        for word in self.words:
            yield word
        return


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


s = Sentence('"The time has come," the Walrus said,')
print(s)
for word in s:
    print(word)

print(list(s))

print(s[5])


class Foo:
    def __iter__(self):
        pass


from collections import abc
print(issubclass(Foo, abc.Iterable))
f = Foo()
print(isinstance(f, abc.Iterable))

s = 'ABC'
for char in s:
    print(char)

s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break


s3 = Sentence('Pig and Pepper')
it = iter(s3)
print("it {}\n----------".format(it))
print("next(it) {}\n----------".format(next(it)))
print("next(it) {}\n----------".format(next(it)))
print("next(it) {}\n----------".format(next(it)))
print("list(it) {}\n----------".format(list(it)))
print("list(iter(s3)) {}\n----------".format(list(iter(s3))))


def gen_123():
    yield 1
    yield 2
    yield 3

print(gen_123())

for i in gen_123():
    print(i)

g = gen_123()
print(next(g))
print(next(g))
print(next(g))

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

for c in gen_AB():
    print('-->', c)

res1 = [ x*3 for x in gen_AB()]
for i in res1:
    print('-->', i)

res2 = (x*3 for x in gen_AB())
for i in res2:
    print('-->', i)

class Sentence2:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


s3 = Sentence2('Pig and Pepper')
it = iter(s3)
print("it {}\n----------".format(it))
print("next(it) {}\n----------".format(next(it)))
print("next(it) {}\n----------".format(next(it)))
print("next(it) {}\n----------".format(next(it)))


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


ap = ArithmeticProgression(0, 1, 3)
print("list(ap) {}\n----------".format(list(ap)))
ap = ArithmeticProgression(1, .5, 3)
print("list(ap) {}\n----------".format(list(ap)))
ap = ArithmeticProgression(0, 1/3, 1)
print("list(ap) {}\n----------".format(list(ap)))
from fractions import Fraction
ap = ArithmeticProgression(0, Fraction(1, 3), 1)
print("list(ap) {}\n----------".format(list(ap)))
from decimal import Decimal
ap = ArithmeticProgression(0, Decimal('.1'), .3)
print("list(ap) {}\n----------".format(list(ap)))


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


ap = aritprog_gen(0, 1, 3)
print("list(ap) {}\n----------".format(list(ap)))
ap = aritprog_gen(1, .5, 3)
print("list(ap) {}\n----------".format(list(ap)))
ap = aritprog_gen(0, 1/3, 1)
print("list(ap) {}\n----------".format(list(ap)))
from fractions import Fraction
ap = aritprog_gen(0, Fraction(1, 3), 1)
print("list(ap) {}\n----------".format(list(ap)))
from decimal import Decimal
ap = aritprog_gen(0, Decimal('.1'), .3)
print("list(ap) {}\n----------".format(list(ap)))


gen = itertools.count(1, .5)
print("next(gen) {}\n----------".format(next(gen)))
print("next(gen) {}\n----------".format(next(gen)))
print("next(gen) {}\n----------".format(next(gen)))
print("next(gen) {}\n----------".format(next(gen)))

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print("list(gen) {}\n----------".format(list(gen)))


def aritprog_gen2(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n:n < end, ap_gen)
    return ap_gen


ap = aritprog_gen2(0, 1, 3)
print("list(ap) {}\n----------".format(list(ap)))
ap = aritprog_gen2(1, .5, 3)
print("list(ap) {}\n----------".format(list(ap)))
ap = aritprog_gen2(0, 1/3, 1)
print("list(ap) {}\n----------".format(list(ap)))


def vowel(c):
    return c.lower() in 'aeiou'


print("list(filter(vowel, 'Aardvark')) {}\n----------".format(list(filter(vowel, 'Aardvark'))))
print("list(itertools.filterfalse(vowel, 'Aardvark')) {}\n----------".format(list(itertools.filterfalse(vowel, 'Aardvark'))))
print("list(itertools.dropwhile(vowel, 'Aardvark')) {}\n----------".format(list(itertools.dropwhile(vowel, 'Aardvark'))))
print("list(itertools.takewhile(vowel, 'Aardvark')) {}\n----------".format(list(itertools.takewhile(vowel, 'Aardvark'))))
print("list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))) {}\n----------".format(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1)))))
print("list(itertools.islice('Aardvark', 4)) {}\n----------".format(list(itertools.islice('Aardvark', 4))))
print("list(itertools.islice('Aardvark', 4, 7)) {}\n----------".format(list(itertools.islice('Aardvark', 4, 7))))
print("list(itertools.islice('Aardvark', 1, 7, 2)) {}\n----------".format(list(itertools.islice('Aardvark', 1, 7, 2))))


sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print("list(itertools.accumulate(sample)) {}\n----------".format(list(itertools.accumulate(sample))))
print("list(itertools.accumulate(sample, min)) {}\n----------".format(list(itertools.accumulate(sample, min))))
print("list(itertools.accumulate(sample, max)) {}\n----------".format(list(itertools.accumulate(sample, max))))
import operator
print("list(itertools.accumulate(sample, operator.mul)) {}\n----------".format(list(itertools.accumulate(sample, operator.mul))))
print("list(itertools.accumulate(range(1, 11), operator.mul)) {}\n----------".format(list(itertools.accumulate(range(1, 11), operator.mul))))

print("list(enumerate('albatroz', 1)) {}\n----------".format(list(enumerate('albatroz', 1))))
print("list(map(operator.mul, range(11), range(11))) {}\n----------".format(list(map(operator.mul, range(11), range(11)))))
print("list(map(operator.mul, range(11), [2, 4, 8])) {}\n----------".format(list(map(operator.mul, range(11), [2, 4, 8]))))
print("list(map(lambda a, b: (a, b), range(11), [2, 4, 8])) {}\n----------".format(list(map(lambda a, b: (a, b), range(11), [2, 4, 8]))))
print("list(itertools.starmap(operator.mul, enumerate('albatroz', 1))) {}\n----------".format(list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))))
print("list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))) {}\n----------".format(list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1)))))

print("list(itertools.chain('ABC', range(2))) {}\n----------".format(list(itertools.chain('ABC', range(2)))))
print("list(itertools.chain(enumerate('ABC'))) {}\n----------".format(list(itertools.chain(enumerate('ABC')))))
print("list(itertools.chain.from_iterable(enumerate('ABC'))) {}\n----------".format(list(itertools.chain.from_iterable(enumerate('ABC')))))
print("list(zip('ABC', range(5))) {}\n----------".format(list(zip('ABC', range(5)))))
print("list(zip('ABC', range(5), [10, 20, 30, 40])) {}\n----------".format(list(zip('ABC', range(5), [10, 20, 30, 40]))))
print("list(itertools.zip_longest('ABC', range(5))) {}\n----------".format(list(itertools.zip_longest('ABC', range(5)))))
print("list(itertools.zip_longest('ABC', range(5), fillvalue='?')) {}\n----------".format(list(itertools.zip_longest('ABC', range(5), fillvalue='?'))))

print("list(itertools.product('ABC', range(2))) {}\n----------".format(list(itertools.product('ABC', range(2)))))
suits = 'spades hearts diamonds clubs'.split()
print("list(itertools.product('AK', suits)) {}\n----------".format(list(itertools.product('AK', suits))))
print("list(itertools.product('ABC')) {}\n----------".format(list(itertools.product('ABC'))))
print("list(itertools.product('ABC', repeat=2)) {}\n----------".format(list(itertools.product('ABC', repeat=2))))
print("list(itertools.product(range(2), repeat=3)) {}\n----------".format(list(itertools.product(range(2), repeat=3))))

rows = itertools.product('AB', range(2), repeat=2)
for row in rows: print(row)

ct = itertools.count()
print("next(ct) {}\n----------".format(next(ct)))
print("next(ct), next(ct), next(ct) {} {} {}\n----------".format(next(ct), next(ct), next(ct)))
print("list(itertools.islice(itertools.count(1, .3), 3)) {}\n----------".format(list(itertools.islice(itertools.count(1, .3), 3))))

cy = itertools.cycle('ABC')
print("next(cy) {}\n----------".format(next(cy)))
print("list(itertools.islice(cy, 7)) {}\n----------".format(list(itertools.islice(cy, 7))))
rp = itertools.repeat(7)
print("next(rp), next(rp) {} {}\n----------".format(next(rp), next(rp)))
print("list(itertools.repeat(8, 4)) {}\n----------".format(list(itertools.repeat(8, 4))))
print("list(map(operator.mul, range(11), itertools.repeat(5))) {}\n----------".format(list(map(operator.mul, range(11), itertools.repeat(5)))))

print("list(itertools.combinations('ABC', 2)) {}\n----------".format(list(itertools.combinations('ABC', 2))))
print("list(itertools.combinations_with_replacement('ABC', 2)) {}\n----------".format(list(itertools.combinations_with_replacement('ABC', 2))))
print("list(itertools.permutations('ABC', 2)) {}\n----------".format(list(itertools.permutations('ABC', 2))))
print("list(itertools.product('ABC', repeat=2)) {}\n----------".format(list(itertools.product('ABC', repeat=2))))


print("list(itertools.groupby('LLLLAAGGG')) {}\n----------".format(list(itertools.groupby('LLLLAAGGG'))))
for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
print("animals.sort(key=len) {}\n----------".format(animals.sort(key=len)))
print("animals {}\n----------".format(animals))
for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))

print("----------\nlist(itertools.tee('ABC')) {}\n----------".format(list(itertools.tee('ABC'))))
g1, g2 = itertools.tee('ABC')
print("next(g1) {}\n----------".format(next(g1)))
print("next(g2) {}\n----------".format(next(g2)))
print("next(g2) {}\n----------".format(next(g2)))
print("list(g1) {}\n----------".format(list(g1)))
print("list(g2) {}\n----------".format(list(g2)))
print("list(zip(*itertools.tee('ABC'))) {}\n----------".format(list(zip(*itertools.tee('ABC')))))


def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


def chain(*iterables):
    for i in iterables:
        yield from i


s = 'ABC'
t = tuple(range(3))
print("list(chain(s, t)) {}\n----------".format(list(chain(s, t))))


print("all([1, 2, 3]) {}\n----------".format(all([1, 2, 3])))
print("all([1, 0, 3]) {}\n----------".format(all([1, 0, 3])))
print("all([]) {}\n----------".format(all([])))
print("any([1, 2, 3]) {}\n----------".format(any([1, 2, 3])))
print("any([1, 0 ,3]) {}\n----------".format(any([1, 0 ,3])))
print("any([0, 0.0]) {}\n----------".format(any([0, 0.0])))
print("any([]) {}\n----------".format(any([])))
g = (n for n in [0, 0.0, 7, 8])
print("any(g) {}\n----------".format(any(g)))
print("next(g) {}\n----------".format(next(g)))


from random import randint
def d6():
    a = randint(1, 6)
    print("a = {}".format(a))
    return a


d6_iter = iter(d6, 1)
print("d6_iter {}\n----------".format(d6_iter))

for roll in d6_iter:
    print(roll)


# infinite loop
def f():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x+=1
        do_yield(x)


def f():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x+=1
        yield from do_yield(x)


print(f())


from collections import abc
e = enumerate('ABC')
print("isinstance(e, abc.Iterator) {}\n----------".format(isinstance(e, abc.Iterator)))

import types
e = enumerate('ABC')
print("isinstance(e, types.GeneratorType) {}\n----------".format(isinstance(e, types.GeneratorType)))


class Fibonacci:
    def __iter__(self):
        return FibonacciGenerator()


class FibonacciGenerator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self


b = iter(Fibonacci())
print(next(b))
print(next(b))
print(next(b))
print(next(b))


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


b = iter(fibonacci())
print(next(b))
print(next(b))
print(next(b))
print(next(b))
for x in fibonacci():
    print(x)
    if x > 10 ** 2:
        break















