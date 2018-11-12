def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    """a.k.a. data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    """an overriding descriptor without ```__get__``"""
    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    """a.k.a. non-data or shadowable descriptor"""
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))

obj = Managed()
obj.over
Managed.over
obj.over = 7
obj.over
obj.__dict__['over'] = 8
print("vars(obj) {}\n----------".format(vars(obj)))
obj.over

print("\n----------None Override Get")
print("obj.over_no_get {}\n----------".format(obj.over_no_get))
print("Managed.over_no_get {}\n----------".format(Managed.over_no_get))
obj.over_no_get = 7
print("obj.over_no_get {}\n----------".format(obj.over_no_get))

obj.__dict__['over_no_get'] = 9
print("obj.over_no_get {}\n----------".format(obj.over_no_get))
obj.over_no_get = 7
print("obj.over_no_get {}\n----------".format(obj.over_no_get))

print("\n----------None Override Set")
obj.non_over
obj.non_over = 7
print("obj.non_over {}\n----------".format(obj.non_over))
Managed.non_over
del obj.non_over
obj.non_over


obj = Managed()
Managed.over = 1
Managed.over_no_get = 2
Managed.non_over = 3

print("obj.over {}\n----------".format(obj.over))
print("obj.over_no_get {}\n----------".format(obj.over_no_get))
print("obj.non_over {}\n----------".format(obj.non_over))

obj = Managed()
print("obj.spam {}\n----------".format(obj.spam))
print("Managed.spam {}\n----------".format(Managed.spam))
obj.spam = 7
print("obj.spam {}\n----------".format(obj.spam))



