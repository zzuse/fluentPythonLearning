class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
    weight = property(get_weight, set_weight)


raisins = LineItem('Golden raisins', 10, 6.95)
print("raisins.subtotal() {}\n----------".format(raisins.subtotal()))
# exception below
# raisins.weight = -20
# raisins = LineItem('Golden raisins', 0, 6.95)
raisins.subtotal()
print("raisins.subtotal() {}\n----------".format(raisins.subtotal()))


class Class:
    data = 'the class data attr'

    @property
    def prop(self):
        return 'the prop value'


obj = Class()
print("vars(obj) {}\n----------".format(vars(obj)))
print("obj.data {}\n----------".format(obj.data))
obj.data = 'bar'
print("vars(obj) {}\n----------".format(vars(obj)))
print("obj.data {}\n----------".format(obj.data))
print("Class.data {}\n----------".format(Class.data))

print("Class.prop{}\n----------".format(Class.prop ))
print("obj.prop{}\n----------".format(obj.prop ))
# obj.prop = 'foo'
obj.__dict__['prop'] = 'foo'
print("vars(obj){}\n----------".format(vars(obj) ))
print("obj.prop{}\n----------".format(obj.prop ))
Class.prop = 'baz'
print("obj.prop{}\n----------".format(obj.prop ))

print("obj.data {}\n----------".format(obj.data))
print("Class.data {}\n----------".format(Class.data))
Class.data = property(lambda self: 'the "data" prop value')
print("obj.data {}\n----------".format(obj.data))
del Class.data
print("obj.data {}\n----------".format(obj.data))


# use python3 -i to run help(Foo.bar) help(Foo)
class Foo:
    @property
    def bar(self):
        '''The bar attribute'''
        return self.__dict__['bar']

    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value