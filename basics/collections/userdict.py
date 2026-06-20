# UserDict
# wrapper around dictionary objects for easier dict subclassing

from collections import UserDict

class MyCustomDict(UserDict):
    """
    A custom dictionary that adds a method to get all keys in uppercase.
    It inherits from UserDict to easily access the underlying data.
    """
    def get_uppercase_keys(self):
        """Returns a list of all keys in uppercase."""
        return [key.upper() for key in self.data.keys()]

# creation
my_dict: MyCustomDict = MyCustomDict({'name': 'Sun', 'age': 30, 'city': 'New York'})
print(f"MyCustomDict: {my_dict}")

# Accessing data directly via .data attribute
print(f"Underlying dictionary: {my_dict.data}")

# Using a standard dictionary method (inherited from dict)
print(f"Value from 'name': {my_dict['name']}")

# Using custom method
print(f"Uppercase keys: {my_dict.get_uppercase_keys}")

# Adding a new item
my_dict['occupation'] = 'Developer'
print(f"After adding 'occupation': {my_dict}")

# Demonstrating that it behaves like dict
print(f"Is 'city' in the dictionary? {'city' in my_dict}")