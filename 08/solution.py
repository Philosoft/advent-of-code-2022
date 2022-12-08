field = []

with open('input.txt') as f:
    for line in f:
        field.append([h for h in map(int, line.strip())])

count = 0
max_scenic_score = 0
for r in range(len(field)):
    if r == 0 or r == len(field) - 1:
        count += len(field[r])
        continue

    for c in range(len(field[r])):
        if c == 0 or c == len(field[r]) - 1:
            count += 1
            continue

        top_score, bottom_score, left_score, right_score = 0, 0, 0, 0

        # top
        current = field[r][c]
        overflow = 0
        for i in range(r - 1, -1, -1):
            if field[i][c] < current:
                top_score += 1
            else:
                overflow = 1
                break
        is_top_visible = top_score == r
        top_score += overflow

        # left
        overflow = 0
        for i in range(c - 1, -1, -1):
            if field[r][i] < current:
                left_score += 1
            else:
                overflow = 1
                break
        is_left_visible = left_score == c
        left_score += overflow

        # bottom
        overflow = 0
        for i in range(r + 1, len(field)):
            if field[i][c] < current:
                bottom_score += 1
            else:
                overflow = 1
                break
        is_bottom_visible = bottom_score == (len(field) - r - 1)
        bottom_score += overflow

        # right
        overflow = 0
        for i in range(c + 1, len(field[r])):
            if field[r][i] < current:
                right_score += 1
            else:
                overflow = 1
                break
        is_right_visible = right_score == (len(field[r]) - c - 1)
        right_score += overflow

        if is_top_visible or is_left_visible or is_right_visible or is_bottom_visible:
            count += 1

        max_scenic_score = max(max_scenic_score, top_score * bottom_score * left_score * right_score)

print(f'Part 1: {count}', '✅' if count == 1698 else '❌')
print(f'Part 2: {max_scenic_score}', '✅' if max_scenic_score == 672280 else '❌')
