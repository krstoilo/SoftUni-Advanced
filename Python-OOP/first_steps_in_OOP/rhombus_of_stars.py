n = int(input())


def print_line(spaces_count, stars_count):
    line_sp = "".join([" "] * spaces_count)
    line_st = " ".join(["*"] * stars_count)
    print(line_sp + line_st)


for i in range(n):
    spaces = n - i - 1
    stars = i + 1
    print_line(spaces, stars)

for i in range(n - 2, -1, -1):
    spaces = n - i - 1
    stars = i + 1
    print_line(spaces, stars)

