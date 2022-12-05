import collections, copy

crates = []
while len(crates) == 0 or len(crates[-1]):
    try: crates.append(input()[1::4])
    except EOFError: break

stacks1 = collections.defaultdict(lambda: [])
for line in crates[-3::-1]:
    for i, crate in enumerate(line):
        if crate == ' ': continue
        stacks1[crates[-2][i]].append(crate)
stacks2 = copy.deepcopy(stacks1)

while True:
    try: _, n, _, a, _, b = input().split()
    except EOFError: break
    stacks1[b] += stacks1[a][:-int(n)-1:-1]
    stacks2[b] += stacks2[a][-int(n):]
    del stacks1[a][-int(n):]
    del stacks2[a][-int(n):]

print(''.join(x[-1] for x in stacks1.values()),
      ''.join(x[-1] for x in stacks2.values()))
