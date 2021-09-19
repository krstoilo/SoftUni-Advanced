clothes_stack = [int(i) for i in input().split()]
capacity = int(input())
racks = 1

value = 0

while clothes_stack:
    current_item = clothes_stack.pop()
    value += current_item
    if value == capacity:
        if clothes_stack:
            racks += 1
            value = 0
    elif value > capacity:
        racks += 1
        value = current_item

print(racks)



