import sys
T = [[int(x), None] for x in sys.stdin.read().splitlines()]
for i in range(len(T)-1, 0, -1):
    T[i-1][1] = T[i]

def solve(start, key, times):
    Q = list(T)
    for _ in range(times):
        cur = start
        while cur != None:
            idx = Q.index(cur)
            Q.pop(idx)
            Q.insert((idx + cur[0] * key) % len(Q), cur)
            cur = cur[1]
    zero = [x for x, _ in Q].index(0)
    return sum(Q[(zero+i) % len(Q)][0] * key for i in (1000, 2000, 3000))

print(solve(T[0], 1, 1), solve(T[0], 811589153, 10))
