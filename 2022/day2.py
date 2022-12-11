file = open('day2.txt', 'r')
og_inputs = file.read()[:-1]
file.close()

wins = 'AY BZ CX'
ties = 'AX BY CZ'
loses = 'AZ BX CY'
points = {"X": 1, "Y": 2, "Z": 3}

inputs = [move[0] + move[-1] for move in og_inputs.split('\n')]
inputs = [(6 if move in wins else 3 if move in ties else 0 if move in loses else 0) + points[move[-1]] for move in inputs]
print("Part 1:")
score = sum(inputs)
print(score)

print()

win_lose_chart = {
    "AZ": "AY",
    "AY": "AX",
    "AX": "AZ",
    "BZ": "BZ",
    "BY": "BY",
    "BX": "BX",
    "CZ": "CX",
    "CY": "CZ",
    "CX": "CY"
}
inputs = [move[0] + move[-1] for move in og_inputs.split('\n')]
inputs = [move.replace(move, win_lose_chart[move]) for move in inputs]
inputs = [(6 if move in wins else 3 if move in ties else 0 if move in loses else 0) + points[move[-1]] for move in inputs]
print("Part 2:")
score = sum(inputs)
print(score)
