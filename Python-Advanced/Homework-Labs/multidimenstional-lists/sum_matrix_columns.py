rows, cols = [int(x) for x in input().split(", ")]


matrix = []

for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)


result = []

for column_index in range(cols):
    column_sum = 0
    for row_index in range(rows):
        column_sum += matrix[row_index][column_index]
    result.append(column_sum)

[print(x) for x in result]