import collections
import functools
from typing import List


def parse(line: str) -> List[int]:
    out = [[]]
    level = 0
    buf = ''
    for c in line:
        if c == '[':
            target = out[0]
            for i in range(level):
                target = target[-1]
            target.append([])
            level += 1
        elif c == ']':
            if buf:
                target = out[0]
                for i in range(level):
                    target = target[-1]
                target.append(int(buf))
                buf = ''
            level -= 1
        elif c == ',':
            if buf:
                target = out[0]
                for i in range(level):
                    target = target[-1]
                target.append(int(buf))
                buf = ''
        else:
            buf += c

    return out[0][0]


RIGHT_ORDER = 1
WRONG_ORDER = 2
UNCERTAIN = 3


def is_in_right_order(left, right) -> bool:
    def compare_int(l: int, r: int) -> int:
        if l == r:
            return UNCERTAIN
        if l > r:
            return WRONG_ORDER
        return RIGHT_ORDER

    def compare_lists(l: List[int], r: List[int]) -> int:
        li, ri = 0, 0
        while li < len(l) and ri < len(r):
            result = compare(l[li], r[ri])
            if result == UNCERTAIN:
                li += 1
                ri += 1
            else:
                return result

        if li == len(l) and ri < len(r):
            return RIGHT_ORDER

        if li < len(l) and ri == len(r):
            return WRONG_ORDER

        return UNCERTAIN

    def compare(l, r):
        if type(l) == type(r) == int:
            return compare_int(l, r)

        if type(l) == type(r) == list:
            return compare_lists(l, r)

        if type(l) == int:
            return compare_lists([l], r)

        return compare_lists(l, [r])

    left_q, right_q = collections.deque(left), collections.deque(right)
    result = UNCERTAIN
    while result == UNCERTAIN and left_q and right_q:
        left_target, right_target = left_q.popleft(), right_q.popleft()
        result = compare(left_target, right_target)
        if result != UNCERTAIN:
            return result == RIGHT_ORDER

    if result == UNCERTAIN:
        return len(left_q) == 0

    return result == RIGHT_ORDER


p1_answer = 0
p2_answer = 1
packets = []
with open('real-input.txt') as f:
    idx = 1
    while True:
        left, right = parse(f.readline().strip()), parse(f.readline().strip())
        packets.extend([left, right])

        if is_in_right_order(left, right):
            p1_answer += idx

        empty_line = f.readline()
        if not empty_line:
            break
        idx += 1

    packets.extend([[[2]], [[6]]])
    packets.sort(key=functools.cmp_to_key(lambda a, b: -1 if is_in_right_order(a, b) else 1))
    i = 1
    for p in packets:
        if p in [[[2]], [[6]]]:
            p2_answer *= i
        i += 1

print('Part 1 answer: ', p1_answer)
print('Part 2 answer: ', p2_answer)
