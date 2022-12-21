import sys, re
OP = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__floordiv__}
lines = [re.split('[\\s:]+', x) for x in sys.stdin.read().splitlines()]
T = {x[0] : x[1:] for x in lines}
def evaluate(T, monkey):
    node = T[monkey]
    if node == ['x']: return node
    if len(node) == 1: return int(node[0])
    a, b = evaluate(T, node[0]), evaluate(T, node[2])
    if not isinstance(a, int) or not isinstance(b, int): 
        return [a, node[1], b]
    return OP[node[1]](a, b)

def solve2():
    Q = dict(T)
    Q['root'] = [Q['root'][0], '=', Q['root'][2]]
    Q['humn'] = ['x']
    expr, _,c  = evaluate(Q, 'root')
    if isinstance(expr, int): c, expr = expr, c
    while expr != ['x']:
        a, op, b = expr
        if isinstance(a, int):
            expr, c = {'+': (b, c-a), '-': (b, a-c), '*': (b, c//a), '/': (b, a//c)}[op]
        if isinstance(b, int):
            expr, c = {'+': (a, c-b), '-': (a, b+c), '*': (a, c//b), '/': (a, b*c)}[op]
    return c

print(evaluate(T, 'root'), solve2())