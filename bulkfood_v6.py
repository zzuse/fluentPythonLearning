import model_v6 as model

@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


raisins = LineItem('Golden raiseins', 10, 6.95)
print("raisins {}\n----------".format(raisins))
print("dir(raisins)[:3] {}\n----------".format(dir(raisins)[:3]))
print("LineItem.description.storage_name {}\n----------".format(LineItem.description.storage_name))
print("raisins.description {}\n----------".format(raisins.description))
print("getattr(raisins, '_NonBlank#description') {}\n----------".format(getattr(raisins, '_NonBlank#description')))
