import heapq

top = [0, 0, 0]
heapq.heapify(top)
current_max = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line == '':
            heapq.heappushpop(top, current_max)
            current_max = 0
        else:
            current_max += int(line)

heapq.heappushpop(top, current_max)

print(sum(top))
