# deque
# list-like container with fast appends and pops on either end
from collections import deque

# 1. Initialization
# Create a deque with some initial elements
my_deque: deque[str] = deque(["apple", "banana", "cherry"])
print(f"Initail deque: {my_deque}")

# Create a bounded queue
bounded_deque: deque[str] = deque(maxlen=3)
print(f"Initial bounded deque: {bounded_deque}")

# 2. Appending and Extending
my_deque.append('date')
my_deque.appendleft('apricot')
print(f"After append and appendleft: {my_deque}")

# Extend with multiple items
my_deque.extend(['elderberry', 'fig'])
print(f"After extend: {my_deque}")

my_deque.extendleft(['grape'])
my_deque.extendleft('abc')
print(f"After extendleft: {my_deque}")

bounded_deque.extend(['A', 'B', 'C', 'D']) # 'A' will be discarded
print(f"Bounded deque after extending bounded deque: {bounded_deque}")

# 3. Popping
rightmost_item = my_deque.pop()
print(f"Popped from right: {rightmost_item}")

leftmost_item = my_deque.popleft()
print(f"Popped from left: {leftmost_item}")

# Attempting to pop from an empty deque will raise IndexError

# 4. Counting and Indexing
print(f"Count of 'banana': {my_deque.count('banana')}")
print(f"Element at index 0: {my_deque[0]}")
print(f"Element at the last index: {my_deque[-1]}")

# 5. Removing specific values
try:
    my_deque.remove('cherry')
    print(f"After removing 'cherry': {my_deque}")
except ValueError:
    print("'cherry' not found in deque")

# 6. Rotating
print(f"\nDeque before rotation: {my_deque}")
my_deque.rotate(2)
print(f"After rotating right by 2: {my_deque}")
my_deque.rotate(-1)
print(f"After rotating left by 1: {my_deque}")

# 7. Reversing
my_deque.reverse()
print(f"\nAfter reversing: {my_deque}")

# 8. Clearing
print(f"\nBefore clearing: {my_deque}")
my_deque.clear()
print(f"After clearing: {my_deque}")

# 9. Copying
original_deque: deque[int] = deque([1, 2, 3])
copied_deque: deque[int] = original_deque.copy()
print(f"\nOriginal deque: {original_deque}")
print(f"Copied deque: {copied_deque}")
copied_deque.append(4)
print(f"Original after modifying copy: {original_deque}")
print(f"Modified copy: {copied_deque}")

# 10. Maxlen
print(f"\nMax length of bounded_deque: {bounded_deque.maxlen}")
print(f"Max length of my_deque: {my_deque}")

# 11. Iteration and Membership
my_deque_for_iteration: deque[str] = deque(['x', 'y', 'z'])
print("\nIterating through deque: ")
for item in my_deque_for_iteration:
    print(item)

print(f"\nIs 'y' in the deque? {'y' in my_deque_for_iteration}")