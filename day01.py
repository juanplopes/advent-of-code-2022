elves = []
while True:
    calories = []
    while True:
        try: calories.append(int(input()))
        except EOFError: break
        except ValueError: break
    if not len(calories): break
    elves.append(sum(calories))
elves.sort(reverse = True)

print(elves[0], sum(elves[:3]))
