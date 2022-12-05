maximum = 0
current_maximum = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line != '':
            current_maximum += int(line)
        else:
            maximum = max(maximum, current_maximum)
            current_maximum = 0


print(max(maximum, current_maximum))