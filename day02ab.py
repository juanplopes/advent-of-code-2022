def score(a, b):
    return b + 1 + (b == a) * 3 + (b == (a + 1) % 3) * 6

total1, total2 = 0, 0
while True:
    try: a, b = input().split()
    except EOFError: break
    
    a = ord(a) - ord('A')
    b = ord(b) - ord('X')
    c = (a + (b + 2)) % 3

    total1 += score(a, b)
    total2 += score(a, c)

print(total1, total2)
