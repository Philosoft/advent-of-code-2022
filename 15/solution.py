import dataclasses
import re


@dataclasses.dataclass
class Point:
    x: int
    y: int


@dataclasses.dataclass
class Sensor:
    position: Point
    beacon: Point

    def get_beacon_distance(self):
        return abs(self.position.x - self.beacon.x) + abs(self.position.y - self.beacon.y)


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
        distance = s.get_beacon_distance()
        diff = abs(target_y - s.position.y)
        if diff <= distance:
            dx = distance - diff
            for x in range(s.position.x - dx, s.position.x + dx):
                covered.add(x)

    print(len(covered))
