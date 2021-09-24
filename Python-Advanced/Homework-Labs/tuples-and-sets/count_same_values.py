numbers = [float(x) for x in input().split()]

numbers_dictionary = {}

for number in numbers:
    if number not in numbers_dictionary:
        numbers_dictionary[number] = 1
    else:
        numbers_dictionary[number] += 1

for number, count in numbers_dictionary.items():
    print(f'{number} - {count} times')
