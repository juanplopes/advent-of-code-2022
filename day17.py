J = input()
P = (((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (0, 1), (1, 0), (1, 1)))

def free(T, x, y): 
    return x >= 0 and x < 7 and y > 0 and (x, y) not in T

def can_move(T, piece, x, y):
    return all(free(T, x+dx, y+dy) for dx, dy in P[piece])

def place(T, jet, piece, maxy):
    x, y = 2, maxy + 5
    while can_move(T, piece, x, y-1):
        y -= 1
        if J[jet] == '<' and can_move(T, piece, x-1, y): x -= 1
        if J[jet] == '>' and can_move(T, piece, x+1, y): x += 1
        jet = (jet + 1) % len(J)
    newcells = [(x+dx, y+dy) for dx, dy in P[piece]]
    T.update(newcells)
    return jet, (piece + 1) % len(P), max(maxy, max(y for _, y in newcells))

def ground_shape(T, maxy):
    def dfs(x, y, visited):
        if not free(T, x, maxy+y) or (x, y) in visited or len(visited) > 20: return
        visited.add((x, y))
        for nx, ny in ((x-1, y), (x+1,y), (x, y-1)): 
            dfs(nx, ny, visited)
    state = set()
    for x in range(7): 
        dfs(x, 0, state)
    return tuple(state) if len(state) <= 20 else None

def solve(count):
    T, cycles = set(), dict()
    jet, maxy, piece, additional = 0, 0, 0, 0

    while count > 0:
        jet, piece, maxy = place(T, jet, piece, maxy)
        count -= 1

        ground = ground_shape(T, maxy)
        if ground is None: continue

        if (jet, piece, ground) in cycles:
            oldmaxy, oldcount = cycles[jet, piece, ground]
            additional += (maxy - oldmaxy) * (count // (oldcount - count))
            count %= oldcount - count
        cycles[jet, piece, ground] = (maxy, count)
    return maxy + additional

print(solve(2022), solve(1000000000000))
