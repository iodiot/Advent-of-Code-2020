# --- Day 24: Lobby Layout ---

import re

VECTORS \
    = {'e': (+1, -1, 0), 'se': (0, -1, +1), 'sw': (-1, 0, +1), 'w': (-1, +1, 0), 'nw': (0, +1, -1), 'ne': (+1, 0, -1)}


def count_black_adjacent(grid, pos):
    n = 0
    for vec in VECTORS.values():
        adj_pos = (pos[0] + vec[0], pos[1] + vec[1], pos[2] + vec[2])
        if adj_pos in grid:
            if not grid[adj_pos]:
                n += 1

    return n


lines = [line.strip() for line in open('input.txt')]

grid = {}

for line in lines:
    moves = [el for el in re.split('(e|se|sw|w|nw|ne)', line) if el != '']
    pos = [0, 0, 0]
    for move in moves:
        pos[0] += VECTORS[move][0]
        pos[1] += VECTORS[move][1]
        pos[2] += VECTORS[move][2]

    if tuple(pos) not in grid:
        grid[tuple(pos)] = False
    else:
        grid[tuple(pos)] = not grid[tuple(pos)]

print("First part: ", list(grid.values()).count(False))

for day in range(0, 100):
    new_grid = {}

    all_pos = []

    for pos in grid.keys():
        if not grid[pos]:
            all_pos.append(pos)
            for vec in VECTORS.values():
                adj_pos = (pos[0] + vec[0], pos[1] + vec[1], pos[2] + vec[2])
                if adj_pos not in all_pos:
                    all_pos.append(adj_pos)

    for pos in all_pos:
        n = count_black_adjacent(grid, pos)
        is_white = (pos not in grid) or grid[pos]

        if is_white:
            new_grid[pos] = n != 2
        else:
            new_grid[pos] = (n == 0) or (n > 2)

    grid = new_grid

    print('Day', day + 1, ':', list(grid.values()).count(False))

print("Second part: ", list(grid.values()).count(False))
