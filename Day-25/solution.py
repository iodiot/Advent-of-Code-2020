# --- Day 25: Combo Breaker ---

def calc_loop_size(public_key):
    loops, n = 1, 1
    while True:
        n = (n * 7) % 20201227
        if n == public_key:
            break
        loops += 1
    return loops


card_public, door_public = [int(line) for line in open('input.txt')]

card = 1

for i in range(0, calc_loop_size(door_public)):
    card = (card * card_public) % 20201227

print("Final answer: ", card)

