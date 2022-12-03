def pri(x):
    return 1 + ord(x) - ord('a') if 'a' <= x <= 'z' else 27 + ord(x) - ord('A')

total = 0
while True:
    try: rucksack = input()
    except EOFError: break
    
    mid = len(rucksack) // 2
    repeated = set(rucksack[:mid]).intersection(set(rucksack[mid:]))
    total += sum(map(pri, repeated))

print(total)
