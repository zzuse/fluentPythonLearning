import inspect


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)


my_coro = simple_coroutine()
print("linspect.getgeneratorstate(my_coro) {}\n----------".format(inspect.getgeneratorstate(my_coro)))
print("my_coro {}\n----------".format(my_coro))
print("linspect.getgeneratorstate(my_coro) {}\n----------".format(inspect.getgeneratorstate(my_coro)))
print("next(my_coro) {}\n----------".format(next(my_coro)))
print("linspect.getgeneratorstate(my_coro) {}\n----------".format(inspect.getgeneratorstate(my_coro)))
try:
    my_coro.send(42)
except:
    print("simple_coroutine except")
print("linspect.getgeneratorstate(my_coro) {}\n----------".format(inspect.getgeneratorstate(my_coro)))


def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


my_coro2 = simple_coro2(14)
print("linspect.getgeneratorstate(my_coro2) {}\n----------".format(inspect.getgeneratorstate(my_coro2)))
print("next(my_coro2) {}\n----------".format(next(my_coro2)))
print("linspect.getgeneratorstate(my_coro2) {}\n----------".format(inspect.getgeneratorstate(my_coro2)))
print("my_coro2.send(28) {}\n----------".format(my_coro2.send(28)))
print("linspect.getgeneratorstate(my_coro2) {}\n----------".format(inspect.getgeneratorstate(my_coro2)))
try:
    my_coro2.send(99)
except:
    print()
print("linspect.getgeneratorstate(my_coro2) {}\n----------".format(inspect.getgeneratorstate(my_coro2)))


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager()
print("next(coro_avg) {}\n----------".format(next(coro_avg)))
print("coro_avg.send(10) {}\n----------".format(coro_avg.send(10)))
print("coro_avg.send(30) {}\n----------".format(coro_avg.send(30)))
print("coro_avg.send(5) {}\n----------".format(coro_avg.send(5)))


from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager()
print("inspect.getgeneratorstate(coro_avg) {}\n----------".format(inspect.getgeneratorstate(coro_avg)))
print("coro_avg.send(10) {}\n----------".format(coro_avg.send(10)))
print("coro_avg.send(30) {}\n----------".format(coro_avg.send(30)))
print("coro_avg.send(5) {}\n----------".format(coro_avg.send(5)))
## below raise tye error
# print("coro_avg.send('spam') {}\n----------".format(coro_avg.send('spam')))


class DemoException(Exception):
    """An exception"""


def demo_exc_handling():
    print('-> corotine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')


exc_coro = demo_exc_handling()
print("next(exc_coro) {}\n----------".format(next(exc_coro)))
print("exc_coro.send(11) {}\n----------".format(exc_coro.send(11)))
print("exc_coro.send(22) {}\n----------".format(exc_coro.send(22)))
print("exc_coro.throw(DemoException) {}\n----------".format(exc_coro.throw(DemoException)))
print("inspect.getgeneratorstate(exc_coro) {}\n----------".format(inspect.getgeneratorstate(exc_coro)))
try:
    print("exc_coro.throw(ZeroDivisionError) {}\n----------".format(exc_coro.throw(ZeroDivisionError)))
except:
    print("ZeroDivisionError")
print("exc_coro.close() {}\n----------".format(exc_coro.close()))
print("inspect.getgeneratorstate(exc_coro) {}\n----------".format(inspect.getgeneratorstate(exc_coro)))


from collections import namedtuple


Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


coro_avg = averager()
print("next(coro_avg) {}\n----------".format(next(coro_avg)))
print("coro_avg.send(10) {}\n----------".format(coro_avg.send(10)))
print("coro_avg.send(30) {}\n----------".format(coro_avg.send(30)))
print("coro_avg.send(6.5) {}\n----------".format(coro_avg.send(6.5)))
try:
    print("coro_avg.send(None) {}\n----------".format(coro_avg.send(None)))
except StopIteration as exc:
    result = exc.value
    print("result {}\n----------".format(result))


def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


print("list(gen()) {}\n----------".format(list(gen())))


def gen():
    yield from 'AB'
    yield from range(1, 3)


print("list(gen()) {}\n----------".format(list(gen())))


# delegating generator
def grouper(results, key):
    while True:
        results[key] = yield from averager()


# the client code, a.k.a the caller
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    print(results)
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)

