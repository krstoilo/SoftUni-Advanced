n = int(input())

elements = set()

for _ in range(n):
    text = input().split()
    for element in text:
        elements.add(element)

for elem in elements:
    print(elem)