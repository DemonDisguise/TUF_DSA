Binary search:

-> When to use 
- use l <= r when
    - searching exact target
    - answer can be mid
    - you may return inside loop
- use l < r when
    - shrinking to one answer 
    - finding boundary/min/max/first true
    - answer is final pointer position

Strings:

-> If repetitive updates on strings better to use list and store and use "".join to get the final string.
-> Reason: everytime using += python creates new string and then stores it and recreating costs
-> += repetitive gets to O(n^2) while list is just 
O(n)

KMP - Exact matching
Rabin-karp - multiple patterns/hashing
Z algorithm - prefix matching problems

# Linked List
- Use dummy when:
    - deleting nodes, merging lists, returning new head
    - it helps avoid head edge cases