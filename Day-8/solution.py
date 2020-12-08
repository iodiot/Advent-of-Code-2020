# --- Day 8: Handheld Halting ---

def run(code):
    acc, ptr = 0, 0

    executed = []
    terminates = True

    while ptr < len(code):
        if ptr in executed:
            terminates = False
            break

        executed.append(ptr)

        op, arg = code[ptr].split(' ')
        arg = int(arg)

        if op == 'acc':
            acc += arg
            ptr += 1
        elif op == 'jmp':
            ptr += arg
        elif op == 'nop':
            ptr += 1
        else:
            raise Exception

    return acc, terminates


lines = [line.strip() for line in open('input.txt')]

print "First part: ", run(lines)[0]

for i in range(0, len(lines)):
    tmp = lines[i]

    op, arg = lines[i].split(' ')

    new_op = op

    if op == 'jmp':
        new_op = 'nop'
    elif op == 'nop':
        new_op = 'jmp'

    lines[i] = '{0} {1}'.format(new_op, arg)

    result = run(lines)

    lines[i] = tmp

    if result[1]:
        print "Second part: ", result[0]
