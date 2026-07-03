# Arrays basics

import array
# Why are arrays 0-indexed
""" 
- Counting arrays fro mthe index value 0 simplifies the computation for the memory

- Array contains homogeneous data, but python's list and tuple are heterogeneous
 
- you can access elements with indexing

- use append(), insert() for inserting
- use pop(), remove() for removing
"""
# For true, fixed-size, homogeneous arrays use array module - memory-efficient
my_list: list[int | float | tuple | str | bool] = [10, "hello", 10.4, True]

list1: list[int] = [1, 2, 3, 4]
print(list1[0])
list1[0] = 0
print(list1)
list1.remove(0)
print(list1)
list1.append(24)
print(list1)
list1.insert(2, 10)
print(list1)
list1.pop()
print(list1)
list2 = array.array('i', [1, 2, 3, 4])
print(list2)
print(list2[0])

# for numerical computations you can use numpy which has homogeneous data and fixed size, efficient operations

# Strings are sequence of characters stored in a specific order
""" 
- len() to get length of the string

- using 0-based indexing [] access individual characters in a string

- concatenate(join strings) using '+' operator

- comparison = '==' or '!=' 
"""
print()
my_str: str = "Annex"
print(len(my_str))
print(my_str[1])
my_str += "ature"
print(my_str)
print(my_str == "Annexature")