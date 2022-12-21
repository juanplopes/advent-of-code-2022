import sys, re
OP = {'+': lambda a, b: a+b, '-': lambda a, b: a-b, 
      '*': lambda a, b: a*b, '/': lambda a, b: a/b}
lines = [re.split('[\\s:]+', x) for x in sys.stdin.read().splitlines()]
T = {x[0] : x[1:] for x in lines}
def evaluate(T, node):
    if len(node) == 1: return complex(node[0])
    return OP[node[1]](evaluate(T, T[node[0]]), evaluate(T, T[node[2]]))

Q = dict(T) | {'humn': [1j]}
r2 = evaluate(Q, Q[Q['root'][0]]) - evaluate(Q, Q[Q['root'][2]])
print(int(evaluate(T, T['root']).real), round(r2.real/-r2.imag))
