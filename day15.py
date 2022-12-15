import sys, re, collections
lines = [tuple(map(int, re.findall('[-0-9]+', x))) 
            for x in sys.stdin.read().splitlines()]
T = collections.defaultdict(lambda: [])
B = collections.defaultdict(lambda: set())
def add(i, a1, a2):
    intervals = T[i]
    while True:
        for j, (b1, b2) in enumerate(intervals):
            if a1 <= b2 and b1 <= a2:
                intervals.pop(j)
                a1, a2 = min(a1, b1), max(a2, b2)
                break
        else: 
            T[i].append((a1, a2))
            return

for a, b, c, d in lines:
    print(a, b, c, d)
    B[d].add(c)
    dist = abs(c-a) + abs(d-b)
    add(b, a-dist, a+dist+1)
    for i in range(dist):
        add(b-i-1, a-dist+i+1, a+dist-i)
        add(b+i+1, a-dist+i+1, a+dist-i)

def solve(limit1, limit2):
    total1 = 0
    beacons = B[limit1]
    for a, b in T[limit1]:
        total1 += b - a - sum(a <= x < b for x in beacons)

    for i in range(limit2+1):
        intervals = T[i]
        intervals.sort()
        if len(intervals) != 1: print(i, intervals)
        j = 0
        while intervals[j][1] <= 0: j += 1
        if (intervals[j][0] > 0):
            return (total1, i)
        if (intervals[j][1] < limit2):
            return (total1, intervals[j][1]*4000000+i)

#print(*solve(10, 20))
print(*solve(2000000, 4000000))
