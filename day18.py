import sys, collections
cubes = set(tuple(map(int, x.split(','))) for x in sys.stdin.read().splitlines())
mins, maxs = [min(x)-1 for x in zip(*cubes)], [max(x)+1 for x in zip(*cubes)]

def neighbors(x, y, z):
    yield from ((x+1, y, z), (x, y+1, z), (x, y, z+1))
    yield from ((x-1, y, z), (x, y-1, z), (x, y, z-1))

total1 = sum(n not in cubes for c in cubes for n in neighbors(*c))
total2 = 0
Q, visited = collections.deque([tuple(mins)]), set(cubes)
while len(Q):
    for cube in neighbors(*Q.popleft()):
        if not all(a <= x <= b for a, b, x in zip(mins, maxs, cube)): continue
        total2 += cube in cubes
        if cube in visited: continue
        visited.add(cube)
        Q.append(cube)
print(total1, total2)