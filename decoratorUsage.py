
print('----target----')
def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')


print('----registry before call main-----')

registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    target()
    print(target)
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()

def f(a):
    global b
    print(a)
    print(b)
    b=9
b = 6
f(3)

