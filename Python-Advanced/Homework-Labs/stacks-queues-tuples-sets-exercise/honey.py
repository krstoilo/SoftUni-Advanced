from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operations = deque(input().split())

total_honey = 0

while True:
    if bees[0] <= nectar[-1]:
        if operations[0] == "+":
            honey = abs(bees[0] + nectar[-1])
            total_honey += honey
        elif operations[0] == "-":
            honey = abs(bees[0] - nectar[-1])
            total_honey += honey
        if operations[0] == "*":
            honey = abs(bees[0] * nectar[-1])
            total_honey += honey
        if operations[0] == "/":
            if nectar[-1] == 0:
                total_honey += 0
            else:
                honey = abs(bees[0] / nectar[-1])
                total_honey += honey
        bees.popleft()
        nectar.pop()
        operations.popleft()
    else:
        nectar.pop()
    if not nectar or not bees:
        break

print(f"Total honey made: {total_honey}")
if bees:
    bees_string = ", ".join(str(x) for x in bees)
    print(f"Bees left: {bees_string}")
if nectar:
    nectar_string = ", ".join(str(x) for x in nectar)
    print(f"Nectar left: {nectar_string}")