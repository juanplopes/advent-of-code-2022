import sys, re, collections

def T(blueprint, mins):
    _, co, cc, cb1, cb2, cg1, cg2 = blueprint
    mo = max(co, cc, cb1, cg1)
    T = {(0, 0, 0, 1, 0, 0): 0}
    for minute in range(mins, 1, -1):
        maxg = max(T.values())
        Q = {}
        def p(v, *k): Q[k] = max(Q.get(k, 0), v)
        for (o, c, b, ro, rc, rb), g in T.items():
            if g+minute*minute-minute < maxg: continue
            bo = o >= co and ro < mo and o+(ro*minute) < mo*minute
            bc = o >= cc and rc < cb2 and c+(rc*minute) < cb2*minute
            bb = o >= cb1 and c >= cb2 and rb < cg2
            bg = o >= cg1 and b >= cg2
            if minute >= 2:
                if bo: p(g, o+ro-co, c+rc, b+rb, ro+1, rc, rb)
                if bc: p(g, o+ro-cc, c+rc, b+rb, ro, rc+1, rb)
                if bb: p(g, o+ro-cb1, c+rc-cb2, b+rb, ro, rc, rb+1)
                if not all((bo, bc, bb, bg)): p(g, o+ro, c+rc, b+rb, ro, rc, rb)
            if bg: p(g + (minute-1), o+ro-cg1, c+rc, b+rb-cg2, ro, rc, rb)
        T = Q
    return max(T.values())

lines = [tuple(map(int, re.findall('\\d+', x))) for x in sys.stdin.read().splitlines()]
total1 = sum(x[0] * T(x, 24) for x in lines)
a, b, c = (T(x, 32) for x in lines[:3])
print(total1, a * b * c)