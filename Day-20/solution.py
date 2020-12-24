# --- Day 20: Jurassic Jigsaw ---

SIZE = 10


def rotate(tile, times):
    if times == 0:
        return tile

    new_tile = {}

    for t in range(0, times):
        new_tile = {}
        for y in range(0, SIZE):
            for x in range(0, SIZE):
                new_tile[(SIZE - y - 1, x)] = tile[(x, y)]

        tile = new_tile

    return new_tile


def flip(tile, horizontal=True):
    new_tile = {}

    for y in range(0, SIZE):
        for x in range(0, SIZE):
            if horizontal:
                new_tile[(SIZE - x - 1, y)] = tile[(x, y)]
            else:
                new_tile[(x, SIZE - y - 1)] = tile[(x, y)]

    return new_tile


def print_tile(tile):
    for y in range(0, SIZE):
        line = ''
        for x in range(0, SIZE):
            line += tile[(x, y)]
        print(line)
    print('-' * SIZE)


def count_adjacent_for(tile, variants):
    n = 0
    this_hash = get_tile_hash(tile)

    for other_tile_id in variants.keys():
        if tile_id != other_tile_id:
            for variant in variants[other_tile_id]:
                if this_hash == get_tile_hash(variant):
                    n += 1
                    break

    return n


def generate_variants_for(tile):
    variants = []

    for rot in range(0, 4):
        new_tile = rotate(tile, rot)
        variants.append(new_tile)
        variants.append(flip(new_tile, horizontal=False))

    return variants


def get_tile_hash(tile):
    hash = ''
    for x in range(0, SIZE):
        hash += tile[(x, 0)]
    return hash


def prod(arr):
    p = 1
    for a in arr:
        p *= a
    return p


tiles = {}
lines = [line for line in open('input.txt')]

for i in range(0, len(lines), 12):
    tile_id = int(lines[i].split(' ')[1].strip('\n').strip(':'))
    tiles[tile_id] = {}

    for y in range(0, SIZE):
        for x in range(0, SIZE):
            tiles[tile_id][(x, y)] = lines[i + y + 1][x]

variants = {}

for tile_id in tiles.keys():
    variants[tile_id] = generate_variants_for(tiles[tile_id])

corners = []

for tile_id in tiles.keys():
    n = 0

    for tile in [rotate(variants[tile_id][0], i) for i in range(0, 4)]:
        n += count_adjacent_for(tile, variants)

    if n == 2:
        corners.append(tile_id)


print(corners)

print("First part: ", prod(corners))

import math

tile_map_size = round(math.sqrt(len(tiles.keys())))
tile_map = {(0, 0): corners[0]}

for y in range(0, tile_map_size):
    for x in range(0, tile_map_size):
        if (x, y) not in tile_map:



print("Second part: ", )
