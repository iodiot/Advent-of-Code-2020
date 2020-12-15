# --- Day 12: Rain Risk ---

DIRS = {'E': 1 + 0j, 'S': 0 - 1j, 'W': -1 + 0j, 'N': 0 + 1j}

actions = [line.strip() for line in open('input.txt')]
actions = list(map(lambda x: (x[0], int(x[1:])), actions))

ship_1 = 0 + 0j
ship_2 = 0 + 0j
waypoint = 10 + 1j
dir = DIRS['E']

for action in actions:
    let, step = action

    if let in DIRS:
        ship_1 += DIRS[let] * step
        waypoint += DIRS[let] * step
    elif let == 'F':
        ship_1 += dir * step
        ship_2 += waypoint * step
    elif let == 'L':
        dir *= complex(1j) ** (step // 90)
        waypoint *= complex(1j) ** (step // 90)
    elif let == 'R':
        dir *= complex(-1j) ** (step // 90)
        waypoint *= complex(-1j) ** (step // 90)
    else:
        raise Exception

print("First part: ", round(abs(ship_1.imag) + abs(ship_1.real)))
print("Second part: ", round(abs(ship_2.imag) + abs(ship_2.real)))
