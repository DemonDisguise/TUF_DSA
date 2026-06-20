# Functions

from typing import List
# Python uses pass-by-object reference (call by sharing)

# Pass by value (behavior with immutable objects)
# Immutable objects: int, float, str, tuple, bool
""" 
When you pass them to a function:
    - A reference to the object is passed
    - But you cannot modify the object itself
    - Reassigning creates a new object
"""
def change(x: int) -> None:
    x = 20
    print(f"Inside function: {x}")

a: int = 10
change(a)
print(f"Outside function: {a}")

# Pass by reference (behavior with mutable objects)
# Mutable objects: list, dict, set, custom objects
""" 
When you modify them:
    - The same object is changed
    - Changes are visible outside the function
"""

def change_lst(lst: List) -> None:
    lst.append(4)
    print(f"Inside function: {lst}")

nums: List[int] = [1, 2, 3]
change_lst(nums)
print(f"Outside function: {nums}")

# Reassigning a mutable object, it won't affect the original
def reset_lst(lst):
    lst = []
    print(f"Inside function: {lst}")

nums = [1, 2, 3]
reset_lst(nums)
print(f"Outside function: {nums}")

# Lambda functions
# It is small one-liner anonymous function defined using 'lambda' keyword
# It can take any number of arguments but only one expression
l = lambda x: x ** 2
print(l(2))