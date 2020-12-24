# --- Day 20: Jurassic Jigsaw ---

import math

SIZE = 10
SEA_MONSTER = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']


def rotate(tile, times):
    if times == 0:
        return tile

    new_tile = {}
    size = round(math.sqrt(len(tile)))

    for t in range(0, times):
        new_tile = {}
        for y in range(0, size):
            for x in range(0, size):
                new_tile[(size - y - 1, x)] = tile[(x, y)]

        tile = new_tile

    return new_tile


def flip(tile, horizontal=True):
    new_tile = {}
    size = round(math.sqrt(len(tile)))

    for y in range(0, size):
        for x in range(0, size):
            if horizontal:
                new_tile[(size - x - 1, y)] = tile[(x, y)]
            else:
                new_tile[(x, size - y - 1)] = tile[(x, y)]

    return new_tile


def find_adjacent_for(tile_id, variants):
    result = []

    for this_tile in [rotate(variants[tile_id][0], i) for i in range(0, 4)]:
        this_hash = get_tile_hash(this_tile)
        for other_tile_id in variants.keys():
            if tile_id != other_tile_id:
                for variant in variants[other_tile_id]:
                    if this_hash == get_tile_hash(variant):
                        result.append(other_tile_id)
                        break

    return result


def orient_tile(tile_variants, prev_tile, tile_edge, prev_tile_edge):
    prev_hash = get_tile_hash(prev_tile, prev_tile_edge)
    for this_tile in tile_variants:
        if get_tile_hash(this_tile, tile_edge) == prev_hash:
            return this_tile

    return None


def generate_variants_for(tile):
    variants = []

    for rot in range(0, 4):
        new_tile = rotate(tile, rot)
        variants.append(new_tile)
        variants.append(flip(new_tile, horizontal=False))

    return variants


def get_tile_hash(tile, edge='t'):
    hash = ''
    for x in range(0, SIZE):
        if edge == 't':
            hash += tile[(x, 0)]
        elif edge == 'b':
            hash += tile[(x, SIZE - 1)]
        elif edge == 'l':
            hash += tile[(0, x)]
        else:
            hash += tile[(SIZE - 1, x)]

    return hash


def prod(arr):
    p = 1
    for a in arr:
        p *= a
    return p


def get_expected_tile_level(x, y, tile_map_size):
    s = tile_map_size - 1
    if (x, y) in [(0, 0), (0, s), (s, 0), (s, s)]:
        return 2
    elif x == 0 or y == 0 or x == s or y == s:
        return 3
    else:
        return 4


def is_sea_monster_here(sea_tile, pos):
    size = round(math.sqrt(len(sea_tile)))

    for y in range(0, len(SEA_MONSTER)):
        for x in range(0, len(SEA_MONSTER[y])):
            xx, yy = pos[0] + x, pos[1] + y
            if xx < 0 or xx >= size or yy < 0 or yy >= size:
                return False

            if SEA_MONSTER[y][x] == '#' and sea_tile[(xx, yy)] != '#':
                return False

    return True


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

real_tile_levels = {}

for tile_id in tiles.keys():
    adj_tiles = find_adjacent_for(tile_id, variants)
    real_tile_levels[tile_id] = len(adj_tiles)

    if len(adj_tiles) == 2:
        corners.append(tile_id)

#print(corners)
print("First part: ", prod(corners))


tile_map_size = round(math.sqrt(len(tiles.keys())))
tile_map = {(0, 0): corners[0]}

# 5 is pure guess in this case, means that the left-top corner is oriented thus
sea_map = {(0, 0): variants[corners[0]][5]}

my_tile_ids = list(tiles.keys())
my_tile_ids.remove(corners[0])

for y in range(0, tile_map_size):
    for x in range(0, tile_map_size):

        if x == 0 and y == 0:
            continue

        expected_level = get_expected_tile_level(x, y, tile_map_size)

        for tile_id in [id for id in my_tile_ids if expected_level == real_tile_levels[id]]:
            adj_tiles = find_adjacent_for(tile_id, variants)

            if (x > 0 and tile_map[(x - 1, y)] in adj_tiles) or (x == 0):
                if (y > 0 and tile_map[(x, y - 1)] in adj_tiles) or (y == 0):

                    tile_map[(x, y)] = tile_id

                    if x > 0:
                        sea_map[(x, y)] = orient_tile(variants[tile_id], sea_map[(x - 1, y)], 'l', 'r')
                    else:
                        sea_map[(x, y)] = orient_tile(variants[tile_id], sea_map[(x, y - 1)], 't', 'b')

                    my_tile_ids.remove(tile_id)
                    break

lines = []

for y in range(0, tile_map_size * SIZE):
    line = ''
    for x in range(0, tile_map_size * SIZE):
        xx, yy = x % SIZE, y % SIZE

        if xx > 0 and yy > 0 and xx < SIZE - 1 and yy < SIZE - 1:
            z = sea_map[(x // SIZE, y // SIZE)]
            zz = z[xx, yy]
            line += str(zz)

    if line != '':
        lines.append(line)

sea_tile = {}
for y in range(0, len(lines)):
    for x in range(0, len(lines)):
        sea_tile[(x, y)] = lines[y][x]

size = round(math.sqrt(len(sea_tile)))
for tile in generate_variants_for(sea_tile):
    n = 0
    for y in range(0, size):
        for x in range(0, size):
            if is_sea_monster_here(tile, (x, y)):
                n += 1

    if n > 0:
        print("Second part: ", list(tile.values()).count('#') - n * ''.join(SEA_MONSTER).count('#'))
        break


