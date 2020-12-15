# --- Day 15: Rambunctious Recitation ---

def run(starting, year):
    turns = [int(x) for x in starting.split(',')]

    mem = {}

    for i in range(0, len(turns)):
        mem[turns[i]] = [i]

    while len(turns) < year:
        curr, last = -1, turns[-1]
        if len(mem.get(last, [])) == 1:
            curr = 0
        else:
            curr = len(turns) - 1 - mem[last][-2]

        if curr not in mem:
            mem[curr] = []

        mem[curr].append(len(turns))

        turns.append(curr)

    return turns[-1]


print("First part: ", run('1,12,0,20,8,16', 2020))
print("Second part: ", run('1,12,0,20,8,16', 30000000))
