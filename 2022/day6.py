file = open('day6.txt', 'r')
inputs = file.read()[:-1]
inputs = list(inputs)
file.close()

def check_if_start(chars):
    for char in chars:
        if chars.count(char) > 1:
            return False
    return True

def return_start_marker(inputs, length):
    chars = inputs[:length]
    index = length
    for char in inputs[length:]:
        if check_if_start(chars):
            return index
        
        chars.pop(0)
        chars.append(char)
        index += 1
    return -1

start_marker = return_start_marker(inputs, 4)
print("Part 1:")
print(start_marker)

print()

start_marker = return_start_marker(inputs, 14)
print("Part 2:")
print(start_marker)
