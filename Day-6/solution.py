# --- Day 6: Custom Customs ---

f = open('input.txt', 'r')
lines = [line for line in f]
f.close()

groups = map(lambda x: x.replace('\n', ''), ''.join(lines).split('\n\n'))
sets = map(lambda x: len(set(x)), groups)

print("First part: ", sum(sets))

groups = ''.join(lines).split('\n\n')

count = 0

for group in groups:
    answers = group.split('\n')

    s = set(answers[0])

    for answer in answers:
        s.intersection_update(answer)

    count += len(s)

print("Second part: ", count)
