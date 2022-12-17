import sys
def execute(program):
    X = 1
    for line in program:
        yield X
        if line[0] == 'addx':
            yield X
            X += int(line[1])

S = list(execute(line.split() for line in sys.stdin.read().splitlines()))
print(sum(S[i-1]*i for i in [20, 60, 100, 140, 180, 220]))

for i in range(6):
    print(''.join(' █'[abs(S[i*40+j] - j) <= 1] for j in range(40)))
