text = input()

ss = []

for ch in text:
    ss.append(ch)

for n in range(len(ss)):
    print(ss.pop(), end="")