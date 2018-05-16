lax_coordinates = (33.9425,-118.408056)
print(lax_coordinates[0])
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA','31195855'),('BRA', 'CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

t = (20,8)
print(t)
quotient, remainder = divmod(*t)
print(quotient,remainder)

import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

a,b,*rest = range(5)
print(a,b,rest)

a,b,*rest = range(3)
print(a,b,rest)

a,b,*rest = range(2)
print(a,b,rest)

a, *body, c, d = range(5)
print(a,body,c,d)

*head, b,c,d = range(5)
print(head,b,c,d)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', '21.935', (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.43333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15}| {:^9} | {:^9}'.format('', 'lat.', 'long.') )
fmt = '{:15}| {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude,longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name,latitude,longitude))

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP',  36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889,77.208889))
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())
for key,value in delhi._asdict().items():
    print(key + ':', value)