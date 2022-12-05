def get_char_priority(char: str) -> int:
    return ord(char) - 96 if char.islower() else ord(char) - 38


sum_of_duplicates, sum_of_badges = 0, 0

with open('input.txt') as f:
    group_things = []
    for line in f:
        line = line.strip()
        group_things.append(set(line))
        middle = len(line) // 2
        left, right = line[:middle], line[middle:]
        sum_of_duplicates += sum(
            map(
                get_char_priority,
                set(left).intersection(set(right))
            )
        )

        if len(group_things) == 3:
            sum_of_badges += sum(
                map(
                    get_char_priority,
                    group_things[0].intersection(group_things[1], group_things[2])
                )
            )
            group_things = []

print(f'Part 1: {sum_of_duplicates}')
print(f'Part 2: {sum_of_badges}')
