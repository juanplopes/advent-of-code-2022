import sys
A = ''.join(sys.stdin.read().split('\n'))
X = 1

P = { '..': -2, '#.': -1, '##': 0, '.#': 2 }
for index, pair in enumerate(zip(A[2::2], A[3::2]), start=1):
    target = index*2%40 + P[''.join(pair)]
    print('addx', target - X)
    X = target
print('addx 0')