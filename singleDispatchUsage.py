from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize({1,2,3}))
print(htmlize(abs))
print(htmlize('Heimlich & Co.\n- a game'))
print(htmlize(42))
print(htmlize(['alpha', 66, {3,2,1}]))


print("*" * 10)
registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')


print('running main()')
print('registry ->', registry)
f1()


print('\n' + "*" * 10 + "decorator parameters" + "*" * 10 +'\n')

registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')

print(registry)
register()(f3)
print(registry)
register(active=False)(f2)
print(registry)