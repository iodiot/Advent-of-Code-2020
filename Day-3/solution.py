# --- Day 3: Toboggan Trajectory ---

f = open('input.txt', 'r')
area = [line.strip() for line in f]
f.close()


def traverse(area, dx, dy):
    width = len(area[0])
    height = len(area)

    x, y = 0, 0

    trees = 0

    while y < height:
        if area[y][x % width] == '#':
            trees += 1

        x += dx
        y += dy

    return trees


print("First part: ", traverse(area, 3, 1))

print("Second part: ",
      traverse(area, 1, 1) * traverse(area, 3, 1)
      * traverse(area, 5, 1) * traverse(area, 7, 1)
      * traverse(area, 1, 2))
