expression = input()

stack = []
balanced = True
pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
}

for ch in expression:
    if ch in '([{':
        stack.append(ch)
    else:
        if stack:
            last_ch = stack.pop()
            if pairs[last_ch] != ch:
                balanced = False
                break
        else:
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")