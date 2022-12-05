count_collapsed = 0
count_overlapping = 0
with open('input.txt') as f:
    for line in f:
        first, second = line.strip().split(',')
        l1, r1 = map(int, first.split('-'))
        l2, r2 = map(int, second.split('-'))

        if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r2 >= r1):
            count_collapsed += 1

        li, ri = max(l1, l2), min(r1, r2)
        if li <= ri:
            count_overlapping += 1

print(f'Part 1: {count_collapsed}')
print(f'Part 2: {count_overlapping}')