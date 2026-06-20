# namedtuple
# factory function for creating tuple subclasses with named fields

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p: tuple[int, int] = Point(11, y=22)

# Unpacking
x, y = p

# Accessing
print(p[0])
print(p.x)
print(p)
print(getattr(p, 'x '))

# replace
p._replace(x=10)
print(p)

print(p._asdict())
print(p._fields)
