# Count prime in range L-R

def solve(queries):
    mx = max(r for _, r in queries)

    prime = [True] * (mx + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(mx ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, mx + 1, i):
                prime[j] = False

    prefix = [0] * (mx + 1)

    for i in range(1, mx + 1):
        prefix[i] = prefix[i - 1] + prime[i]

    res = []

    for l, r in queries:
        res.append(prefix[r] - prefix[l - 1])

    return res


if __name__ == "__main__":
    n = int(input())

    queries = []

    for _ in range(n):
        l, r = map(int, input().split())
        queries.append((l, r))

    print(*solve(queries))