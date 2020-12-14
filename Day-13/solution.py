# --- Day 13: Shuttle Search ---

lines = [line.strip() for line in open('input.txt')]

earliest = int(lines[0])
buses = ['x' if bus == 'x' else int(bus) for bus in lines[1].split(',')]

min_time = 100 ** 100
min_bus = -1

for bus in buses:
    if bus != 'x':
        time = (earliest // bus) * bus
        if time < earliest:
            time += bus

        if time < min_time:
            min_time = time
            min_bus = bus

print ("First part: ", min_bus * (min_time - earliest))

# http://math.csu.ru/new_files/students/lectures/teor_chisel/mitina_resh_zadach.pdf
# t = Bn (mod Mn)
# M = M1 * M2 * ... * Mn


def prod(arr):
    p = 1
    for a in arr:
        p *= a
    return p


def iterative_egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q # use x//y for floor "floor division"
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y


def mod_inv(a, m):
    g, x, y = iterative_egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


M = prod([bus for bus in buses if bus != 'x'])

b, m, m_stroke, mods = [], [], [], []
for i in range(0, len(buses)):
    bus = buses[i]
    if bus != 'x':
        mods.append(bus)
        b.append(bus - i)
        m.append(M // bus)
        m_stroke.append(mod_inv(M // bus, bus))

t = 0
for i in range(0, len(b)):
    t += m[i] * m_stroke[i] * b[i]

print ("Second part: ", t % M)
