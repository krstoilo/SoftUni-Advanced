rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum_matrix_elements = 0

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

# the best!!!!!!!!!!
print(sum(sum(rows) for rows in matrix))
print(matrix)