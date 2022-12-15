file = open('day10.txt', 'r')
inputs = file.read()
file.close()

class PC:
    def __init__(self):
        self.cycles = -1
        self.x = 1
        self.program = []
    
    def exec_single(self):
        command = self.program.pop(0)
        if (command[0] == 'noop'):
            return
        if (command[-1] < 1):
            command[-1] += 1
            self.program.insert(0, command)
            return
        command[-1] = 0
        self.x += command[1]
        return

    def execute(self, positions):
        self.cycles = -1
        self.x = 1
        original_program = self.program[:]
        result = []
        while self.cycles < max(positions):
            self.cycles += 1
            if self.cycles in positions:
                result.append(self.x)
            if self.cycles > 0:
                self.exec_single()
        self.program = original_program
        return result

    def render_crt(self):
        cycles = self.execute(range(40 * 6 + 1))[1:]
        print(len(cycles))
        result = ''
        for position, cycle in enumerate(cycles):
            if position % 40 == 0:
                result += '\n'
            draw = position % 40
            ### test ###
            # test = ''
            # for i in range(40):
            #     if abs(cycle - i) <= 1:
            #         test += '#'
            #     else:
            #         test += '.'
            # print(cycle)
            # print(test)
            ### end test ###
            draw = abs(cycle - draw)
            draw = draw <= 1
            if draw:
                result += '\u001b[40;1m#'
            else:
                result += '\u001b[47;1m.'
            result += '\u001b[0m'
        return result[1:]

    def load_program(self, commands):
        commands = commands.split('\n')
        commands = [command.split(' ') for command in commands]
        for index in range(len(commands)):
            if len(commands[index]) > 1:
                commands[index][1] = int(commands[index][1])
            commands[index].append(0)
        self.program = commands

pc = PC()
pc.load_program(inputs)
strengths = pc.execute([20, 60, 100, 140, 180, 220])
strengths[0] *= 20
strengths[1] *= 60
strengths[2] *= 100
strengths[3] *= 140
strengths[4] *= 180
strengths[5] *= 220
total_strength = sum(strengths)
print("Part 1:")
print(total_strength)

print()

rendered_crt = pc.render_crt()
print("Part 2:")
print(rendered_crt)
