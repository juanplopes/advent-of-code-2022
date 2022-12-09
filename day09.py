def solve(moves, knots):
    X = [[0, 0] for _ in range(knots)]
    visited = set()
    for a, b in moves:
        for _ in range(int(b)):
            X[0][0] += {'R': 1, 'L': -1}.get(a, 0)
            X[0][1] += {'D': 1, 'U': -1}.get(a, 0)
            for j in range(1, knots):
                if (X[j-1][0]-X[j][0])**2 + (X[j-1][1]-X[j][1])**2 > 2:
                    X[j][0] += max(-1, min(1, X[j-1][0] - X[j][0]))
                    X[j][1] += max(-1, min(1, X[j-1][1] - X[j][1]))
            visited.add(tuple(X[-1]))
    return len(visited)

moves = []
while True:
    try: moves.append(input().split())
    except EOFError: break

print(solve(moves, 2), solve(moves, 10))
