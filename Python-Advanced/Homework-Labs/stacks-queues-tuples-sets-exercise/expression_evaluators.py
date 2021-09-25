from math import floor
from collections import deque

expression = input().split()
numbers = deque()


for element in expression:
    if element.isdigit() or len(element) > 1:
        numbers.append(int(element))
    else:
        if element == "*":
            result = numbers.popleft()
            while numbers:
                result *= numbers.popleft()
            numbers.append(result)
        elif element == "+":
            result = numbers.popleft()
            while numbers:
                result += numbers.popleft()
            numbers.append(result)
        elif element == "/":
            result = numbers.popleft()
            while numbers:
                result /= numbers.popleft()
            numbers.append(floor(result))
        elif element == "-":
            result = numbers.popleft()
            while numbers:
                result -= numbers.popleft()
            numbers.append(floor(result))

for n in numbers:
    print(n)