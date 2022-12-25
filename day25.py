import sys
A = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
B = {v: k for k, v in A.items()}

total = 0
for line in sys.stdin.read().splitlines():
    for i, c in enumerate(line[::-1]):
        total += A[c] * 5**i

answer = ''
while total:
    digit = (total+2)%5-2
    answer = B[digit] + answer
    total = (total-digit)//5

print(answer)