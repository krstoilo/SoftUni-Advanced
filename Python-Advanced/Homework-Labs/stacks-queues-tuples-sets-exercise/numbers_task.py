first_sequence = {int(x) for x in input().split()}
second_sequence = {int(x) for x in input().split()}

n = int(input())

for _ in range(n):
    command = input()
    if "Check Subset" == command:
        if first_sequence < second_sequence or second_sequence < first_sequence:
            print(True)
        else:
            print(False)
    else:
        token = command.split()
        if "Add First" in command:
            for elem in token:
                if elem[0].isdigit():
                    first_sequence.add(int(elem))
        elif "Add Second" in command:
            for elem in token:
                if elem[0].isdigit():
                    second_sequence.add(int(elem))
        elif "Remove First" in command:
            for elem in token:
                if elem[0].isdigit():
                    if int(elem) in first_sequence:
                        first_sequence.remove(int(elem))
        elif "Remove Second" in command:
            for elem in token:
                if elem[0].isdigit():
                    if int(elem) in second_sequence:
                        second_sequence.remove(int(elem))


print(", ".join(str(x) for x in sorted(first_sequence)))
print(", ".join(str(x) for x in sorted(second_sequence)))