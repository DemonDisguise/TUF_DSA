# UserList
# wrapper around list objects for easier list subclassing
from collections import UserList

class MyCustomList(UserList):
    """
    A custom list that adds a method to find the sum of numeric elements.
    It inherits from UserList to easily access the underlying data.
    """
    def sum_numeric_elements(self):
        """Calculates the sum of all elements that are numbers(int or float)."""
        total = 0
        for item in self.data:
            if isinstance(item, (int, float)):
                total += item
        return total
    
# Usage
my_list: MyCustomList = MyCustomList([10, 'hello', 20.5, 'world', 30, True])
print(f"MyCustomList instance: {my_list}")

# Accessing data directly via .data attribute
print(f"Underlying list: {my_list.data}")

# Using standard list method
my_list.append(40)
print(f"After appending 40: {my_list}")

# Using custom method
print(f"Sum of numeric elements: {my_list.sum_numeric_elements()}")

# Demonstrating it behaves like normal list
print(f"Element at index 2: {my_list[2]}")
print(f"Length of the list: {len(my_list)}")