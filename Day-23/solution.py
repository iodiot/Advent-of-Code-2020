# --- Day 23: Crab Cups ---

from blist import blist


def print_move(move, cups, curr, pick, dest):
    print('-- move {0} --'.format(move + 1))
    line = ''
    for cup in cups:
        if cup == curr:
            line += '({0}) '.format(cup)
        else:
            line += '{0} '.format(cup)
    print('cups:', line)
    line = ''
    for cup in pick:
        line += '{0} '.format(cup)
    print('pick up:', line)
    print('destination:', dest)
    print()


input = '389125467'

cups = blist(map(lambda x: int(x), input))

#for i in range(10, 1001):
#    cups.append(i)

curr, moves = cups[0],  100

CUPS_LEN = len(cups)

for move in range(0, moves):
    pick = []
    pos = cups.index(curr) + 1
    for i in range(0, 3):
        pick.append(cups[(pos + i) % CUPS_LEN])

    dest = curr - 1
    if dest == 0:
        dest = CUPS_LEN

    while dest in pick:
        dest -= 1
        if dest == 0:
            dest = CUPS_LEN

    #print_move(move, tmp_cups, curr, pick, dest)

    for cup in pick:
        cups.remove(cup)

    pos = cups.index(dest) + 1
    for cup in reversed(pick):
        cups.insert(pos, cup)

    curr = cups[(cups.index(curr) + 1) % CUPS_LEN]

pos = cups.index(1)
answer = ''.join(map(lambda x: str(x), cups[pos + 1:] + cups[0:pos]))
print("First part: ", answer)

# pos = cups.index(1)
# answer_2 = cups[(pos + 1) % CUPS_LEN] * cups[(pos + 2) % CUPS_LEN]
# print(pos, cups[(pos + 1) % CUPS_LEN], cups[(pos + 2) % CUPS_LEN])
#
# print("Second part: ", answer_2)
