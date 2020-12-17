# --- Day 5: Binary Boarding ---

def compute_seat_id(s):
    rows, columns = s[:-4], s[-4:]

    left, right = 0, 127
    for r in rows:
        if r == 'F':
            right = (left + right) // 2
        else:
            left = (left + right) // 2

    row = right

    left, right = 0, 7

    for c in columns:
        if c == 'L':
            right = (left + right) // 2
        else:
            left = (left + right) // 2

    column = right

    return row * 8 + column


f = open('input.txt', 'r')
lines = [line for line in f]
f.close()

ids = map(compute_seat_id, lines)

print("First part: ", max(ids))
print("Second part:", sum(range(1, max(ids) + 1)) - sum(ids) - sum(range(1, min(ids))))
