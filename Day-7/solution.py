# --- Day 7: Handy Haversacks ---

def contains_shiny_bag(rules, name):
    if name not in rules:
        return False

    contains = False

    for other_bag in rules[name]:
        other_name = other_bag['name']
        if other_name == 'shiny gold bag':
            return True
        else:
            contains |= contains_shiny_bag(rules, other_name)

    return contains


def count_bags_inside(rules, name):
    if name not in rules:
        return 0

    sum = 0

    for other_bag in rules[name]:
        other_name, other_n = other_bag['name'], other_bag['n']
        sum += other_n + other_n * count_bags_inside(rules, other_name)

    return sum


f = open('input.txt', 'r')

rules = {}

for line in f:
    new_line = '0 ' + line.strip().replace('contain', ',')
    bags = []

    for bag in new_line.split(','):
        temp = bag.strip(' ').split(' ')
        if temp[0] != 'no':
            n, name = int(temp[0]), ' '.join(temp[1:]).rstrip('.').rstrip('s')
            bags.append({'name': name, 'n': n})

    name = bags[0]['name']

    for bag in bags[1:]:
        if name not in rules:
            rules[name] = []
        rules[name].append({'name': bag['name'], 'n': bag['n']})

f.close()

print "First part: ", sum(map(lambda x: contains_shiny_bag(rules, x), rules.keys()))
print "Second part: ", count_bags_inside(rules, 'shiny gold bag')

