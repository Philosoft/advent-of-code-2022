from dataclasses import dataclass


@dataclass
class Sand:
    x: int
    y: int

    def get_possible_directions(self):
        return [(self.x, self.y + 1), (self.x - 1, self.y + 1), (self.x + 1, self.y + 1)]


with open('real-input.txt') as f:
    HOLE = (500, 0)
    points = []
    wall_points = set()
    for line in f:
        row = []
        for point in line.strip().split('->'):
            row.append(tuple(map(int, point.strip().split(','))))
        points.append(row)
        for i in range(len(row)):
            wall_points.add(row[i])
            print(f'working on {row[i]}')
            if i + 1 < len(row):
                y1 = row[i][1]
                y2 = row[i + 1][1]
                step_y = 1 if y1 <= y2 else -1
                y_stop = y2 + step_y
                for y in range(y1, y_stop, step_y):
                    x1 = row[i][0]
                    x2 = row[i + 1][0]
                    step_x = 1 if x1 <= x2 else -1
                    x_stop = x2 + step_x
                    for x in range(x1, x_stop, step_x):
                        wall_points.add((x, y))

    xlist = [p[0] for row in points for p in row]
    ylist = [p[1] for row in points for p in row]
    ylist.append(0)
    min_x, max_x = min(xlist), max(xlist)
    min_y, max_y = min(ylist), max(ylist)

    resting_sand = set()
    while True:
        sand = Sand(*HOLE)
        while True:
            previous_position = (sand.x, sand.y)
            for next_position in sand.get_possible_directions():
                if next_position not in wall_points and next_position not in resting_sand:
                    sand.x, sand.y = next_position
                    break

            if previous_position == (sand.x, sand.y):
                resting_sand.add((sand.x, sand.y))
                break

            if sand.x > max_x or sand.x < min_x or sand.y > max_y:
                break

        if sand.x > max_x or sand.x < min_x or sand.y > max_y:
            break

    cave = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            p = (x, y)
            c = '.'
            if p == HOLE:
                c = '+'
            elif p in wall_points:
                c = '#'
            elif p in resting_sand:
                c = '*'
            row.append(c)

        cave.append(row)

    for row in cave:
        for c in row:
            print(c, end='')
        print()

    print('Part 1: ', len(resting_sand))

    #################
    ### part 2
    ##################
    resting_sand = set()
    while True:
        sand = Sand(*HOLE)
        while True:
            previous_position = (sand.x, sand.y)
            if sand.y + 1 < max_y + 2:
                for next_position in sand.get_possible_directions():
                    if next_position not in wall_points and next_position not in resting_sand:
                        sand.x, sand.y = next_position
                        break

            if previous_position == (sand.x, sand.y):
                resting_sand.add((sand.x, sand.y))
                break

        if (sand.x, sand.y) == HOLE:
            break

    # paint cave
    cave = []
    x_options = []
    for p in resting_sand:
        x_options.append(p[0])

    for p in wall_points:
        x_options.append(p[0])

    min_x = min(x_options)
    max_x = max(x_options)
    for y in range(min_y, max_y + 1 + 2):
        row = []
        for x in range(min_x, max_x + 1):
            p = (x, y)
            c = '.'
            if p == HOLE:
                c = '+'
            elif p in wall_points:
                c = '#'
            elif p in resting_sand:
                c = '*'
            elif p[1] == max_y + 2:
                c = '#'
            row.append(c)

        cave.append(row)

    for row in cave:
        for c in row:
            print(c, end='')
        print()

    print('Part 1: ', len(resting_sand))
