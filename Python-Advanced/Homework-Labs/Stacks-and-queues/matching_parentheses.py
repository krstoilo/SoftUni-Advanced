expression = input()

opening = []

for index, ch in enumerate(expression):
    if ch == '(':
        opening.append(index)
    elif ch == ')':
        closing_i = index
        opening_i = opening.pop()
        print(expression[opening_i:closing_i+1])
