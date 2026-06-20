# OrderedDict
# regular dict is good at mapping operations, tracking insertion order is secondary
# OrderedDict is designed to be good at reordering operations. Space efficiency, iteration speed, and performance of update operations are secondary
# It can handle frequent reordering operations
# popitem(last=True) here we can specify which item in popped
# move_to_end() to efficiently reposition an element to an endpoint

from collections import OrderedDict

# 1. Creating and Insertion
od: OrderedDict[str, int] = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3
od['date'] = 4

print(f"OrderedDict: {od}")

# 2. Overwriting an item
od['banana'] = 22
print(f"OrderedDict after overwriting: {od}")

# 3. using popitem
last_item: tuple[str, int] = od.popitem()
print(f"Last item in OrderedDict: {last_item}")

first_item: tuple[str, int] = od.popitem(last=False)
print(f"First item in OrderedDict: {first_item}")

print(f"OrderedDict after popitem(): {od}")

# 4. Using move_to_end()
od.move_to_end('banana')
print(f"OrderedDict after move_to_end: {od}")

od.move_to_end('banana', last=False)
print(f"OrderedDict after move_to_end with last as False: {od}")

# Equality comparison with another OrderedDict
od1: OrderedDict[str, int] = OrderedDict([('a', 1), ('b', 2)])
od2: OrderedDict[str, int] = OrderedDict([('b', 2), ('a', 1)])
od3: OrderedDict[str, int] = OrderedDict([('a', 1), ('b', 2)])

print(f"od1 == od2: {od1 == od2}")
print(f"od1 == od3: {od1 == od3}")

# comparison with regular dict
regular_dict = {'b': 2, 'a': 1}
print(f"od1 == regular_dict: {od1 == regular_dict}")
# This behaviour is subtle
# For strict order-sensitive comparisons, compare with another OrderedDict

# Iteration order
print("Iterating through keys: ")
for key in od1:
    print(key, end=" ")
print("\nIterating through values: ")
for value in od1.values():
    print(value, end=" ")
print("\nIterating through items: ")
for item in od1.items():
    print(item, end=" ")
print()