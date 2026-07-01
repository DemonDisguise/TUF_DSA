# Lemonade change
"""Each lemonade costs $5. Given an array representing a queue of customers and the value of bills they hold, determine if it is possible to provide correct change to each customer. Customers can only pay with 5$, 10$ or 20$ bills and we initially do not have any change at hand. 
 Return true, if it is possible to provide correct change for each customer otherwise return false. """

from typing import List

def solve(bills: List[int]) -> bool:
    fives, tens = 0, 0
    
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives > 0:
                fives -= 1
                tens += 1
            else:
                return False
        else:
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True

if __name__ == "__main__":
    bills = list(map(int, input().split()))
    print(solve(bills))
    
    # 5 5 10 10 20
