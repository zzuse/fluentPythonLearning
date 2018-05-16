from array import array
from random import random

print("----------------10 million floats in array------------")

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-1])
print(floats[10])
print(floats2 == floats)
print("----------------memory view------------")
numbers = array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
print("----------------sciPy and NumPy------------")
import numpy
a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
print(a[:, 1])
print(a.transpose())
floats = numpy.loadtxt('floats-10M-lines.txt')
print(floats[-3:])
floats *= .5
print(floats[-3:])
from time import perf_counter as pc
t0 = pc(); floats /= 3;
print(pc() - t0)
numpy.save('floats-10M', floats)
floats2 = numpy.load('floats-10M.npy', 'r+')
floats2 *= 6
print(floats2[-3:])

