file = open('day8.txt', 'r')
inputs = file.read()[:-1]
file.close()

inputs = inputs.split()

def grid_to_columns(grid):
    num_columns = len(grid[0])
    num_rows = len(grid)
    columns = [[[] for _ in range(num_rows)] for _ in range(num_columns)]
    for y in range(num_rows):
        for x in range(num_columns):
            columns[x][y] = int(grid[y][x])

    return columns

def to_rows_columns(grid):
    num_columns = len(grid[0])
    rows = [list(row) for row in grid]
    rows = [[int(item) for item in row] for row in rows]
    columns = grid_to_columns(grid)

    return (rows, columns)

def is_visible(rows, columns, x, y):
    row = rows[y]
    column = columns[x]

    value = row[x]
    assert(value == column[y])

    row_left = row[:x] or [-1]
    row_right = row[x+1:] or [-1]
    column_up = column[:y] or [-1]
    column_down = column[y+1:] or [-1]

    row_left = max(row_left) < value
    row_right = max(row_right) < value
    column_up = max(column_up) < value
    column_down = max(column_down) < value

    row = row_left or row_right
    column = column_up or column_down

    return row or column

def count_visible(list, value):
    count = 0
    for x in range(len(list)):
        count += 1
        if list[x] >= value: break
    return count

def calc_score(rows, columns, x, y):
    row = rows[y]
    column = columns[x]

    value = row[x]
    assert(value == column[y])

    row_left = row[:x] or [-1]
    row_left.reverse()
    row_right = row[x+1:] or [-1]
    column_up = column[:y] or [-1]
    column_up.reverse()
    column_down = column[y+1:] or [-1]
    
    row_left = count_visible(row_left, value)
    row_right = count_visible(row_right, value)
    column_up = count_visible(column_up, value)
    column_down = count_visible(column_down, value)

    row = row_left * row_right
    column = column_up * column_down

    return row * column

def get_visible_count(rows, columns):
    num_columns = len(columns)
    num_rows = len(rows)
    grid_visible = []
    for y in range(num_rows):
        for x in range(num_columns):
            grid_visible.append(is_visible(rows, columns, x, y))

    return grid_visible.count(True)

def get_scores(rows, columns):
    num_columns = len(columns)
    num_rows = len(rows)
    scores = []
    for y in range(num_rows):
        for x in range(num_columns):
            scores.append(calc_score(rows, columns, x, y))

    return scores

rows, columns = to_rows_columns(inputs)
visible_count = get_visible_count(rows, columns)
print("Part 1:")
print(visible_count)

print()

scores = get_scores(rows, columns)
print("Part 2:")
print(max(scores))
