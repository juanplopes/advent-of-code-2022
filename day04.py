total1, total2 = 0, 0
while True:
    try: (a, b), (c, d) = [map(int, x.split('-')) for x in input().split(',')]
    except EOFError: break
    
    if min(b, d) - max(c, a) in (b - a, d - c):
        total1 += 1
    if min(b, d) - max(c, a) >= 0:
        total2 += 1

print(total1, total2)
