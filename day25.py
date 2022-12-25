import sys
total = 0
for line in sys.stdin.read().splitlines():
    for i, c in enumerate(line[::-1]):
        total += ("=-012".index(c)-2) * 5**i
answer = ''
while total:
    digit = (total+2)%5-2
    answer = "=-012"[digit+2] + answer
    total = (total-digit)//5
print(answer)