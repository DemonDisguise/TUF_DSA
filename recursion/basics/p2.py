# Print all subsequences

def f(ind: int, arr: list[int], n, res: list[int]):
    if (ind >= n):
        if res:  print(res) 
        return
    res.append(arr[ind])
    f(ind + 1, arr, n, res)
    res.remove(arr[ind])
    f(ind + 1, arr, n, res)

if __name__ == "__main__":
    arr = [3,1,2]
    res = []
    f(0, arr, len(arr), res)