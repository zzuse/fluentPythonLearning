from collections import abc
my_dict = {}

print('-'*20)
print("instance of abc {}".format(isinstance(my_dict, abc.Mapping)))
print('-'*20)
tt = (1,2,(30,40))
print("tuple is hashable {}".format(hash(tt)))
tf = (1,2,frozenset([30,40]))
print("frozen set is hashable {}".format(hash(tf)))
print('-'*20)
a = dict(one=1,two=2,three=3)
print("building dict {}".format(a))
b = {'one' : 1, 'two': 2, 'three' : 3}
print("building dict {}".format(b))
c = dict(zip(['one', 'two', 'three'], [1,2,3]))
print("building dict {}".format(c))
d = dict([('two', 2), ('one', 1), ('three', 3)])
print("building dict {}".format(d))
e = dict({'three':3, 'one': 1, 'two': 2})
print("building dict {}".format(e))
print("equal dict {}".format(a==b==c==d==e))

print('-'*20)
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
country_code = {country: code for code, country in DIAL_CODES}
print("country_code {}".format(country_code))
print("another code {}".format({code: country.upper() for country, code in country_code.items() if code < 66}))

print('-'*20)
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2','two'), ('4','four')])
print("StrKeyDict0 d['2'] {}".format(d['2']))
print("StrKeyDict0 d[4] {}".format(d[4]))
# below will raise exception
# print("StrKeyDict0 d[1] {}".format(d[1]))
print("StrKeyDict0 d.get('2') {}".format(d.get('2')))
print("StrKeyDict0 d.get(4) {}".format(d.get(4)))
print("StrKeyDict0 d.get(1, 'N/A') {}".format(d.get(1, 'N/A')))
print("StrKeyDict0 2 in d {}".format(2 in d))
print("StrKeyDict0 1 in d {}".format(1 in d))

print('-'*20)
import builtins
from collections import ChainMap
pylookups = ChainMap(locals(), globals(), vars(builtins))
print("builtins {}".format(pylookups))

from collections import Counter
ct = Counter('abracadabra')
print("counter {}".format(ct))
ct.update('aaaaazzz')
print("counter {}".format(ct))
print("most common {}".format(ct.most_common(2)))

print('-'*20)
import collections
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str[key]]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

d = StrKeyDict([(2,'two'), (4,'four')])
# print("StrKeyDict d[2] {}".format(d[2]))
print("StrKeyDict d['2'] {}".format(d['2']))

print('-'*20)
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print("d_proxy {}".format(d_proxy))
print("d_proxy[1] {}".format(d_proxy[1]))
d[2] = 'B'
#any changes will be reflect
print("d_proxy[2] {}".format(d_proxy[2]))