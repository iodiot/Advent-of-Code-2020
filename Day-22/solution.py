# --- Day 22: Crab Combat ---

from collections import deque


def play_game(deck_1, deck_2, recursive=False):
    prev_games = []

    while len(deck_1) > 0 and len(deck_2) > 0:
        if recursive:
            game_hash = '*'.join(str(el) for el in deck_1) + '/' + '*'.join(str(el) for el in deck_2)
            if game_hash in prev_games:
                return True, deck_1
            else:
                prev_games.append(game_hash)

        draw_1, draw_2 = deck_1.popleft(), deck_2.popleft()

        first_is_winner = draw_1 > draw_2

        if recursive and len(deck_1) >= draw_1 and len(deck_2) >= draw_2:
            subgame_result = play_game(deque(list(deck_1)[0:draw_1]), deque(list(deck_2)[0:draw_2]), recursive)
            first_is_winner = subgame_result[0]

        if first_is_winner:
            deck_1.append(draw_1)
            deck_1.append(draw_2)
        else:
            deck_2.append(draw_2)
            deck_2.append(draw_1)

    return len(deck_1) > 0, deck_1 if len(deck_1) > 0 else deck_2


def calc_score(game_result):
    deck = game_result[1]
    score = 0
    for i in range(0, len(deck)):
        score += deck[i] * (len(deck) - i)

    return score


lines = [line.strip() for line in open('input.txt')]

deck_1 = deque(map(lambda x: int(x), lines[1: lines.index('')]))
deck_2 = deque(map(lambda x: int(x), lines[lines.index('') + 2:]))

print("First part: ", calc_score(play_game(deck_1.copy(), deck_2.copy(), recursive=False)))
print("Second part: ", calc_score(play_game(deck_1.copy(), deck_2.copy(), recursive=True)))
