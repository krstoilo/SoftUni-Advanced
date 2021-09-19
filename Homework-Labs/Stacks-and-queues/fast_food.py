from collections import deque

food_qty = int(input())
order_sequence = [int(i) for i in input().split()]
order_of_serving = deque()

max_order = 0
for order in order_sequence:
    if order > max_order:
        max_order = order
    order_of_serving.appendleft(order)

for n in range(len(order_of_serving)):
    served = order_of_serving.pop()
    if served <= food_qty:
        food_qty -= served
    else:
        order_of_serving.append(served)
        break

print(max_order)
if order_of_serving:
    order_of_serving = [str(i) for i in order_of_serving]
    print(f'Orders left: {" ".join(order_of_serving[::-1])}')
else:
    print("Orders complete")