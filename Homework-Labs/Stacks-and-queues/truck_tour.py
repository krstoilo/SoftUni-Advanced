from collections import deque

pump_count = int(input())
queue = deque()

for _ in range(pump_count):
    pump = [int(x) for x in input().split()]
    queue.append(pump)

for idx in range(pump_count):
    circle_completed = True
    tank = 0
    for pump in queue:
        fuel = pump[0]
        distance = pump[1]
        tank += fuel
        if distance > tank:
            circle_completed = False
            break
        tank -= distance
    if circle_completed:
        print(idx)
        break
    else:
        queue.append(queue.popleft())
