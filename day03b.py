def pri(x):
    return 1 + ord(x) - ord('a') if 'a' <= x <= 'z' else 27 + ord(x) - ord('A')

total = 0
while True:
    try: a, b, c = input(), input(), input()
    except EOFError: break
    
    repeated = set(a).intersection(b).intersection(c)
    total += sum(map(pri, repeated))

print(total)
