jets = input()
pieces = (((0, 0), (1, 0), (2, 0), (3, 0)),
        ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
        ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (0, 1), (1, 0), (1, 1)))

def free(T, x, y): 
    return x >= 0 and x < 7 and y > 0 and (x, y) not in T

def can_move(T, piece, x, y):
    return all(free(T, x+dx, y+dy) for dx, dy in pieces[piece])

def place(T, jet, maxy, piece):
    x, y = 2, maxy + 4
    while True:
        if jets[jet] == '<' and can_move(T, piece, x-1, y): x -= 1
        if jets[jet] == '>' and can_move(T, piece, x+1, y): x += 1
        jet = (jet + 1) % len(jets)
        if can_move(T, piece, x, y-1): y -= 1
        else: break
    T.update((x+dx, y+dy) for dx, dy in pieces[piece])
    return (jet, 
            max(maxy, max((y+dy) for _, dy in pieces[piece])), 
            (piece + 1) % len(pieces))

def ground_state(T, maxy):
    def dfs(x, y, visited):
        if not free(T, x, maxy+y) or (x, y) in visited: return
        visited.add((x, y))
        for nx, ny in ((x-1, y), (x+1,y), (x, y-1)): 
            dfs(nx, ny, visited)
    state = set()
    for x in range(7): 
        dfs(x, 0, state)
    return tuple(sorted(state))

def solve(count):
    T, cycle = set(), dict()
    jet, maxy, piece, additional = 0, 0, 0, 0

    while count > 0:
        jet, maxy, piece = place(T, jet, maxy, piece)
        count -= 1

        ground = ground_state(T, maxy)
        if (jet, piece, ground) in cycle:
            oldmaxy, oldcount = cycle[jet, piece, ground]
            dcount, dmaxy = oldcount - count, maxy - oldmaxy
            if dcount < count:
                additional += dmaxy * (count // dcount)
                count %= dcount

        cycle[jet, piece, ground] = (maxy, count)
    return additional + maxy

print(solve(2022), solve(1000000000000))
