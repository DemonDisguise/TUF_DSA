# reverse an array
def rec1(l: int, r: int, arr: list[int]) -> list[int]:
    if l >= r:
        return 
    
    arr[l], arr[r] = arr[r], arr[l]
    rec1(l + 1, r - 1, arr)

lst: list[int] = list(map(int, input().split()))
rec1(0, len(lst) - 1, lst)
print(*lst)