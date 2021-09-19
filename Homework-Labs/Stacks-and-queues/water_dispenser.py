from collections import deque

w_qty = int(input())
qq = deque()

command = input()
while command != 'Start':
    qq.appendleft(command)
    command = input()

while True:
    command = input()
    if command.isdigit():
        if int(command) <= w_qty:
            w_qty -= int(command)
            name = qq.pop()
            print(f'{name} got water')
        else:
            name = qq.pop()
            print(f'{name} must wait')
    elif 'refill' in command:
        token = command.split()
        litres = int(token[1])
        w_qty += litres
    elif command == 'End':
        break

print(f"{w_qty} liters left")