text = input().split()

ss = []

for ch in text:
    ss.append(ch)

for _ in range(len(ss)):
    last = ss.pop()
    print(last, end=" ")