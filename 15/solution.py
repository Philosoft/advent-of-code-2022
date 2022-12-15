from dataclasses import dataclass
import re

MIN_COORD = 0
MAX_COORD = 4000000


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Sensor:
    position: Point
    beacon: Point

    @property
    def beacon_distance(self):
        return abs(self.position.x - self.beacon.x) + abs(self.position.y - self.beacon.y)

    @property
    def perimeter(self):
        # pinnacle

        # top
        yield Point(self.position.x, self.position.y + self.beacon_distance + 1)
        # left
        yield Point(self.position.x - 1, self.position.y + self.beacon_distance)
        # right
        yield Point(self.position.x + 1, self.position.y + self.beacon_distance)

        # top to bottom
        traveled = 1
        for y in range(self.position.y + self.beacon_distance, self.position.y - 1, -1):
            left, right = Point(self.position.x - traveled - 1, y), Point(self.position.x + traveled + 1, y)
            yield left
            yield right

            traveled += 1

        # sensor line
        # left
        yield Point(self.position.x - self.beacon_distance - 1, self.position.y)
        # right
        yield Point(self.position.x + self.beacon_distance + 1, self.position.y)

        traveled = self.beacon_distance
        for y in range(self.position.y + 1, self.position.y + self.beacon_distance):
            left, right = Point(self.position.x - traveled, y), Point(x + traveled, y)
            yield left
            yield right

            traveled -= 1

        # the very bottom
        yield Point(self.position.x, self.position.y + self.beacon_distance + 1)

    def has(self, p: Point) -> bool:
        return abs(p.x - self.position.x) + abs(p.y - self.position.y) <= self.beacon_distance


with open('real-input.txt') as f:
    beacons = []
    sensors = []

    for line in f:
        r = re.compile('=(-?\\d+)')
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, r.findall(line))
        sensor_position = Point(sensor_x, sensor_y)
        beacon_position = Point(beacon_x, beacon_y)

        sensors.append(Sensor(sensor_position, beacon_position))

    covered = set()
    target_y = 2000000
    for s in sensors:
        diff = abs(target_y - s.position.y)
        if diff <= s.beacon_distance:
            dx = s.beacon_distance - diff
            for x in range(s.position.x - dx, s.position.x + dx):
                covered.add(x)

    print('Part 1: ', len(covered))
    del covered

    for s in sensors:
        # walk along perimeter + 1, check if it's inside any other sensor "field" - skip it
        for p in s.perimeter:
            found = [0] * len(sensors)
            i = 0
            for s_ in sensors:
                if s == s_:
                    continue

                if 0 <= p.x <= MAX_COORD and 0 <= p.y <= MAX_COORD:
                    if s_.has(p):
                        found[i] = 1
                else:
                    found[i] = 1
                i += 1

            if sum(found) == 0:
                print('Part 2: ', p.x * 4000000 + p.y)
                print(p)
                exit()
