import sys, re, functools, heapq

def res(req, cur, prod):
    return max((req - cur + prod - 1) // prod, 0) + 1

def T(blueprint, mins):
    _, co, cc, cb1, cb2, cg1, cg2 = blueprint
    mo = max(cc, cb1, cg1)
    Q, V, maxx = [], {}, 0
    def p(g, t, o, c, b, ro, rc, rb):
        nonlocal maxx
        k = (t, o, c, b, ro, rc, rb)
        if t < 0 or -g+t*t-t < maxx or V.get(k, -1) >= -g: return
        maxx = max(maxx, -g)
        V[k] = -g
        heapq.heappush(Q, (g, t, o, c, b, ro, rc, rb))

    p(0, mins, 0, 0, 0, 1, 0, 0)
    while Q:
        g, t, o, c, b, ro, rc, rb = heapq.heappop(Q)
        if -g+t*t-t < maxx: continue
        if rb:
            dt = max(res(cg1, o, ro), res(cg2, b, rb))
            p(g - max(t-dt, 0), t-dt, o+dt*ro-cg1, c+dt*rc, b+dt*rb-cg2, ro, rc, rb)
        if rc and rb < cg2 and b+(rb*t) < cg2*t:
            dt = max(res(cb1, o, ro), res(cb2, c, rc))
            p(g, t-dt, o+dt*ro-cb1, c+dt*rc-cb2, b+dt*rb, ro, rc, rb+1)
        if rc < cb2 and c+(rc*t) < cb2*t:
            dt = res(cc, o, ro)
            p(g, t-dt, o+dt*ro-cc, c+dt*rc, b+dt*rb, ro, rc+1, rb)
        if ro < mo and o+(ro*t) < mo*t:
            dt = res(co, o, ro)
            p(g, t-dt, o+dt*ro-co, c+dt*rc, b+dt*rb, ro+1, rc, rb)
    return maxx    

lines = [tuple(map(int, re.findall('\\d+', x))) for x in sys.stdin.read().splitlines()]
total1 = sum(x[0] * T(x, 24) for x in lines)
total2 = functools.reduce(lambda a, b: a*b, (T(x, 32) for x in lines[:3]), 1)
print(total1, total2)
