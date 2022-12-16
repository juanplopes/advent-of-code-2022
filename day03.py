import sys 

def pri(x):
    return 1 + ord(x) - ord('a') if 'a' <= x <= 'z' else 27 + ord(x) - ord('A')

lines = sys.stdin.read().splitlines()

def solve(rucksacks):
    return sum(pri(y) for x in rucksacks for y in set.intersection(*map(set, x)))

total1 = solve((x[:len(x) // 2], x[len(x) // 2:]) for x in lines)
total2 = solve(zip(lines[::3], lines[1::3], lines[2::3]))
print(total1, total2)
