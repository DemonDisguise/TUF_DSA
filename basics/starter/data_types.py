# Data types

# Everything is a object in python 
# That includes: numbers, strings, functions, classes, type themselves
# int - unbounded
num: int = 100

# float
x: float = 5

# complex number
c: complex = 2+3j

# boolean
is_boy: bool = True

# string
name: str = "Rohit"

# checking type 
print(type(num)) # <class 'int'>

# In python list can store anything not necessary it to be one data type 
# Mutable
# List
arr1: list[int | str | float] = [1.38, "hello", 23]
arr2: list[int] = [1, 2, 3]

# Tuple
# Immutable
point: tuple[int, int] = (3, 4)

# Range
r: range = range(1, 10)

# Dictionary
marks: dict[str, int] = {"math": 90, "cs": 95}
print(marks)
print(marks.keys())
print(marks.values())
print(marks.items())

# set
# mutable
s1: set[int] = {1, 2, 3}

# frozenset
# immutable version of set
s2: frozenset[int] = frozenset({1, 2, 3})

# class
class n:
    def __init__(self) -> None:
        self.x: int = 5

# Function
def fn(a: int) -> None:
    print(a)
# Function calling
fn(9)