import collections
from typing import Tuple

field = []
start_coordinates = ()
end_coordinates = ()
START_MARKER = 'S'
END_MARKER = 'E'

with open('real-input.txt') as f:
    row_number = 0
    for line in f:
        row = []
        column = 0
        for c in line.strip():
            if c == START_MARKER:
                c = 'a'
                start_coordinates = (column, row_number)
            elif c == END_MARKER:
                c = 'z'
                end_coordinates = (column, row_number)

            row.append(ord(c) - ord('a'))
            column += 1
        field.append(row)
        row_number += 1

possible_paths = []
pp = []


def bfs(start: Tuple[int, int], end: Tuple[int, int]) -> int:
    step_field = []
    for row in field:
        step_field.append([-1 for x in row])

    q = collections.deque([start])
    steps = 0
    start_x, start_y = start
    step_field[start_y][start_x] = steps
    points_in_queue = set()
    points_in_queue.add(start)
    while q:
        for _ in range(len(q)):
            point = q.popleft()
            points_in_queue.remove(point)
            x, y = point
            if step_field[y][x] == -1 or steps < step_field[y][x]:
                step_field[y][x] = steps

            current_cell = field[y][x]
            if x + 1 < len(step_field[y]) and (x + 1, y) not in points_in_queue:
                right_step_cell = step_field[y][x + 1]
                if current_cell + 1 >= field[y][x + 1] and (right_step_cell == -1 or right_step_cell > steps):
                    q.append((x + 1, y))
                    points_in_queue.add((x + 1, y))

            if x - 1 >= 0 and (x - 1, y) not in points_in_queue:
                left_step_cell = step_field[y][x - 1]
                if current_cell + 1 >= field[y][x - 1] and (left_step_cell == -1 or left_step_cell > steps):
                    q.append((x - 1, y))
                    points_in_queue.add((x - 1, y))

            if y + 1 < len(step_field) and (x, y + 1) not in points_in_queue:
                down_step_cell = step_field[y + 1][x]
                if current_cell + 1 >= field[y + 1][x] and (down_step_cell == -1 or down_step_cell > steps):
                    q.append((x, y + 1))
                    points_in_queue.add((x, y + 1))

            if y - 1 >= 0 and (x, y - 1) not in points_in_queue:
                up_step_cell = step_field[y - 1][x]
                if current_cell + 1 >= field[y - 1][x] and (up_step_cell == -1 or up_step_cell > steps):
                    q.append((x, y - 1))
                    points_in_queue.add((x, y - 1))
        steps += 1

    end_x, end_y = end
    return step_field[end_y][end_x]


print('Part 1: ', bfs(start_coordinates, end_coordinates))

possible_p2_answers = []
for y in range(len(field)):
    for x in range(len(field[y])):
        if field[y][x] == 0:
            result = bfs((x, y), end_coordinates)
            if result > -1:
                possible_p2_answers.append(result)

print('Part 2: ', min(possible_p2_answers))
