
def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = '_{}:{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity()
    price = quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

print("LineItem.price {}\n----------".format(LineItem.price))


br_nuts = LineItem('Brazil nuts', 10, 34.95)
print("br_nuts.price {}\n----------".format(br_nuts.price))