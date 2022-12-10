from typing import Tuple


class Segment:
    def __init__(self, x: int = 0, y: int = 0, head=None):
        self.x = x
        self.y = y
        self.previous_x = x
        self.previous_y = y
        self.head = head
        self.visited_positions = {(x, y)}

    def get_position(self) -> Tuple[int, int]:
        return self.x, self.y

    def move(self, dx: int, dy: int) -> None:
        self.previous_x = self.x
        self.previous_y = self.y

        self.x += dx
        self.y += dy

        self.visited_positions.add((self.x, self.y))

    def chase(self) -> None:
        dx = self.head.x - self.x
        dy = self.head.y - self.y

        if dx in [1, -1, 0] and dy in [1, -1, 0]:
            return

        if dx in [1, 2] and dy in [1, 2]:
            self.move(1, 1)
        elif dx == 2 and dy == 0:
            self.move(1, 0)
        elif dx in [2, 1] and dy in [-1, -2]:
            self.move(1, -1)
        elif dx == 0 and dy == -2:
            self.move(0, -1)
        elif dx == 0 and dy == 2:
            self.move(0, 1)
        elif dx in [-1, -2] and dy in [-1, -2]:
            self.move(-1, -1)
        elif dx == -2 and dy == 0:
            self.move(-1, 0)
        elif dx in [-1, -2] and dy in [1, 2]:
            self.move(-1, 1)

    def get_visited_positions_count(self):
        return len(self.visited_positions)


class Snake:
    def __init__(self):
        self.segments = []

    def add_segment(self) -> None:
        segment = Segment()
        parent = self.segments[-1] if self.segments else None
        segment.head = parent
        self.segments.append(segment)

    def get_head(self) -> Segment:
        return self.segments[0]

    def get_tail(self) -> Segment:
        return self.segments[-1]

    def get_tail_coordinates(self) -> Tuple[int, int]:
        return self.get_tail().get_position()

    def move(self, dx: int, dy: int) -> None:
        self.get_head().move(dx, dy)
        for segment in self.segments[1:]:
            segment.chase()

    def up(self) -> None:
        self.move(0, 1)

    def down(self) -> None:
        self.move(0, -1)

    def right(self) -> None:
        self.move(1, 0)

    def left(self) -> None:
        self.move(-1, 0)

    def go(self, direction: str) -> None:
        if direction == 'R':
            self.right()
        elif direction == 'L':
            self.left()
        elif direction == 'D':
            self.down()
        elif direction == 'U':
            self.up()
        else:
            raise Exception(f'Unknown direction {direction}')

    def get_visited_locations_count_for_tail(self) -> int:
        return self.get_tail().get_visited_positions_count()


with open('real-input.txt') as f:
    snake1 = Snake()
    snake1.add_segment()
    snake1.add_segment()

    snake2 = Snake()
    for i in range(10):
        snake2.add_segment()

    for line in f:
        direction, steps = line.strip().split(' ')
        for i in range(int(steps)):
            snake1.go(direction)
            snake2.go(direction)

    print(f'Part 1: {snake1.get_visited_locations_count_for_tail()}')
    print(f'Part 2: {snake2.get_visited_locations_count_for_tail()}')
