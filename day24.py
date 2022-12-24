import sys, collections
T = sys.stdin.read().splitlines()
N, M = len(T)-2, len(T[0])-2
FN, FS = ([set(i for i in range(N) if T[i+1][j+1] == c) for j in range(M)] for c in '^v')
FW, FE = ([set(j for j in range(M) if T[i+1][j+1] == c) for i in range(N)] for c in '<>')

def solve(st, si, sj, ei, ej):
    queue, visited = collections.deque([(si, sj, st)]), set()
    while queue:
        i, j, t = queue.popleft()
        if i == ei and j == ej: return t
        for ni, nj in (i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if not -1 <= ni <= N or not -1 <= nj <= M or T[ni+1][nj+1] == '#': continue
            if 0 <= nj < M and ((ni-t-1)%N in FS[nj] or (ni+t+1)%N in FN[nj]): continue
            if 0 <= ni < N and ((nj-t-1)%M in FE[ni] or (nj+t+1)%M in FW[ni]): continue
            if (ni, nj, (t + 1) % (M * N)) in visited: continue
            visited.add((ni, nj, (t + 1) % (M * N)))
            queue.append((ni, nj, t + 1))

ta = solve(0, -1, 0, N, M-1)
tb = solve(ta, N, M-1, -1, 0)
tc = solve(tb, -1, 0, N, M-1)
print(ta, tc)
