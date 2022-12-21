import sys, re, operator
OP = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
T = {x[0]: x[1:] for x in (re.split('[\\s:]+', x) for x in sys.stdin.read().splitlines())}
def ev(T, x):
    return complex(x[0]) if len(x) == 1 else OP[x[1]](ev(T, T[x[0]]), ev(T, T[x[2]]))

r2 = ev(T | {'humn': [1j]}, [T['root'][0], '-', T['root'][2]])
print(int(ev(T, T['root']).real), round(r2.real/-r2.imag))
