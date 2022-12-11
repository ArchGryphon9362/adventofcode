file = open('day4.txt', 'r')
og_inputs = file.read()
file.close()

pairs = []
for pair in og_inputs.split():
    pair1, pair2 = pair.split(',')
    pair1 = pair1.split('-')
    pair2 = pair2.split('-')
    pair1 = [i for i in range(int(pair1[0]), int(pair1[1]) + 1)]
    pair2 = [i for i in range(int(pair2[0]), int(pair2[1]) + 1)]
    pair1_in_2 = set(pair2).issubset(set(pair1))
    pair2_in_1 = set(pair1).issubset(set(pair2))
    pairs.append(pair1_in_2 or pair2_in_1)
overlapping = len([pair for pair in pairs if pair])
print("Part 1:")
print(overlapping)

print()

pairs = []
for pair in og_inputs.split():
    pair1, pair2 = pair.split(',')
    pair1 = pair1.split('-')
    pair2 = pair2.split('-')
    pair1 = [i for i in range(int(pair1[0]), int(pair1[1]) + 1)]
    pair2 = [i for i in range(int(pair2[0]), int(pair2[1]) + 1)]
    overlap = [i for i in pair1 if i in pair2]
    pairs.append(overlap)
overlapping = len([pair for pair in pairs if pair])
print("Part 2:")
print(overlapping)
