# --- Day 9: Encoding Error ---

preamble = 25
numbers = [int(line.strip()) for line in open('input.txt', 'r')]

invalid_num = -1

for k in range(preamble, len(numbers)):
    seq = sorted(numbers[k - preamble:k])

    found = False

    for i in range(0, len(seq) - 1):
        for j in range(i + 1, len(seq)):
            if seq[i] + seq[j] == numbers[k]:
                found = True
                break

    if not found:
        invalid_num = numbers[k]
        break

enc_weakness = -1

for i in range(0, len(numbers) - 1):
    if enc_weakness != -1:
        break

    for j in range(i + 1, len(numbers)):
        seq = numbers[i:j + 1]
        if sum(seq) == invalid_num:
            enc_weakness = min(seq) + max(seq)
            break
        elif sum(seq) > invalid_num:
            break

print("First part: ", invalid_num)
print("Second part: ", enc_weakness)
