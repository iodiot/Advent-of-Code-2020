# --- Day 11: Seating System ---

import itertools

DIRS = [[i, j] for i, j in itertools.product([-1, 0, 1], [-1, 0, 1])]
DIRS.remove([0, 0])


def count_adjacent(layout, x, y):
    w, h = len(layout[0]), len(layout)

    occupied = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not (i == x and j == y) and 0 <= i < w and 0 <= j < h:
                if layout[j][i] == '#':
                    occupied += 1

    return occupied


def count_visible(layout, x, y):
    w, h = len(layout[0]), len(layout)

    occupied = 0

    for dir in DIRS:
        i, j = x + dir[0], y + dir[1]
        while 0 <= i < w and 0 <= j < h:
            if layout[j][i] == '#':
                occupied += 1
                break
            elif layout[j][i] == 'L':
                break

            i += dir[0]
            j += dir[1]

    return occupied


def run(count_func, tolerance):
    layout = [list(line.strip()) for line in open('input.txt')]
    w, h = len(layout[0]), len(layout)

    while True:
        new_layout = []

        changed = False

        for y in range(0, h):
            new_layout.append([])

            for x in range(0, w):
                new_layout[y].append(layout[y][x])

                n = count_func(layout, x, y)

                if layout[y][x] == 'L' and n == 0:
                    new_layout[y][x] = '#'
                    changed = True
                elif layout[y][x] == '#' and n >= tolerance:
                    new_layout[y][x] = 'L'
                    changed = True

        layout = new_layout

        if not changed:
            break

    return ''.join(map(lambda x: ''.join(x), layout)).count('#')


print("First part: ", run(count_adjacent, 4))
print("Second part: ", run(count_visible, 5))
