# UserString
# wrapper around string objects for easier string subclassing

from collections import UserString

class MyCustomString(UserString):
    """
    A custom string that adds a method to count vowels.
    It inherits from UserString to easily access the underlying data.
    """
    
    def count_vowels(self):
        """Counts the number of vowels in a string - case insensitive"""
        vowels = "aeiouAEIOU"
        count = 0
        for char in self.data:
            if char in vowels:
                count += 1
        return count

# Usage
my_string: MyCustomString = MyCustomString("Hello, World! This string is created using UserString.")
print(f"MyCustomString: {my_string}")

# Accessing data directly via .data attribute
print(f"Underlying string: {my_string.data}")

# Using a standard string method
print(f"Uppercased: {my_string.upper()}")

# Using custom method
print(f"Number of vowels: {my_string.count_vowels()}")

# Demonstrating it behaves like a string
print(f"Character at index 0: {my_string[0]}")

print(f"String sliced: {my_string[7:12]}")