symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes2 = [ord(symbol) for symbol in symbols]
print(codes2)

x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c:c>127,map(ord,symbols)))
print(beyond_ascii)

colors =['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)
for color in colors:
    for size in sizes:
        print((color,size))

tshirts = [(color,size) for size in sizes
                        for color in colors]
print(tshirts)

'''generator'''
print("--------------- generator------------")

for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)

a = tuple(ord(symbol) for symbol in symbols)
print(a)

import array
b = array.array('I',(ord(symbol) for symbol in symbols))
print(b)

print("--------------- Slices------------")

l = [10,20,30,40,50,60]
print(l[:2])
print(l[2:])

s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

invoice = """
0     6                                40          52 55
1909  Pimoroni PiBrella                 $17.50      3    $52.50
1489  6mm Tactile Switch                $4.95       2    $9.90
1510  Panavise Jr.-PV-201               $28.00      1    $28.00
1610  PiTFT Mini Kit                    $34.95      1    $34.95
"""
SKU = slice(0,6)
DESCRIPTION = slice(6,40)
UNIT_PRICE = slice(40,52)
QUANTITY = slice(52,55)
ITEM_TOTAL = slice(55,None)
line_times = invoice.split('\n')[2:]
for item in line_times:
    print(item[UNIT_PRICE],item[DESCRIPTION])

'''assigning to Slices'''
print("--------------- assigning to Slices------------")
l = list(range(10))
print(l)
l[2:5]=[20,30]
print(l)
del l[5:7]
l[3::2] = [11,22]
print(l)
l[2:5] = [100]
print(l)

'''+ and *'''
print("--------------- + and *------------")

l = [1,2,3]
print(l*5)
print(5*'abcd')

'''lists of lists'''
print("---------------lists of lists------------")

board = [['_'] * 3 for i in range(3) ]
print(board)
board[1][2] = 'X'
print(board)
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
board[1][2] = 'X'
print(board)

'''reference of inner list'''
print("---------------reference of inner list------------")

weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)
row = ['_'] *3
board = []
for i in range(3):
    board.append(row)
board[1][2] = '0'
print(board)

''' *= usage '''
print("---------------*= usage------------")

l = [1,2,3]
print(id(l))
l *= 2
print(l)
print(id(l))
t = (1,2,3)
print(id(t))
t *= 2
print(id(t))

import dis
dis.dis('s[a] += b')

'''list sort'''
print("---------------list sort------------")

fruits = ['grape','raspbeerry', 'apple', 'banana']
print(sorted(fruits))
print(sorted(fruits,reverse=True))
print(sorted(fruits,key=len))
print(sorted(fruits,key=len,reverse=True))
print(fruits)
fruits.sort()
print(fruits)

'''bisect usage'''
print("---------------bisect usage------------")
import bisect
import sys
HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle,position, offset))

if __name__  == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

def grade(score, breakpoints = [60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    return grades[i]

print([grade(score) for score in [33,99,77,70,89,90,200]])

print("---------------bisect.insort usage------------")

import bisect
import random

SIZE = 7
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)