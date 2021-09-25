rows = int(input())

matrix = []

for n in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

evens = [[x for x in row if x % 2 == 0] for row in matrix]
print(evens)