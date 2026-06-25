# Fruit into baskets
""" There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree.
The goal is to gather as much fruit as possible, adhering to the owner's stringent rules :

There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.
Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.
Once reaching a tree with fruit that cannot fit into any basket, stop.
Return the maximum number of fruits that can be picked. """
# Trick: Maximum length subarray with at most 2 types of numbers

def solve(arr):
    k = 2
    l = 0
    mx = 0
    mp = {}
    
    for r in range(len(arr)):
        mp[arr[r]] = mp.get(arr[r], 0) + 1
        
        if len(mp) > k:
            while len(mp) > k:
                mp[arr[l]] -= 1
                if mp[arr[l]] == 0: del mp[arr[l]]
                l += 1
        
        mx = max(mx, r - l + 1)
    
    return mx

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    
    # 1 2 3 2 2