import itertools

grid = []
while True:
    try: grid.append(input())
    except EOFError: break

total1, total2 = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        left = [grid[i][k] < grid[i][j] for k in range(j-1, -1, -1)]
        right = [grid[i][k] < grid[i][j] for k in range(j+1, len(grid[i]))]
        up = [grid[k][j] < grid[i][j] for k in range(i-1, -1, -1)]
        down = [grid[k][j] < grid[i][j] for k in range(i+1, len(grid))]
        f2 = lambda dir: (not all(dir)) + sum(itertools.takewhile(lambda x:x, dir))

        total1 += all(left) or all(right) or all(up) or all(down)
        total2 = max(total2, f2(left) * f2(right) * f2(up) * f2(down))

print(total1, total2)        
