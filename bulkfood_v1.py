class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')


raisins = LineItem('Golden raisins', 10, 6.95)
print("raisins.subtotal() {}\n----------".format(raisins.subtotal()))
# exception below
# raisins.weight = -20
# raisins = LineItem('Golden raisins', 0, 6.95)
raisins.subtotal()
print("raisins.subtotal() {}\n----------".format(raisins.subtotal()))
