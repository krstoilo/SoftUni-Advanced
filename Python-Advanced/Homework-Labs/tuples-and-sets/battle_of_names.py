n = int(input())

even_set = set()
odd_set = set()

for row in range(1, n + 1):
    name = input()
    temp_sum = 0
    for sym in name:
        temp_sum += ord(sym)
    temp_sum = temp_sum // row
    if temp_sum % 2 == 0:
        even_set.add(temp_sum)
    else:
        odd_set.add(temp_sum)


if sum(even_set) == sum(odd_set):
    new_set = odd_set ^ even_set
    print(", ".join(str(x) for x in new_set))
elif sum(odd_set) > sum(even_set):
    new_set = odd_set - even_set
    print(", ".join(str(x) for x in new_set))
else:
    new_set = odd_set ^ even_set
    print(", ".join(str(x) for x in new_set))

