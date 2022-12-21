import sys, re, math
OP = {'+': lambda a, b: a+b, '-': lambda a, b: a-b, 
      '*': lambda a, b: a*b, '/': lambda a, b: a/b}
lines = [re.split('[\\s:]+', x) for x in sys.stdin.read().splitlines()]
T = {x[0] : x[1:] for x in lines}
def evaluate(T, monkey):
    node = T[monkey]
    if len(node) == 1: return complex(node[0])
    return OP[node[1]](evaluate(T, node[0]), evaluate(T, node[2]))

Q = dict(T)
Q['humn'] = [1j]
r2 = evaluate(Q, Q['root'][0]) - evaluate(Q, Q['root'][2])     
print(int(evaluate(T, 'root').real), round(r2.real/-r2.imag))
