text = input()

occurrences = {}

for letter in text:
    if letter in occurrences:
        occurrences[letter] += 1
    else:
        occurrences[letter] = 1

s_occurences = sorted(occurrences.items())

for symbol, count in s_occurences:
    print(f'{symbol}: {count} time/s')
