# --- Day 12: Rain Risk ---

DIRS = 'ESWN'
VECTORS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

actions = [line.strip() for line in open('input.txt')]
actions = map(lambda x: (x[0], int(x[1:])), actions)

print actions

d, x, y = 0, 0, 0

for action in actions:
    let, step = action

    if let in DIRS:
        x += VECTORS[DIRS.index(let)][0] * step
        y += VECTORS[DIRS.index(let)][1] * step
    elif let == 'F':
        x += VECTORS[d][0] * step
        y += VECTORS[d][1] * step
    elif let == 'L':
        z = d
        d = (d - step // 90)
        if d < 0:
            d += 4
        print action, DIRS[z], '->', DIRS[d]
    elif let == 'R':
        z = d
        d = (d + step // 90) % 4
        print action, DIRS[z], '->', DIRS[d]
    else:
        raise Exception

    #print action, x, y

print ("First part: ", abs(x + y))
print ("Second part: ", 0)

# 1199 -- 1400