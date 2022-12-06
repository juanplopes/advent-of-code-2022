def solve(s, n):
    for i, chars in enumerate(zip(*(s[i:] for i in range(n)))):
        if len(set(chars)) == n:
            return i + n

s = input()
print(solve(s, 4), solve(s, 14))

