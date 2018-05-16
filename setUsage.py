print("-"*20)
l = ['spam', 'spam', 'eggs', 'spam']
print("set(l) {}".format(set(l)))

print("-"*20)
needles = set(l)
print("needles {}".format(needles))
haystack = set(["spam", "eggs", "abs"])
print("haystack {}".format(haystack))

found = 0
for n in needles:
    if n in haystack:
        found += 1
print("found needles & haystack 1 is {}".format(found))

found = len(needles & haystack)
print("found needles & haystack 2 is {}".format(found))

found = len(needles.intersection(haystack))
print("found needles & haystack 3 is {}".format(found))

print("haystack - needles is {}".format(haystack - needles))

print("haystack ^ needles (__xor__) is {}".format(haystack ^ needles))

print("haystack > needles (__xor__) is {}".format(haystack > needles))

needles &= haystack
print("needles &= haystack is {}".format(needles))

print("-"*20)
s = {1}
print("type(s) {}".format(type(s)))
print("s {}".format(s))
s.pop()
print("s after pop {}".format(s))
from dis import dis
print("dis('{1}')")
dis('{1}')
print("dis('set([1])')")
dis('set([1])')

print("-"*20)
print("frozenset(range(10)) {}".format(frozenset(range(10))))
print("-"*20)
from unicodedata import name
print("<chr(i) for i in range(32,256) if 'SIGN' in name(chr(i), '')> {}".format({chr(i) for i in range(32,256) if 'SIGN' in name(chr(i), '')}))
print("name(chr(i), '') {}".format(name(chr(245), '')))
#print("chr(i) for i in range(32,256) {}".format({ chr(i) for i in range(32,256) }))

print("-"*20)
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
d1 = dict(DIAL_CODES)
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3

print("-"*20)
import sys
MAX_BITS = len(format(sys.maxsize, 'b'))
print('%s-bit Python build' % (MAX_BITS + 1))

def hash_diff(o1, o2):
    h1 = '{:>0{}b}'.format(hash(o1),MAX_BITS)
    h2 = '{:>0{}b}'.format(hash(o2),MAX_BITS)
    diff = ''.join('!' if b1 != b2 else ' ' for b1, b2 in zip(h1, h2))
    count = '!= {}'.format(diff.count('!'))
    width = max(len(repr(o1)), len(repr(o2)), 8)
    sep = '-' * (width * 2 + MAX_BITS)
    return '{!r:{width}} {}\n{:{width}} {} {}\n{!r:{width}} {}\n{}'.format(o1, h1, ' ' * width, diff, count, o2, h2, sep, width=width)

if __name__ == '__main__':
    print("-" * 20)
    print(hash_diff(1, 1.0))
    print(hash_diff(1.0, 1.0001))
    print(hash_diff(1.0001, 1.0002))
    print(hash_diff(1.0002, 1.0003))