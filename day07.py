import collections

tree, files = collections.defaultdict(lambda: []), {}

def part1(path):
    if path in files: return files[path], 0
    total, answer = zip(*(part1(f) for f in tree[path]))
    total, answer = sum(total), sum(answer)
    return total, answer if total >= 100000 else answer + total

def part2(path, target):
    if path in files: return files[path], float('+inf')
    total, answer = zip(*(part2(f, target) for f in tree[path]))
    total, answer = sum(total), min(answer)
    return total, answer if total < target else min(answer, total)

currdir = '/'
while True:
    try: line = input().split()
    except EOFError: break

    if line[0] == '$':
        if line[1] != 'cd': continue
        if line[2].startswith('/'):
            currdir = line[2]
        elif line[2] == '..':
            currdir = currdir[:currdir.rindex('/', 0, -1)+1]
        else:
            currdir += line[2] + '/'
    elif line[0] != 'dir':
        files[currdir + line[1]] = int(line[0])
        tree[currdir].append(currdir + line[1])
    else:    
        tree[currdir].append(currdir + line[1] + '/')

total, answer1 = part1('/')
_, answer2 = part2('/', total - 40000000)

print(answer1, answer2)
