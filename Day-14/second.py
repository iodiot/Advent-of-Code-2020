# --- Day 14: Docking Data ---

lines = [line.strip() for line in open('input.txt')]

mem = {}
mask = ''

for line in lines:
    left, right = line.split('=')

    if left.strip() == 'mask':
        mask = right
    else:
        addr = '{:037b}'.format(int((left[4:-2])))
        val = int(right.strip())

        addr_list = ['']

        for i in range(0, len(mask)):
            new_addr_list = []
            for in_addr in addr_list:
                if mask[i] == 'X':
                    new_addr_list.append(in_addr + '0')
                    new_addr_list.append(in_addr + '1')
                elif mask[i] == '0':
                    new_addr_list.append(in_addr + addr[i])
                else:
                    new_addr_list.append(in_addr + '1')
            addr_list = new_addr_list

        for in_addr in addr_list:
            mem[int(in_addr, 2)] = val

print ("Second part: ", sum(mem.values()))
