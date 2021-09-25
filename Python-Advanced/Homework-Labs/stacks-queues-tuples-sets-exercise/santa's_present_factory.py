from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

doll_magic_needed = 150
train_magic_needed = 200
bear_magic_needed = 300
bicycle_magic_needed = 400

successfully_crafted = False

toys = {}

while True:
    if not materials or not magic_level:
        break
    if materials[-1] == 0:
        materials.pop()
    elif magic_level[0] == 0:
        magic_level.popleft()
    elif materials[-1] * magic_level[0] < 0:
        result = materials[-1] + magic_level[0]
        materials.pop()
        magic_level.popleft()
        materials.append(result)
    elif materials[-1] * magic_level[0] > 0:
        if materials[-1] * magic_level[0] == doll_magic_needed:
            if "Doll" not in toys:
                toys["Doll"] = 1
            else:
                toys["Doll"] += 1
            materials.pop()
            magic_level.popleft()
        elif materials[-1] * magic_level[0] == train_magic_needed:
            if "Wooden train" not in toys:
                toys["Wooden train"] = 1
            else:
                toys["Wooden train"] += 1
            materials.pop()
            magic_level.popleft()
        elif materials[-1] * magic_level[0] == bear_magic_needed:
            if "Teddy bear" not in toys:
                toys["Teddy bear"] = 1
            else:
                toys["Teddy bear"] += 1
            materials.pop()
            magic_level.popleft()
        elif materials[-1] * magic_level[0] == bicycle_magic_needed:
            if "Bicycle" not in toys:
                toys["Bicycle"] = 1
            else:
                toys["Bicycle"] += 1
            materials.pop()
            magic_level.popleft()
        else:
            magic_level.popleft()
            materials[-1] += 15
    if "Doll" in toys and "Wooden train" in toys or \
            "Teddy bear" in toys and "Bicycle" in toys:
        successfully_crafted = True


if successfully_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left: ", end= "")
    for n in range(len(materials)-1, 0, -1):
        print(f'{materials[n]}, ', end="")
    print(materials[0])
if magic_level:
    print("Magic left: ", end="")
    for n in range(len(magic_level) - 1, 0, -1):
        print(f'{magic_level[n]}, ', end="")
    print(magic_level[0])


for key, value in sorted(toys.items()):
    print(f'{key}: {value}')