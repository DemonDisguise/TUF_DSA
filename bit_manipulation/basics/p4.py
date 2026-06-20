# Binary operators

# Binary addition
# 0 + 0 -> 0
# 0 + 1 -> 1
# 1 + 0 -> 1
# 1 + 1 -> 10

# Binary subtraction
# x - y = x + (2s compliment of y)

# Binary multiplication
# 0 * 0 -> 0
# 0 * 1 -> 0
# 1 * 0 -> 0
# 1 * 1 -> 1



# AND &
# all true -> true
# 1 false -> false
# 1 & 1 -> 1
# 1 & 0 -> 0
# 0 & 1 -> 0
# 0 & 0 -> 0

print(13 & 7) # 5

# OR |
# 1 true -> true
# all false -> false
# 1 & 1 -> 1
# 1 & 0 -> 1
# 0 & 1 -> 1
# 0 & 0 -> 0

print(13 & 7) # 15

# XOR ^
# no. of 1s -> odd -> 1
# no. of 1s -> even -> 0

print(13 ^ 7) # 10

# right shift >>
# shift bits right by k positions
# x >> k = x // (2 ** k)

print(13 >> 1) # 6

# left shift <<
# shift bits left by k positions
# x << k = x * (2 ** k)
# in c/cpp overflow occurs if it more than 32 bit, then it discards bits until it is just 32 bit
# but python doesnt have that limit

print(13 << 1) # 26

# For signed n bit integers
# MAX = 2 ** (n - 1) - 1
# MIN = - 2 ** (n - 1)

# INT_MIN = -2**31
# INT MAX = 2**31 - 1

# NOT ~
# Steps: flips, check if -ve, if -ve 2s compliment else stop

print(~5)


# & -> keep common 1s
# | -> turn bits on
# ^ -> flip if different
# ~ -> invert
# << -> move left
# >> -> move right

# n & mask -> check ith bit
# n | mask -> set ith bit
# n ^ mask -> toggle ith bit
# n & ~mask -> clear ith bit