from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0


while True:
    if chocolates[-1] <= 0:
        chocolates.pop()
    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
    elif chocolates[-1] == cups_of_milk[0]:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        current_milk = cups_of_milk.popleft()
        cups_of_milk.append(current_milk)
        chocolates[-1] -= 5
    if not cups_of_milk or not chocolates:
        break
    if milkshakes == 5:
        break

if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

if not chocolates and cups_of_milk:
    print("Chocolate: empty")
    milk_string = ", ".join(str(x) for x in cups_of_milk)
    print(f"Milk: {milk_string}")
elif not cups_of_milk and chocolates:
    choc_string = ", ".join(str(x) for x in chocolates)
    print(f"Chocolate: {choc_string}")
    print(f"Milk: empty")
elif cups_of_milk and chocolates:
    choc_string = ", ".join(str(x) for x in chocolates)
    print(f"Chocolate: {choc_string}")
    milk_string = ", ".join(str(x) for x in cups_of_milk)
    print(f"Milk: {milk_string}")
elif not cups_of_milk and not chocolates:
    print("Chocolate: empty")
    print(f"Milk: empty")