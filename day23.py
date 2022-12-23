import sys, re, collections

T = set((i, j)
     for i, row in enumerate(sys.stdin.read().splitlines())
     for j, cell in enumerate(row) if cell == '#')

def decide(round, i, j):
    if all(k1 == 0 and k2 == 0 or (i+k1, j+k2) not in T for k1 in (-1, 0, 1) for k2 in (-1, 0, 1)): return (i, j)
    opts = [
        (all((i-1, j+k) not in T for k in (-1, 0, 1)), (i-1, j)),
        (all((i+1, j+k) not in T for k in (-1, 0, 1)), (i+1, j)),
        (all((i+k, j-1) not in T for k in (-1, 0, 1)), (i, j-1)),
        (all((i+k, j+1) not in T for k in (-1, 0, 1)), (i, j+1))]
    for k in range(4):
        if opts[(k+round)%4][0]: return opts[(k+round)%4][1]
    return (i, j)

for r in range(1000):
    Q = collections.defaultdict(lambda: [])
    for i, j in T:
        Q[decide(r, i, j)].append((i, j))

    N = set()
    for k, v in Q.items():
        if len(v) == 1: N.add(k)
        else: N.update(v)
    if r == 9: 
        x, y = ((max(x) - min(x) + 1) for x in zip(*N))
        total1 = x * y - len(T)
    if N == T: 
        total2 = r+1
        break
    T = N

print(total1, total2)
