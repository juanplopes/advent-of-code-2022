import sys, re
lines = [re.findall('[-0-9]+', x) for x in sys.stdin.read().splitlines()]
T = [tuple(map(int, line)) for line in lines]
B = set((int(c), int(d)) for _, _, c, d in T)

def find(a, b, c, d, y):
    dist = abs(c-a) + abs(d-b)
    return (a - (dist - abs(y - b)), a + (dist - abs(y - b)) + 1)

def find_all(y):
    return sorted(find(*item, y) for item in T)

def find_disjoint(y):
    maxx = float('-inf')
    for a, b in find_all(y):
        if b - max(maxx, a) > 0: yield max(maxx, a), b
        maxx = max(maxx, b)

def count_beacons(a, b, y):
    return sum(a <= xb < b for xb, yb in B if yb == y)

def contains(a, b, c, d, x1, y1, x2, y2):
    q1, r1 = find(a, b, c, d, y1)
    q2, r2 = find(a, b, c, d, y2-1)
    return q1 <= x1 <= x2 <= r1 and q2 <= x1 <= x2 <= r2

def search_single(x1, y1, x2, y2):
    if any(contains(*item, x1, y1, x2, y2) for item in T): return None
    if x1 >= x2 or y1 >= y2: return
    if x2 - x1 == 1 and y2 - y1 == 1: return (x1, y1)
    xm, ym = (x1+x2)>>1, (y1+y2)>>1
    return (search_single(x1, y1, xm, ym) or
            search_single(xm, y1, x2, ym) or
            search_single(x1, ym, xm, y2) or
            search_single(xm, ym, x2, y2))

def solve(limit1, limit2):
    total1 = sum(b-a-count_beacons(a, b, limit1) for a, b in find_disjoint(limit1))
    x, y = search_single(0, 0, limit2, limit2)
    return (total1, x*4000000+y)

#print(*solve(10, 20))
print(*solve(2000000, 4000000))
