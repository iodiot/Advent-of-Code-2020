# --- Day 14: Docking Data ---

lines = [line.strip() for line in open('input.txt')]

mem = {}
mask = ''

for line in lines:
    left, right = line.split('=')
    if left.strip() == 'mask':
        mask = right
    else:
        addr = (left[4:-2])
        val = '{:037b}'.format(int(right.strip()))
        new_val = ''
        for i in range(0, len(mask)):
            if mask[i] == 'X':
                new_val += val[i]
            else:
                new_val += mask[i]

        mem[addr] = int(new_val, 2)

print ("First part: ", sum(mem.values()))
