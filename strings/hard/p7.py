def solve(s: str) -> str:

    rev = s[::-1]

    temp = s + "#" + rev

    lps = [0] * len(temp)

    prev = 0
    i = 1

    while i < len(temp):

        if temp[i] == temp[prev]:
            prev += 1
            lps[i] = prev
            i += 1

        else:
            if prev == 0:
                lps[i] = 0
                i += 1
            else:
                prev = lps[prev - 1]

    longest_pal_prefix = lps[-1]

    remaining = s[longest_pal_prefix:]

    return remaining[::-1] + s

if __name__ == "__main__":
    s = input()
    print(solve(s))