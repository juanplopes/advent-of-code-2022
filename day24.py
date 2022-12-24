import sys, collections
T = sys.stdin.read().splitlines()
N, M = len(T) - 2, len(T[0]) - 2
def solve(st, si, sj, ei, ej):
    Q = {(si, sj, st)}
    while Q:
        i, j, t = next(iter(Q))
        Q.remove((i, j, t))
        if i == ei and j == ej: return t
        for ni, nj in (i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if not 0 <= ni < len(T) or not 0 <= nj < len(T[0]) or T[ni][nj] == '#': continue
            if T[1+(ni-t-2)%N][nj] == 'v' or T[1+(ni+t)%N][nj] == '^': continue
            if T[ni][1+(nj-t-2)%M] == '>' or T[ni][1+(nj+t)%M] == '<': continue
            Q.add((ni, nj, t + 1))

t1 = solve(0, 0, 1, len(T)-1, len(T[0])-2)
t2 = solve(solve(t1, len(T)-1, len(T[0])-2, 0, 1), 0, 1, len(T)-1, len(T[0])-2)
print(t1, t2)
