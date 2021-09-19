import sys


def max_num(ss):
    max_n = -sys.maxsize
    for el in ss:
        if int(el) > max_n:
            max_n = int(el)
    return max_n


def min_num(ss):
    min_n = sys.maxsize
    for el in ss:
        if int(el) < min_n:
            min_n = int(el)
    return min_n

ss = []

n = int(input())
for i in range(n):
    query = input()
    if '1' in query:
        token = query.split()
        number = int(token[1])
        ss.append(number)
    elif '2' in query:
        if ss:
            ss.pop()
    elif '3' in query:
        if ss:
            print(max_num(ss))
    elif '4' in query:
        if ss:
            print(min_num(ss))

for n in range(len(ss)-1):
    last = ss.pop()
    print(f'{last},', end=" ")
print(ss.pop())
