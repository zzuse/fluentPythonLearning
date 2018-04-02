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
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)

a = tuple(ord(symbol) for symbol in symbols)
print(a)

import array
b = array.array('I',(ord(symbol) for symbol in symbols))
print(b)

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