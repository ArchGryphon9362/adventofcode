file = open('day7.txt', 'r')
inputs = file.read()[:-1]
file.close()

# Helper Functions
def add_if_command(commands, command_indexes, line, index):
    if line.startswith("$"):
        commands.append(line[2:].split())
        command_indexes.append(index)

def is_command(console_log, command_indexes, index):
    if index + 1 == len(console_log):
        return False
    return index in command_indexes

def is_file(line):
    return not line.startswith("dir")

def get_dir_size(listing):
    total_size = 0

    for line in listing:
        if is_file(line):
            file_size = line.split()[0]
            file_size = int(file_size)
            total_size += file_size

    return total_size

def parse_command(command, result, dir):
    dir_size = 0

    if command[0] == "cd":
        if command[1] == "/":
            dir = ""
            return [False, dir]
        if command[1] == "..":
            dir = dir.split('/')
            dir = dir[:-1]
            dir = '/'.join(dir)
            return [False, dir]
        dir += "/" + command[1]
    elif command[0] == "ls":
        dir_size = get_dir_size(result)

    return [dir_size, dir]

# Main Functions
def convert_to_command_result(console_log):
    console_log = inputs.split('\n')
    commands = []
    command_indexes = []
    for index, line in enumerate(console_log):
        add_if_command(commands, command_indexes, line, index)

    result_lengths = []
    current_length = 0
    for index, line in enumerate(console_log[1:]):
        if is_command(console_log[1:], command_indexes[1:], index + 1):
            result_lengths.append(current_length)
            current_length = 0
        else:
            current_length += 1
    result_lengths.append(current_length)
    
    commands_results = []
    for index, command in enumerate(commands):
        result_index = command_indexes[index] + 1
        result_length = result_lengths[index]

        result = console_log[result_index:result_index + result_length]
        command_result = (command, result)
        commands_results.append(command_result)

    return commands_results

def get_dir_sizes(command_results):
    dirs = {}

    current_dir = ""
    for command, result in command_results:
        dir_size, new_dir = parse_command(command, result, current_dir)
        if dir_size != False:
            dirs[current_dir] = dir_size
        dir_split = current_dir.split('/')
        for dir_idx in range(1, len(dir_split)):
            extra_dir = dir_split[:dir_idx]
            extra_dir = '/'.join(extra_dir)
            final = 0
            if extra_dir in dirs:
                final = dirs[extra_dir]
            if dir_size != False:
                final += dir_size
            dirs[extra_dir] = final
        current_dir = new_dir

    return dirs

def sum_dirs(dirs, max):
    total_size = 0

    for dir_size in dirs.values():
        if dir_size <= max or max == -1:
            total_size += dir_size

    return total_size

def closest_lower_number(list, x):
    sorted_list = sorted(list)
    for item in sorted_list:
        if item >= x:
            return item

# Main Code
command_results = convert_to_command_result(inputs)
dirs = get_dir_sizes(command_results)
total_size_100k_max = sum_dirs(dirs, 100_000)

print("Part 1:")
print(total_size_100k_max)

print()

total_space = 70_000_000
free_space = total_space - dirs['']
needed_space = 30_000_000
to_free = needed_space - free_space
delete_dir_size = closest_lower_number(dirs.values(), to_free)
print("Part 2:")
print(delete_dir_size)
