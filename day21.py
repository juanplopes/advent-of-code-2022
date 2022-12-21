import sys, re, operator
OP = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
T = {x[0]: x[1:] for x in (re.split('[\\s:]+', x) for x in sys.stdin.read().splitlines())}
def evaluate(T, x):
    if len(x) == 1: return complex(x[0])
    return OP[x[1]](evaluate(T, T[x[0]]), evaluate(T, T[x[2]]))

r2 = evaluate(T | {'humn': [1j]}, [T['root'][0], '-', T['root'][2]])
print(int(evaluate(T, T['root']).real), round(r2.real/-r2.imag))
