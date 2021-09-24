n = int(input())

max_len = 0
longest_intersection = set()

for _ in range(n):
    ranges = input().split("-")
    first_range = [int(x) for x in ranges[0].split(",")]
    second_range = [int(x) for x in ranges[1].split(",")]
    first_set = set()
    second_set = set()
    for n in range(first_range[0], first_range[1]+1):
        first_set.add(n)
    for n in range(second_range[0], second_range[1]+1):
        second_set.add(n)
    current_intersection = first_set & second_set
    if len(current_intersection) > max_len:
        max_len = len(current_intersection)
        longest_intersection = current_intersection

string_nums = [str(x) for x in longest_intersection]
string = ", ".join(string_nums)

print(f"Longest intersection is [{string}] with length {max_len}")