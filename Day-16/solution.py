# --- Day 16: Ticket Translation ---

def to_range_included(s):
    left, right = s.split('-')
    return range(int(left), int(right) + 1)


def val_in_ranges(val, ranges):
    for r in ranges:
        if val in r:
            return True
    return False


lines = [line.strip() for line in open('input.txt')]

fields = {}

for line in lines[0:lines.index('')]:
    left, right = line.split(': ')
    fields[left] = list(map(lambda x: to_range_included(x), right.split(' or ')))

tickets = lines[lines.index('nearby tickets:') + 1:]
tickets.append(lines[lines.index('your ticket:') + 1])
tickets = list(map(lambda x: list(map(lambda y: int(y), x.split(','))), tickets))

your = tickets[-1]
nearby = tickets[0:-1]

error_rate = 0
all_ranges = [item for sublist in fields.values() for item in sublist]

valid_tickets = []

for ticket in nearby:
    valid_ticket = True
    for val in ticket:
        valid_val = False
        for r in all_ranges:
            if val in r:
                valid_val = True
                break

        if not valid_val:
            error_rate += val
            valid_ticket = False

    if valid_ticket:
        valid_tickets.append(ticket)

options = {}

for x in range(0, len(valid_tickets[0])):
    options[x] = set()
    for name in fields:
        in_ranges = True
        for y in range(0, len(valid_tickets)):
            in_ranges = in_ranges and val_in_ranges(valid_tickets[y][x], fields[name])

        if in_ranges:
            options[x].add(name)


options = {k: v for k, v in sorted(options.items(), key=lambda item: len(item[1]))}

exclude = set()

for row in options:
    options[row].difference_update(exclude)
    exclude.update(options[row])

departure_mult = 1

for row in options:
    if list(options[row])[-1].startswith('departure'):
        departure_mult *= your[row]

print("First part: ", error_rate)
print("Second part: ", departure_mult)
