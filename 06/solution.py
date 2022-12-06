offset_for_packet, offset_for_message = -1, -1
offset = 0

with open('input.txt') as f:
    seen_chars_so_far = set()
    buf = []

    while True:
        char = f.read(1)
        if not char:
            break

        offset += 1
        if char not in seen_chars_so_far:
            if len(buf) < 14:
                buf.append(char)
                seen_chars_so_far.add(char)

            if len(buf) == 4 and offset_for_packet == -1:
                offset_for_packet = offset

            if len(buf) == 14 and offset_for_message == -1:
                offset_for_message = offset

            if offset_for_packet != -1 and offset_for_message != -1:
                break
        else:
            pos = 0
            for i in range(len(buf)):
                pos = i
                if buf[i] != char:
                    seen_chars_so_far.remove(buf[i])
                else:
                    break
            buf = buf[pos + 1:]
            buf.append(char)

print(f'Part 1: {offset_for_packet}')
print(f'Part 2: {offset_for_message}')
