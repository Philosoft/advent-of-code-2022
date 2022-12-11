import collections
import functools


class Monkey:
    def __init__(self):
        self.items = collections.deque([])
        self.original_items = []
        self.operation = None
        self.test_number = None
        self.positive_outcome_target = None
        self.negative_outcome_target = None
        self.items_inspected = 0
        self.factor_in_relief = True
        self.custom_reducer = 1

    def choose_target(self) -> int:
        if len(self.items) == 0:
            raise Exception('Cannot choose targets when empty handed')

        return self.positive_outcome_target if self.items[0] % self.test_number == 0 else self.negative_outcome_target

    def has_items(self) -> bool:
        return len(self.items) > 0

    def inspect(self) -> None:
        self.items_inspected += 1
        self.items[0] = self.operation(self.items[0])
        if self.factor_in_relief:
            self.items[0] //= 3
        else:
            self.items[0] %= self.custom_reducer

    def throw(self) -> int:
        return self.items.popleft()

    def catch(self, item: int) -> None:
        self.items.append(item)

    def reset(self):
        self.items = collections.deque(self.original_items.copy())
        self.items_inspected = 0


monkeys = []
initial_items = []
with open('real-input.txt') as f:
    while True:
        monkey_header = f.readline()
        if not monkey_header:
            break

        monkey = Monkey()
        items = list(map(lambda x: int(x.strip()), f.readline().strip().split(':')[1].split(',')))
        monkey.items = collections.deque(items.copy())
        monkey.original_items = items.copy()
        operation = f.readline().split('=')[1].strip()
        operator, constant = operation.split(' ')[1:]


        def generate_operation(monkey_operator: str, operand: str):
            def op(worry_level: int) -> int:
                monkey_constant = worry_level if operand == 'old' else int(operand)

                if monkey_operator == '*':
                    return worry_level * monkey_constant

                if monkey_operator == '+':
                    return worry_level + monkey_constant

                if monkey_operator == '/':
                    return worry_level // monkey_constant

                if monkey_operator == '-':
                    return worry_level - monkey_constant

            return op


        monkey.operation = generate_operation(operator, constant)

        monkey.test_number = int(f.readline().strip().split(' ')[-1])
        monkey.positive_outcome_target = int(f.readline().strip().split(' ')[-1])
        monkey.negative_outcome_target = int(f.readline().strip().split(' ')[-1])

        monkeys.append(monkey)
        f.readline()

for _ in range(20):
    for monkey in monkeys:
        while monkey.has_items():
            monkey.inspect()
            monkeys[monkey.choose_target()].catch(monkey.throw())

inspections = [m.items_inspected for m in monkeys]
inspections.sort()
print('Part 1: ', inspections[-2] * inspections[-1])

part_2_reducer = functools.reduce(lambda c, i: i * c, [m.test_number for m in monkeys], 1)
for monkey in monkeys:
    monkey.reset()
    monkey.factor_in_relief = False
    monkey.custom_reducer = part_2_reducer

for _ in range(10_000):
    for monkey in monkeys:
        while monkey.has_items():
            monkey.inspect()
            monkeys[monkey.choose_target()].catch(monkey.throw())

inspections = [m.items_inspected for m in monkeys]
inspections.sort()
print('Part 2: ', inspections[-2] * inspections[-1])
