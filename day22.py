import sys, re, collections

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
T = [list(x) for x in sys.stdin.read().splitlines()]
def solve(*wrap):
    def cells(x, y, d):
        for i in range(50): 
            yield (x * 50 + 49 * (d == 1) + i * (d in (0, 2)), 
                y * 50 + 49 * (d == 0) + i * (d in (1, 3)))

    W = {}
    for x1, y1, d1, x2, y2, d2, inv in wrap:
        for a, b in zip(cells(x1, y1, d1), list(cells(x2, y2, d2))[::1-2*inv]):
            W[(*a, d1)] = (*b, (d2-2)%4)
            W[(*b, d2)] = (*a, (d1-2)%4)

    x, y, d = 0, min(y for x, y, _ in W if x == 0), 0
    for cmd in re.findall(r'\d+|[RL]+', ''.join(T[-1])):
        if cmd in 'RL': d = (d + (1 - 2 * (cmd == 'L'))) % 4
        else:
            for i in range(int(cmd)):
                dx, dy = D[d]
                nx, ny, nd = W.get((x, y, d), (x + dx, y + dy, d))
                if T[nx][ny] == '#': break
                x, y, d = nx, ny, nd
    return 1000*(x+1)+4*(y+1)+d    

total1 = solve((0, 1, 2, 0, 2, 0, False),
                (0, 1, 3, 2, 1, 1, False),
                (0, 2, 1, 0, 2, 3, False),
                (1, 1, 2, 1, 1, 0, False),
                (2, 0, 2, 2, 1, 0, False),
                (2, 0, 3, 3, 0, 1, False),
                (3, 0, 0, 3, 0, 2, False))
total2 = solve((0, 1, 2, 2, 0, 2, True),
                (0, 1, 3, 3, 0, 2, False),
                (0, 2, 0, 2, 1, 0, True),
                (0, 2, 1, 1, 1, 0, False),
                (0, 2, 3, 3, 0, 1, False),
                (1, 1, 2, 2, 0, 3, False),
                (2, 1, 1, 3, 0, 0, False))
print(total1, total2)