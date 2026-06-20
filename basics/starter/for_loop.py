# For loop 
# - control structure in programming taht allows you to execute a specific block of code repeatedly.

for i in range(1, 10):
    print(i, end=" ")
print()

# For else loop 
# Runs else block if loop runs without breaking 

for i in range(1, 10):
    print(i, end=" ")
else:
    print("\nDone looping")

for i in range(1, 10): 
    if i > 8:
        break
    print(i, end=" ")
else:
    print("\nDone looping")