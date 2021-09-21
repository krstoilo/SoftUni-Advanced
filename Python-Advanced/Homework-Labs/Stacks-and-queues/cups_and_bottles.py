from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0

while True:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    if current_bottle < current_cup:
        current_cup -= current_bottle
        cups.appendleft(current_cup)
    elif current_bottle == current_cup:
        pass
    else:
        wasted_water += current_bottle - current_cup
    if not cups:
        print("Bottles: ", end="")
        for n in range(len(bottles)-1):
            print(bottles.pop(), end=" ")
        print(bottles[0])
        break
    if not bottles:
        print("Cups: ", end="")
        for n in range(len(cups)-1):
            print(cups.popleft(), end=" ")
        print(cups[0])
        break

print(f"Wasted litters of water: {wasted_water}")