
def f1(a):
    print(a)
    print(b)

b = 3
f1(3)

b = 6
def f2(a):
    print(a)
    print(b)
    b = 9  #this line will panic, surprise?


from dis import dis
dis(f1)
dis(f2)

# f2(3) #this line will panic

class Averager():
    def __init__(self):
        self.series = []
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        print("averager class...")
        return total/len(self.series)

avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))

def make_average():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        print('averager closure...')
        return total/len(series)
    return averager

avg = make_average()
print(avg(10))
print(avg(11))
print(avg(12))
print("__code__.co_varnames = {}".format(avg.__code__.co_varnames))
print("__code__.co_freevars = {}".format(avg.__code__.co_freevars))
print("__closure__ = {}".format(avg.__closure__))
print("__closure__[0].cell_contents = {}".format(avg.__closure__[0].cell_contents))

def make_averageer():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        print('effective closure...')
        return total / count
    return averager

avg = make_averageer()
print(avg(10))
print(avg(11))
print(avg(12))

import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


print('*' * 40, 'Calling snooze(.123)')
snooze(.123)
print('*' * 40, 'Calling factorial(6)')
print('6! = ', factorial(6))
print('factorial func real name is: {}'.format(factorial.__name__))

import functools


def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock2
def factorial2(n):
    return 1 if n < 2 else n*factorial2(n-1)


print('*' * 40, 'Calling factorial2(6)')
print('6! = ', factorial2(6,))
print('factorial2 func real name is: {}'.format(factorial2.__name__))

@clock2
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print('*' * 40)
print("fibonaci(6) not efficient {}".format(fibonacci(6)))

@functools.lru_cache()
@clock2
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)

print('*' * 40)
print("fibonaci2(6) efficient {}".format(fibonacci2(6)))

