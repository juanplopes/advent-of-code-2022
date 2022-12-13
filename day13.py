import sys, functools

def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int): return a - b
    if isinstance(a, int): return cmp([a], b)
    if isinstance(b, int): return cmp(a, [b])
    for x, y in zip(a, b):
        c = cmp(x, y)
        if c != 0: return c
    return len(a) - len(b)

lines = [eval(x) for x in sys.stdin.read().splitlines() if len(x.strip())]
total1 = sum(i//2+1 for i in range(0, len(lines), 2) if cmp(*lines[i:i+2]) < 0)
lines += [[[6]], [[2]]]
lines.sort(key=functools.cmp_to_key(cmp))
a, b = (i+1 for i, v in enumerate(lines) if v in ([[2]], [[6]]))
print(total1, a * b)