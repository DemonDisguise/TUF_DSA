# 1'S COMPLEMENT AND 2'S COMPLEMENT 

# ------------------------------------------------------------
# WHY DO WE NEED COMPLEMENTS?
# ------------------------------------------------------------

# Computers store data in binary.
# We need a way to represent NEGATIVE numbers.

# Example:
# +5 = 00000101

# One naive idea:
#
# Positive:
# 00000101
#
# Negative:
# 10000101
#
# (Using MSB as sign bit)
#
# Problems:
# +0 = 00000000
# -0 = 10000000
#
# Two representations of zero.
# Arithmetic becomes complicated.


# ============================================================
# 1'S COMPLEMENT
# ============================================================

# Definition:
#
# Flip every bit.
#
# 0 -> 1
# 1 -> 0

# Example:
#
# 5 = 00000101
#
# 1's complement:
#
# 11111010


def ones_complement(num, bits=8):
    mask = (1 << bits) - 1
    return (~num) & mask


print("1's Complement of 5 (8 bits):")
print(f"{ones_complement(5):08b}")

# Output:
# 11111010


# ------------------------------------------------------------
# PROBLEM WITH 1'S COMPLEMENT
# ------------------------------------------------------------

# +0

# 00000000

# 1's complement of 0

# 11111111

# This becomes "-0"

# Therefore:

# +0 = 00000000
# -0 = 11111111

# Two zeros exist.

# This is undesirable.


# ============================================================
# 2'S COMPLEMENT
# ============================================================

# Definition:
#
# Step 1:
# Take 1's complement
#
# Step 2:
# Add 1

# Example:

# 5

# 00000101

# 1's complement

# 11111010

# Add 1

# 11111011

# Therefore:

# -5 = 11111011


def twos_complement(num, bits=8):
    mask = (1 << bits) - 1
    return ((~num) + 1) & mask


print("\n2's Complement of 5 (8 bits):")
print(f"{twos_complement(5):08b}")

# Output:
# 11111011


# ============================================================
# IMPORTANT FORMULA
# ============================================================

# Negative number representation:

# -x = (~x) + 1

# Example:

x = 5

print("\n-x using formula:")
print((~x) + 1)

# Output:
# -5


# ============================================================
# WHY IS 2'S COMPLEMENT USED?
# ============================================================

# 1. Only one representation of zero
#
# 00000000
#
# No negative zero

# 2. Addition and subtraction become simple

# Example:

# +5

# 00000101

# -5

# 11111011

# Add:

# 00000101
# 11111011
# --------
#100000000

# Ignore carry

# 00000000

# Result = 0

# Same adder hardware can perform:
#
# Addition
# Subtraction
#
# Very efficient.


# ============================================================
# RANGE OF N-BIT SIGNED INTEGERS
# ============================================================

# Formula:

# -(2^(n-1)) to (2^(n-1)-1)

# Example:

# 8 bits

# -128 to 127

# Because:

# 10000000 = -128
# 01111111 = 127


# ============================================================
# HOW TO FIND NEGATIVE REPRESENTATION
# ============================================================

# Example:
#
# Represent -13 in 8 bits

# Step 1:
#
# +13

# 00001101

# Step 2:
#
# 1's complement

# 11110010

# Step 3:
#
# Add 1

# 11110011

# Therefore:

# -13 = 11110011


# ============================================================
# HOW TO RECOVER ORIGINAL NUMBER
# ============================================================

# Example:

# 11110011

# This is negative because MSB = 1

# Take 2's complement again

# 11110011

# 1's complement

# 00001100

# Add 1

# 00001101

# = 13

# Therefore original number = -13


# ============================================================
# PYTHON BITWISE NOT
# ============================================================

# Important interview question:

print("\n~5:")
print(~5)

# Output:
# -6

# Why?

# Formula:

# ~x = -(x + 1)

# Therefore:

# ~5
# = -(5 + 1)
# = -6


# ============================================================
# MOST IMPORTANT BIT TRICK
# ============================================================

# x & -x

# Extracts RIGHTMOST SET BIT

# Example:

# x = 12

# 1100

# -12 in 2's complement

# 0100 (relevant bit overlap)

# Therefore:

# 1100
# 0100
# ----
# 0100

# = 4

x = 12

print("\nRightmost set bit:")
print(x & -x)

# Output:
# 4


# ============================================================
# WHY DOES x & -x WORK?
# ============================================================

# Because:

# -x = (~x) + 1

# Example:

# x = 12

# 1100

# ~x

# 0011

# +1

# 0100

# Now:

# 1100
# 0100
# ----
# 0100

# Only the lowest set bit survives.

# Used in:

# 1. N Queens Bitmask
# 2. Fenwick Tree (BIT)
# 3. Subset DP
# 4. Competitive Programming

# ============================================================
# INTERVIEW MUST-REMEMBER FORMULAS
# ============================================================

# 1's complement:
#
# Flip all bits

# 2's complement:
#
# Flip all bits
# +
# 1

# Negative number:
#
# -x = (~x) + 1

# Bitwise NOT:
#
# ~x = -(x + 1)

# Remove rightmost set bit:
#
# x & (x - 1)

# Extract rightmost set bit:
#
# x & -x

# Check power of 2:
#
# x > 0 and (x & (x - 1)) == 0

# Count bits:
#
# repeatedly do:
#
# x &= (x - 1)

# Signed n-bit range:
#
# -(2^(n-1))
# to
# (2^(n-1)-1)

# Modern computers use:
#
# 2's Complement
#
# NOT
#
# 1's Complement
#
# because it avoids negative zero and
# simplifies arithmetic.