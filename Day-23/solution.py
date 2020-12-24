# --- Day 23: Crab Cups ---

def run(cups, moves):
    curr = int(input[0])
    cups_len = len(cups)

    for move in range(0, moves):
        pick = [cups[curr], cups[cups[curr]], cups[cups[cups[curr]]]]

        dest = curr - 1
        if dest == 0:
            dest = cups_len

        while dest in pick:
            dest -= 1
            if dest == 0:
                dest = cups_len

        cups[curr] = cups[pick[-1]]

        tmp = cups[dest]
        cups[dest] = pick[0]
        cups[pick[-1]] = tmp

        curr = cups[curr]

    return cups


input = '364297581'

input_cups = {}

for i in range(0, len(input)):
    input_cups[int(input[i])] = int(input[(i + 1) % len(input)])

final_cups = run(input_cups.copy(), 100)

answer_1 = ''
curr = 1
while final_cups[curr] != 1:
    answer_1 += str(final_cups[curr])
    curr = final_cups[curr]

print("First part: ", answer_1)

input_cups[int(input[-1])] = 10
for i in range(10, 1000001):
    input_cups[i] = i + 1
input_cups[1000000] = int(input[0])

final_cups = run(input_cups, 10000000)

answer_2 = final_cups[1] * final_cups[final_cups[1]]
print("Second part: ", answer_2)
