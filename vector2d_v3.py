from vector2d import Vector2d
v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
print(len(dumpd))
v1.typecode = 'f'
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))
print(Vector2d.typecode)


class ShortVector2d(Vector2d):
    typecode = 'f'

sv = ShortVector2d(1/11, 1/27)
print(sv)
print(len(bytes(sv)))
