class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

x = Gizmo()
print(x)

# y = Gizmo() * 10 #exception orrurs
# print(y)

print(dir())

print("*" * 20 + "")
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print("charles id {0} -- lewis id {1}".format(id(charles), id(lewis)))
lewis['balance'] = 950
print("charles is {}".format(charles))

print("*" * 20 + "tuples equality")
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print("id of t1[-1] is {}".format(id(t1[-1])))
t1[-1].append(99)
print("after append 99 {}".format(t1))
print("id of t1[-1] is {}".format(id(t1[-1])))
print(t1 == t2)

print("*" * 20 + "copy is shallow by defalut")
l1 = [3, [55,44], (7,8,9)]
l2 = list(l1)
print(l2)
print("l2 == l1 {}".format(l2 == l1))
print("l2 is l1 {}".format(l2 is l1))


l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
print("original l1,l2 is {}".format(l1))
l1.append(100)
l1[1].remove(55)
print('l1:',l1)
print('l2:',l2)
l2[1]+= [33,22]
l2[2]+= (10,11)
print('l1:',l1)
print('l2:',l2)

print("*" * 20 + "Bus picks up passengers")

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

import copy


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)


print("*" * 20 + "cyclic copies")

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)
from copy import deepcopy
c = deepcopy(a)
print(c)


print("*" * 20 + "function parameters")

def f(a,b):
    a += b
    return a

x = 1
y = 2
f(x,y)
print("the number is unchanged")
print(f(x,y))
print(x,y)

a = [1,2]
b = [3,4]
print("the list is changed")
print(f(a,b))
print(a,b)
t = (10,20)
u = (30,40)
print("the tuple is unchanged")
print(f(t,u))
print(t, u)

print("*" * 20 + "dangerous passengers")

class HauntedBus:
    def __init__(self, passengers = []):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)

bus1.pick('Charlie')
bus1.drop('Alice')
print("bus1:",bus1.passengers)
bus2 = HauntedBus()
bus2.pick('Carrie')
print("bus2:", bus2.passengers)
bus3 = HauntedBus()
print("bus3 given the default list!!!a")
print("bus3:", bus3.passengers)
bus3.pick('Dave')
print("bus2:", bus2.passengers)
print(bus2.passengers is bus3.passengers)
print("bus1:", bus1.passengers)
print("HauntedBus.__init__", dir(HauntedBus.__init__))
print("HauntedBus.__init__.__defaults__[0]", HauntedBus.__init__.__defaults__[0])
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)

print("*" * 20 + "basketball_team droped by twilightBus")

class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
print("basket_ballteam: ", basketball_team)
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print("basket_ballteam: ", basketball_team)

print("*" * 20 + " weakref callback")

import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)

print("*" * 20 + " weakref callback")

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print(wref())
print(wref() is None)
print(wref() is None)

print("*" * 20 + " WeakValueDictionary")


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese
print("sorted(stock.keys())",sorted(stock.keys()))
del catalog
print("del catalog")
print("sorted(stock.keys()", sorted(stock.keys()))
del cheese
print("del cheese")
print("sorted(stock.keys()", sorted(stock.keys()))

print("*" * 20 + " WeakValueDictionary")

class MyList(list):
    pass

a_list = MyList(range(10))
wref_to_a_list = weakref.ref(a_list)


print("*" * 20 + " copy tuple is reference")

t1 = (1, 2, 3)
t2 = tuple(t1)
print("t2 is t1 ",t2 is t1)
t3 = t1[:]
print("t3 is t1 ",t3 is t1)

s1 = 'ABC'
s2 = 'ABC'
print("Implementation internal string equal", s1 is s2)
