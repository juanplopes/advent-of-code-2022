import sys, functools

def fx(x, depth = 10):
    if depth == 0: return x
    if isinstance(x, int): return [fx(x, depth-1)]
    return [fx(el, depth-1) for el in x]

lines = [fx(eval(x)) for x in sys.stdin.read().splitlines() if len(x.strip())]
total1 = sum(i+1 for i, (a, b) in enumerate(zip(lines[::2], lines[1::2])) if a < b)
sorted_lines = sorted(lines + [fx([[6]]), fx([[2]])])
a, b = (i+1 for i, v in enumerate(sorted_lines) if v in (fx([[2]]), fx([[6]])))
print(total1, a * b)