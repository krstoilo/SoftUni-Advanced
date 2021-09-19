from collections import deque

qq = deque()

while True:
    command = input()
    if command == 'End':
        print(f'{len(qq)} people remaining.')
        break
    elif command == "Paid":
        while qq:
            print(qq.pop())
    else:
        qq.appendleft(command)