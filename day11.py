import sys, functools

def parse(lines, index):
    items = [int(x.strip()) for x in lines[index+1].split(':')[1].split(',')]
    expr = lines[index+2].split('=')[1].strip()
    div = int(lines[index+3].split('by')[1].strip())
    m1 = int(lines[index+4].split('monkey')[1].strip())
    m2 = int(lines[index+5].split('monkey')[1].strip())
    return (items, expr, div, m1, m2, [0])

def solve(monkeys, relief, rounds):
    divlimit = functools.reduce(lambda a, b: a*b[2], monkeys, 1)
    def step(items, expr, div, m1, m2, stats):
        for item in items:
            stats[0] += 1
            new = eval(expr, {'old': item}) // relief % divlimit
            monkeys[m2 if new % div else m1][0].append(new)
        items.clear()
    for _ in range(rounds):
        for monkey in monkeys:
            step(*monkey)
    a, b = sorted(m[5][0] for m in monkeys)[-2:]
    return a * b

lines = sys.stdin.read().splitlines()
monkeys1 = [parse(lines, i) for i in range(0, len(lines), 7)]
monkeys2 = [parse(lines, i) for i in range(0, len(lines), 7)]
print(solve(monkeys1, 3, 20), solve(monkeys2, 1, 10000))