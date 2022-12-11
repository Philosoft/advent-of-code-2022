with open('real-input.txt') as f:
    epoch = 0
    durations = {'addx': 2, 'noop': 1}
    cycles_left = 0
    x = 1
    sprite_position = [0, 1, 2]

    targets = {
        20: -1,
        60: -1,
        100: -1,
        140: -1,
        180: -1,
        220: -1.
    }
    screen = []
    row = []
    SCREEN_WIDTH = 40
    for line in f:
        parts = line.strip().split(' ')
        if parts[0] == 'addx':
            cycles_left = 2


            def callback(reg: int) -> int:
                return reg + int(parts[1])
        elif parts[0] == 'noop':
            cycles_left = 1


            def callback(reg: int) -> int:
                return reg
        else:
            raise Exception(f'Unknown operation "{parts[0]}"')

        while cycles_left > 0:
            row.append('#' if epoch % SCREEN_WIDTH in sprite_position else ' ')
            cycles_left -= 1
            epoch += 1
            if epoch % 40 == 0:
                screen.append(row)
                row = []
            if epoch in targets:
                targets[epoch] = epoch * x

        x = callback(x)
        sprite_position = [x - 1, x, x + 1]

print(sum(targets.values()))
for row in screen:
    print(''.join(row))

# answer for part 2 E F G E R U R E