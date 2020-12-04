# coding=utf-8
# --- Day 2: Password Philosophy ---

f = open('input.txt', 'r')

valid_first, valid_second = 0, 0

for line in f:
    tokens = line.strip().split(' ')
    fr, to = map(lambda x: int(x), tokens[0].split('-'))
    let = tokens[1][0]
    passwd = tokens[2]

    if passwd.count(let) in range(fr, to + 1):
        valid_first += 1

    valid_second += (passwd[fr - 1] == let) ^ (passwd[to - 1] == let)

f.close()

print("First part: ", valid_first)
print("Second part: ", valid_second)

