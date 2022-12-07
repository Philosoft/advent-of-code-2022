import collections
import sys
from collections import defaultdict


class Node:
    def __init__(self, path: str, size: int = 0):
        self.path = path
        self.name = path.strip('/').split('/')[-1]
        self.size = size
        self.parent = None
        self.children = {}

    def add_child(self, child) -> None:
        child.parent = self
        p = child.parent
        while p:
            p.size += child.size
            p = p.parent

        self.children[child.name] = child

    def add_child_by_path(self, path: str, size: int) -> None:
        if self.name != '' or self.parent:
            raise Exception('Method add_child_by_path can be used only on root node')

        target = self
        path_so_far = '/'
        parts = path.strip('/').split('/')
        for dirname in parts[0:-1]:
            path_so_far += dirname + '/'
            child = target.get_child_by_name(dirname)
            if not child:
                child = Node(path_so_far)
                target.add_child(child)

            target = child

        if len(parts) > 1:
            path_so_far += parts[-1] + '/'

        target.add_child(Node(path_so_far, size))

    def get_child_by_path(self, path: str):
        if self.name != '' or self.parent:
            raise Exception('Method must be used only on root node')

        target = self
        stack = ['']
        for dirname in path.strip('/').split('/'):
            target = target.get_child_by_name(dirname)
            if not target:
                raise Exception(f'{path} is not correct. There is no "{dirname}" in "{"/".join(stack)}"')
            stack.append(dirname)

        return target

    def get_child_by_name(self, dirname: str):
        return self.children[dirname] if dirname in self.children else None

    def get_all_children(self):
        return self.children.values()


with open('input.txt') as f:
    path_history = []
    sizes = defaultdict(lambda: 0)
    skip_next_read = False
    tree = Node('/')

    line = f.readline()
    while line:
        line = line.strip()
        if line.startswith('$'):
            args = line.split(' ')
            cmd = args[1]
            if cmd == 'cd':
                directory = args[2]
                if directory == '..':
                    if len(path_history) > 0:
                        path_history.pop()
                    else:
                        path_history = ['']
                else:
                    path_history.append(f'{directory}/'.replace('//', '/'))
            elif cmd == 'ls':
                line = f.readline()
                cwd = ''.join(path_history)
                while line and not line.startswith('$'):
                    if not line.startswith('dir'):
                        file_size = int(line.split(' ')[0])
                        sizes[cwd] += file_size

                    line = f.readline()
                tree.add_child_by_path(cwd, sizes[cwd])

                if line and line.startswith('$'):
                    skip_next_read = True
            else:
                raise Exception(f'Unknown command {cmd}')

        if not skip_next_read:
            line = f.readline()
        else:
            skip_next_read = False

    answer_p1 = 0
    answer_p2 = sys.maxsize

    TOTAL_SPACE = 70000000
    UPDATE_SIZE = 30000000
    free_space = TOTAL_SPACE - tree.size
    needed_space = UPDATE_SIZE - free_space
    q = collections.deque([tree])
    while len(q) > 0:
        for i in range(len(q)):
            current = q.popleft()
            for child in current.get_all_children():
                q.append(child)

            if current.size < 100000:
                answer_p1 += current.size

            if current.size >= needed_space:
                answer_p2 = min(answer_p2, current.size)

    print(f'Part 1: {answer_p1}')
    print(f'Part 2: {answer_p2}')
