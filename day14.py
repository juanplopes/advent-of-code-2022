import sys

def parse(lines):
    for line in lines:
        pairs = [tuple(map(int, pair.split(','))) for pair in line.split(' -> ')]
        for (a, b), (c, d) in zip(pairs, pairs[1:]):
            for i in range(min(a, c), max(a, c)+1):
                for j in range(min(b, d), max(b, d)+1):
                    yield i, j

T = set(parse(sys.stdin.read().splitlines()))
maxy = max(y for _, y in T)
def solve(until):
    p = lambda x, y: (x, y) if (x, y) not in T and y < maxy+2 else None
    for i in range(1000000):
        x, y = 500, 0
        while True:
            nx, ny = p(x, y+1) or p(x-1, y+1) or p(x+1, y+1) or (None, None)
            if nx is None: break
            x, y = nx, ny
        if until(x, y): return i
        T.add((x, y))

total1 = solve(lambda x, y: y > maxy)
total2 = total1 + solve(lambda x, y: (x, y) == (500, 0)) + 1
print(total1, total2)