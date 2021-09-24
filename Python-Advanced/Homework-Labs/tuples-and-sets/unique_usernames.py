username_number = int(input())

uniques = set()
for _ in range(username_number):
    username = input()
    uniques.add(username)

for un in uniques:
    print(un)
