# --- Day 17: Conway Cubes ---

import itertools

A = [-1, 0, 1]

OFFSETS_3D = [[x, y, z] for x, y, z in itertools.product(A, A, A)]
OFFSETS_3D.remove([0, 0, 0])

OFFSETS_4D = [[x, y, z, w] for x, y, z, w in itertools.product(A, A, A, A)]
OFFSETS_4D.remove([0, 0, 0, 0])


def count_neighbours(pocket, x, y, z, w, dims=3):
    num = 0

    for os in OFFSETS_3D if dims == 3 else OFFSETS_4D:
        if pocket.get((x + os[0], y + os[1], z + os[2], 0 if dims == 3 else w + os[3]), False):
            num += 1

    return num


def run(lines, dims=3):
    xy_range = range(-len(lines) // 2 + 1, len(lines) // 2 + 1)
    z_range = range(0, 1)
    w_range = range(0, 1)

    pocket = {}

    for y in xy_range:
        for x in xy_range:
            pocket[(x, y, 0, 0)] = lines[y - xy_range.start][x - xy_range.start] == '#'

    cycle, cycles = 0, 6
    while cycle < cycles:
        new_w_range = range(w_range.start - 1, w_range.stop + 1) if dims == 4 else w_range
        new_z_range = range(z_range.start - 1, z_range.stop + 1)
        new_xy_range = range(xy_range.start - 1, xy_range.stop + 1)
        new_pocket = {}

        for w in new_w_range:
            for z in new_z_range:
                for y in new_xy_range:
                    for x in new_xy_range:
                        n = count_neighbours(pocket, x, y, z, w, dims)
                        cube = pocket.get((x, y, z, w), False)
                        new_cube = False
                        if cube:
                            new_cube = (n == 2) or (n == 3)
                        else:
                            new_cube = (n == 3)
                        new_pocket[(x, y, z, w)] = new_cube

        pocket = new_pocket
        z_range, w_range, xy_range = new_z_range, new_w_range, new_xy_range

        cycle += 1

    return list(pocket.values()).count(True)


lines = [line.strip() for line in open('input.txt')]

print("First part: ", run(lines, dims=3))
print("Second part: ", run(lines, dims=4))
