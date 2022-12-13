file = open('day9.txt')
inputs = file.read()[:-1]
file.close()

# x = right
# y = up
# like in standard maths
class Map:
    def __init__(self, tails=1):
        self.knots = [(0, 0)] * (tails + 1)
        self.tails = tails
        self.visited = [(0, 0)]

    def move_tails(self):
        for knot in range(self.tails):
            head = self.knots[knot]
            tail = self.knots[knot + 1]
            distance_x = head[0] - tail[0]
            distance_y = head[1] - tail[1]
            dx_abs = abs(distance_x)
            dy_abs = abs(distance_y)
            direction_x = distance_x / dx_abs if dx_abs > 0 else 0
            direction_y = distance_y / dy_abs if dy_abs > 0 else 0

            if dx_abs <= 1 and dy_abs <= 1:
                continue

            new_x = tail[0]
            new_y = tail[1]

            if (dx_abs > 0 and dy_abs > 1) or (dx_abs > 1 and dy_abs > 0):
                new_x += 1 * direction_x
                new_y += 1 * direction_y
                tail = (new_x, new_y)
                self.knots[knot + 1] = tail
                if knot == self.tails - 1 and tail not in self.visited:
                    self.visited.append(tail)
                continue

            if dx_abs > 1:
                new_x += 1 * direction_x
            elif dy_abs > 1:
                new_y += 1 * direction_y

            tail = (new_x, new_y)
            self.knots[knot + 1] = tail
            if knot == self.tails - 1 and tail not in self.visited:
                self.visited.append(tail)

    def move_head_x(self, x):
        direction = x / abs(x)
        speed = abs(x)

        for _ in range(speed):
            new_x = self.knots[0][0]
            new_y = self.knots[0][1]

            new_x += 1 * direction
            self.knots[0] = (new_x, new_y)
            self.move_tails()

    def move_head_y(self, y):
        direction = y / abs(y)
        speed = abs(y)

        for _ in range(speed):
            new_x = self.knots[0][0]
            new_y = self.knots[0][1]

            new_y += 1 * direction
            self.knots[0] = (new_x, new_y)
            self.move_tails()

def parsed_commands(commands):
    commands = commands.split('\n')
    commands = [command.split() for command in commands]
    commands = [(command[0], int(command[1])) for command in commands]
    return commands

def run_commands(map, commands):
    for command in commands:
        if command[0] == 'L':
            map.move_head_x(-command[1])
        elif command[0] == 'R':
            map.move_head_x(command[1])
        elif command[0] == 'D':
            map.move_head_y(-command[1])
        elif command[0] == 'U':
            map.move_head_y(command[1])

map = Map()
commands = parsed_commands(inputs)
run_commands(map, commands)
places_visited = len(map.visited)
print("Part 1:")
print(places_visited)

print()

map = Map(9)
commands = parsed_commands(inputs)
run_commands(map, commands)
places_visited = len(map.visited)
print("Part 2:")
print(places_visited)
