"""
STRING HASHING (POLYNOMIAL ROLLING HASH)
========================================

Hashing converts a string into a numeric value called a HASH VALUE.

Why hashing?
------------
1. Fast string comparison
   - Comparing long strings directly takes O(n)
   - Comparing hashes takes O(1)

2. Efficient searching
   - Used in Rabin-Karp pattern matching

3. Duplicate / anagram detection
   - Strings with same structure can be grouped quickly

4. Prefix / substring queries
   - Substring hashes can be computed in O(1)

------------------------------------------------------------

Polynomial hashing works because
- characters are mapped to numbers
- powers encode positions
- modulo keeps numbers manageable
- primes reduce collisions

------------------------------------------------------------

POLYNOMIAL ROLLING HASH
-----------------------

For string s:

Hash(s) =
(s[0] * p^0 +
 s[1] * p^1 +
 s[2] * p^2 + ...
 s[n-1] * p^(n-1)) % m

where:
- s[i] = mapped numeric value of character
- p    = prime base (commonly 31 or 53)
- m    = large prime modulus (1e9+7, 1e9+9)

Common mapping:
'a' -> 1
'b' -> 2
...
'z' -> 26

------------------------------------------------------------

EXAMPLE
-------

s = "abc"

Using:
p = 31
m = 1e9+9

Hash =
(1 * 31^0 +
 2 * 31^1 +
 3 * 31^2) % m

= (1 + 62 + 2883)
= 2946


# Common prime bases:

31 -> lowercase letters
53 -> upper + lowercase
137 -> large alphbets

# Modulo to keep the values from overflowing (hash %= m)

m = 1e9+7
m = 1e9+9

# Equal strings ALWAYS have equal hashes
# Different strings USUALLY have different hashes
# Not guaranteed because of collisions
------------------------------------------------------------

COLLISIONS
----------

Two different strings can produce same hash.

To reduce collisions:
1. Use large prime modulus
2. Use good prime base
3. Use double hashing

------------------------------------------------------------

TIME COMPLEXITY
---------------

Build hash:
O(n)

Substring hash query:
O(1) after preprocessing

------------------------------------------------------------

IMPORTANT APPLICATIONS
----------------------

1. Rabin-Karp algorithm
2. Pattern matching
3. String comparison
4. Finding repeated substrings
5. Palindrome checking
6. Competitive Programming string problems

------------------------------------------------------------
"""


# Compute polynomial rolling hash of a string

def string_hash(s, p=31, m=10**9 + 9):
    h = 0
    power = 1

    for ch in s:
        val = ord(ch) - ord('a') + 1

        h = (h + val * power) % m
        power = (power * p) % m
        print(ch, h, power)

    return h


if __name__ == "__main__":
    s = input()

    print("Hash Value:", string_hash(s))