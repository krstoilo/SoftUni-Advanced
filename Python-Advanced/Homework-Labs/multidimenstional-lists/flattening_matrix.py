rows = int(input())

matrix = []

for n in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

flattened_m = [num for row in matrix for num in row]
print(flattened_m)

