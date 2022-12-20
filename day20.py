import sys
T = [int(x) for x in sys.stdin.read().splitlines()]

def solve(key, times):
    I = list(range(len(T)))
    for _ in range(times):
        for i in range(len(T)):
            idx = I.index(i)
            I.pop(idx)
            I.insert((idx + T[i] * key) % len(I), i)
    zero = I.index(T.index(0))
    return sum(T[I[(zero+i) % len(I)]] * key for i in (1000, 2000, 3000))

print(solve(1, 1), solve(811589153, 10))
