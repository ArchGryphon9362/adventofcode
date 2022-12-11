file = open('day1.txt', 'r')
inputs = file.read()
file.close()

elves = inputs.split('\n\n')
elves = [elf.split() for elf in elves]
elves = [[int(number) for number in elf] for elf in elves]
elves = [sum(elf) for elf in elves]
top_elf = max(elves)
print("Part 1:")
print(top_elf)

print()

elves.sort()
top_3 = elves[-1] + elves[-2] + elves[-3]
print("Part 2:")
print(top_3)
