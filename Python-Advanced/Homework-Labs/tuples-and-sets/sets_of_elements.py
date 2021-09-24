n, m = [int(x) for x in input().split()]

set_n = set()
set_m = set()

for _ in range(n):
    number = int(input())
    set_n.add(number)
for _ in range(m):
    number = int(input())
    set_m.add(number)

unique_elements = set_n & set_m

for num in unique_elements:
    print(num)

