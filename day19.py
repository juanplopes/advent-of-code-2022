import sys, re, functools

def timeto(req, cur, prod):
    return max(((req - cur + prod - 1) // prod), 0) + 1

def T(blueprint, mins):
    _, co, cc, cb1, cb2, cg1, cg2 = blueprint
    mo, maxx = max(cc, cb1, cg1), 0
    def dfs(g, t, o, c, b, ro, rc, rb):
        nonlocal maxx
        maxg = g+t*t-t
        if t <= 0 or maxg <= maxx: return
        maxx = max(maxx, g)
        if rb: # create geode robot?
            dt = max(timeto(cg1, o, ro), timeto(cg2, b, rb))
            dfs(g + max(t-dt, 0), t-dt, o+dt*ro-cg1, c+dt*rc, b+dt*rb-cg2, ro, rc, rb)
        if maxg <= maxx: return
        if rc and b+(rb*t) < cg2*t: #create obsidian robot?
            dt = max(timeto(cb1, o, ro), timeto(cb2, c, rc))
            dfs(g, t-dt, o+dt*ro-cb1, c+dt*rc-cb2, b+dt*rb, ro, rc, rb+1)
        if maxg <= maxx: return
        if c+(rc*t) < cb2*t: # create clay robot?
            dt = timeto(cc, o, ro)
            dfs(g, t-dt, o+dt*ro-cc, c+dt*rc, b+dt*rb, ro, rc+1, rb)
        if maxg <= maxx: return
        if o+(ro*t) < mo*t: # create ore robot?
            dt = timeto(co, o, ro)
            dfs(g, t-dt, o+dt*ro-co, c+dt*rc, b+dt*rb, ro+1, rc, rb)

    dfs(0, mins, 0, 0, 0, 1, 0, 0)
    return maxx    

lines = [tuple(map(int, re.findall('\\d+', x))) for x in sys.stdin.read().splitlines()]
total1 = sum(x[0] * T(x, 24) for x in lines)
total2 = functools.reduce(lambda a, b: a*b, (T(x, 32) for x in lines[:3]), 1)
print(total1, total2)
