guests = int(input())

vips = set()
regulars = set()

for _ in range(guests):
    code = input()
    if code[0].isdigit():
        vips.add(code)
    else:
        regulars.add(code)

while True:
    command = input()
    if command == "END":
        break
    if command in vips:
        vips.remove(command)
    elif command in regulars:
        regulars.remove(command)

vips_sorted = sorted(vips)
regs_sorted = sorted(regulars)


print(len(vips_sorted) + len(regs_sorted))
if vips_sorted:
    for vip in vips_sorted:
        print(vip)
if regs_sorted:
    for reg in regs_sorted:
        print(reg)
