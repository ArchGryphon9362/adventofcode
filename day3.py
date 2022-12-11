file = open('day3.txt', 'r')
og_inputs = file.read()
file.close()

inputs = og_inputs.split()
inputs = [[rucksack[:int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2):]] for rucksack in inputs]
rucksacks = []
for rucksack in inputs:
    intersection = [i for i in rucksack[0] if i in rucksack[1]]
    rucksacks.append(intersection[0])
rucksacks = [ord(i) - 64 + 26 if ord(i) <= 65 + 26 else ord(i) - 96 for i in rucksacks]
priority_sum = sum(rucksacks)
print("Part 1:")
print(priority_sum)

print()

inputs = og_inputs.split()
groups = [[inputs[i + 0], inputs[i + 1], inputs[i + 2]] for i in range(0, len(inputs), 3)]
intersections = []
for group in groups:
    intersection = [i for i in group[0] if i in group[1] and i in group[2]]
    intersections.append(intersection[0])
intersections = [ord(i) - 64 + 26 if ord(i) <= 65 + 26 else ord(i) - 96 for i in intersections]
priority_sum = sum(intersections)
print("Part 2:")
print(priority_sum)
