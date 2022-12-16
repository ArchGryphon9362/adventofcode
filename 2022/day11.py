file = open('day11.txt', 'r')
inputs = file.read()
file.close()

class Monkey:
    def __init__(self, items, operation, test_mod, test_true, test_false):
        self.items = items
        self.operation = operation
        self.test_mod = test_mod
        self.test_true = test_true
        self.test_false = test_false
        self.inspected = 0

    def inspect(self, mod, relief=1):
        result = [
            (self.test_true, []),
            (self.test_false, [])
        ]
        for item in self.items:
            self.inspected += 1
            if self.operation[0] == '*':
                item *= self.operation[1]
            elif self.operation[0] == '+':
                item += self.operation[1]
            elif self.operation[0] == '**':
                item **= self.operation[1]

            item //= relief
            item %= mod

            if item % self.test_mod == 0:
                result[0][1].append(item)
            else:
                result[1][1].append(item)
        self.items = []
        return result

    def receive(self, items):
        for item in items:
            self.items.append(item)

class KeepAway:
    def __init__(self):
        self.monkeys = []

    def round(self, mod, relief=1):
        for monkey in self.monkeys:
            result = monkey.inspect(mod, relief)
            self.monkeys[result[0][0]].receive(result[0][1])
            self.monkeys[result[1][0]].receive(result[1][1])

    def rounds(self, times, relief=1):
        mod = self.get_max_mod()
        for _ in range(times):
            self.round(mod, relief)

    def get_inspections(self):
        inspections = []
        for monkey in self.monkeys:
            inspections.append(monkey.inspected)
        return inspections

    def get_monkey_business(self):
        inspections = self.get_inspections()
        inspections.sort()
        result = inspections[-2] * inspections[-1]
        return result

    def get_max_mod(self):
        mod = 1
        for monkey in self.monkeys:
            mod *= monkey.test_mod
        return mod

    def load_start_states(self, start_states):
        for start_state in start_states:
            items = start_state["items"]
            operation = start_state["operation"]
            test_mod = start_state["mod"]
            test_true = start_state["true"]
            test_false = start_state["false"]
            monkey = Monkey(items, operation, test_mod, test_true, test_false)
            self.monkeys.append(monkey)

    def load_using_text(self, text):
        parsed = []
        text = text.split('\n\n')
        text = [lines.split('\n')[1:] for lines in text]
        for monkey in text:
            items = monkey[0].split()
            items = items[2:]
            items = [int(item.replace(',', '')) for item in items]

            operation = monkey[1].split()
            operation = operation[-2:]
            if operation[-1] == 'old':
                operation[0] = '**'
                operation[1] = 2
            else:
                operation[-1] = int(operation[-1])

            test_mod = monkey[2].split()
            test_mod = test_mod[-1]
            test_mod = int(test_mod)

            test_true = monkey[3].split()
            test_true = test_true[-1]
            test_true = int(test_true)

            test_false = monkey[4].split()
            test_false = test_false[-1]
            test_false = int(test_false)

            result_monkey = {
                "items": items,
                "operation": operation,
                "mod": test_mod,
                "true": test_true,
                "false": test_false
            }
            parsed.append(result_monkey)
        self.load_start_states(parsed)

game = KeepAway()
game.load_using_text(inputs)
game.rounds(20, 3)
business = game.get_monkey_business()
print("Part 1:")
print(business)

print()

game = KeepAway()
game.load_using_text(inputs)
game.rounds(10000)
business = game.get_monkey_business()
print("Part 2:")
print(business)
