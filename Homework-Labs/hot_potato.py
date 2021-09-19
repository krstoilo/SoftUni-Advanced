from collections import deque

names = input().split()
names_q = deque(names)
step = int(input())

while names_q:
    for _ in range(step - 1):
        names_q.append(names_q.popleft())
    removed_name = names_q.popleft()

    if names_q:
        print(f'Removed {removed_name}')
    else:
        print(f'Last is {removed_name}')

