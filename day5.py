file = open('day5.txt', 'r')
inputs = file.read()[:-1]
file.close()

lines = inputs.split("\n")
count_line_num = lines.index('') - 1
count_line = lines[count_line_num]
num_of_columns = int(count_line.split()[-1])
columns = [[] for _ in range(num_of_columns)]

for row in lines[:count_line_num]:
    for i in range(1, num_of_columns * 4 - 1, 4):
        if row[i] != ' ':
            columns[int((i - 1) / 4)].insert(0, row[i])

instruction_line_num = count_line_num + 2
instructions = lines[instruction_line_num:]
instruction_nums = []
for instruction in instructions:
    instruction = instruction.replace('move ', '')
    instruction = instruction.replace('from ', '')
    instruction = instruction.replace('to ', '')
    instruction = instruction.split(' ')
    instruction_nums.append([int(i) for i in instruction])

for instruction in instruction_nums:
    for _ in range(instruction[0]):
        crate = columns[instruction[1] - 1].pop()
        columns[instruction[2] - 1].append(crate)

last_items = [crates[-1] for crates in columns if len(columns) > 0]
print("Part 1:")
print(''.join(last_items))

print()

lines = inputs.split("\n")
count_line_num = lines.index('') - 1
count_line = lines[count_line_num]
num_of_columns = int(count_line.split()[-1])
columns = [[] for _ in range(num_of_columns)]

for row in lines[:count_line_num]:
    for i in range(1, num_of_columns * 4 - 1, 4):
        if row[i] != ' ':
            columns[int((i - 1) / 4)].insert(0, row[i])

instruction_line_num = count_line_num + 2
instructions = lines[instruction_line_num:]
instruction_nums = []
for instruction in instructions:
    instruction = instruction.replace('move ', '')
    instruction = instruction.replace('from ', '')
    instruction = instruction.replace('to ', '')
    instruction = instruction.split(' ')
    instruction_nums.append([int(i) for i in instruction])

for instruction in instruction_nums:
    crates_to_move = []
    for _ in range(instruction[0]):
        crate = columns[instruction[1] - 1].pop()
        crates_to_move.insert(0, crate)
    for crate in crates_to_move:
        columns[instruction[2] - 1].append(crate)

last_items = [crates[-1] for crates in columns if len(columns) > 0]
print("Part 2:")
print(''.join(last_items))
