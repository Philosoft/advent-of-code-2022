with open('input.txt') as f:
    stacks_data = []
    for line in f:
        line = line.strip()
        if line == '':
            break

        stacks_data.append(line)

    row_numbers = stacks_data.pop()
    number_of_rows = len(list(filter(lambda x: x != '', row_numbers.split(' '))))
    stacks = [[] for x in range(number_of_rows)]
    # + 2 since there is no extra space for aligning at the beginning and end. + 1 for extra space
    column_width = (len(row_numbers) + 2) // number_of_rows + 1
    while stacks_data:
        line = stacks_data.pop()
        left, right = 0, column_width
        column = 0
        while left < len(line):
            letter = line[left:right].replace('[', '').replace(']', '').strip()
            if letter.strip() != '':
                stacks[column].append(letter)

            left, right = right, right + column_width
            column += 1

    stacks_p2 = []
    for stack in stacks:
        stacks_p2.append(stack.copy())
    for instruction in f:
        """
        move 6 from 1 to 7
        move 2 from 2 to 4
        """
        action, count, src_word, src, to, target = instruction.strip().split(' ')
        src, target, count = int(src) - 1, int(target) - 1, int(count)
        for i in range(count):
            stacks[target].append(stacks[src].pop())
        buf = []
        for _ in range(count):
            buf.append(stacks_p2[src].pop())

        for i in reversed(buf):
            stacks_p2[target].append(i)

    answer_p1 = ''.join([x[-1] for x in stacks])
    print(f'Part 1: {answer_p1}')
    answer_p2 = ''.join([x[-1] for x in stacks_p2])
    print(f'Part 2: {answer_p2}')
