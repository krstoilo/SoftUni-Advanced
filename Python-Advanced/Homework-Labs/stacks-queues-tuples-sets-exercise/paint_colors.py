from collections import deque
from math import ceil

text_line = deque(input().split())
available_colors = ["blue", "red", "yellow", "orange", "purple", "green"]

colors_found = []

while text_line:
    if len(text_line) == 1:
        if text_line[0] in available_colors:
            colors_found.append(text_line[0])
            text_line.pop()
        else:
            subs = text_line.pop()
            text_line.append(subs[:-1])
            text_line = deque([x for x in text_line if x != ''])
    else:
        current_color = text_line[0] + text_line[-1]
        current_color_2 = text_line[-1] + text_line[0]
        if current_color in available_colors:
            colors_found.append(current_color)
            text_line.pop()
            text_line.popleft()
        elif current_color_2 in available_colors:
            colors_found.append(current_color_2)
            text_line.pop()
            text_line.popleft()
        else:
            first_sub = text_line.popleft()
            second_sub = text_line.pop()
            index = ceil(len(text_line) / 2)
            text_line.insert(index, first_sub[:-1])
            text_line.insert(index+1, second_sub[:-1])
            text_line = deque([x for x in text_line if x != ''])

if "purple" in colors_found:
    if "blue" not in colors_found or "red" not in colors_found:
        colors_found.remove("purple")
if "orange" in colors_found:
    if "red" not in colors_found or "yellow" not in colors_found:
        colors_found.remove("orange")
if "green" in colors_found:
    if "blue" not in colors_found or "yellow" not in colors_found:
        colors_found.remove("green")

print(colors_found)