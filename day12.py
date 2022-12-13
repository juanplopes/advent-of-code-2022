import sys, collections

def solve(grid, *start):
    Q = collections.deque((i, j, 0, 'a') for i in range(len(grid)) 
                    for j in range(len(grid[i])) 
                    if grid[i][j] in start)
    visited = set((i, j) for i, j, _, _ in Q)

    while len(Q):
        i, j, d, a = Q.popleft()
        if grid[i][j] == 'E': return d
        for ni, nj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if not 0 <= ni < len(grid): continue
            if not 0 <= nj < len(grid[ni]): continue
            if (ni, nj) in visited: continue
            b = grid[ni][nj].replace('E', 'z')
            if ord(b) > ord(a) + 1: continue
            visited.add((ni, nj))
            Q.append((ni, nj, d + 1, b))

grid = sys.stdin.read().splitlines()
print(solve(grid, 'S'), solve(grid, 'S', 'a'))