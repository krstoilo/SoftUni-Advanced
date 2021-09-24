number_of_ops = int(input())

parking_lot = set()

for _ in range(number_of_ops):
    input_text = input().split(", ")
    direction = input_text[0]
    car_number = input_text[1]
    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        parking_lot.remove(car_number)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)