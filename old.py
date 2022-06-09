from random import randint

winner = None
player_scores = [0] * 12
total_rounds = 0


def roll_dice(n):
    return [randint(1, 6) for i in range(n)]


def get_two_biggest(arr):
    return sorted(arr)[-2:]


def is_draw():
    biggest = get_two_biggest(player_scores)
    if biggest[0] == biggest[1]:
        return player_scores.index(biggest[0]), player_scores.index(biggest[1])


while winner is None:
    for _ in range(3):
        for i in range(len(player_scores)):
            dice = roll_dice(34)
            for die in dice:
                print(f"Player {i+1} rolled a {die}")
            biggest1, biggest2 = get_two_biggest(dice)
            player_scores[i] += biggest1 + biggest2
            print(
                f"{biggest1 + biggest2} points were added to player {i+1}'s score"
            )
            if biggest1 == biggest2:
                if biggest1 == 6:
                    player_scores[i] += 6
                    print(
                        f"A bonus 6 points were added to player {i+1}'s score")
                else:
                    player_scores[i] += 5
                    print(
                        f"A bonus 5 points were added to player {i+1}'s score")
            print()

        total_rounds += 1
        print(f"Scores for round {total_rounds}:")
        for i, score in enumerate(player_scores):
            print(f"Player {i+1}: {score} points")
        print()

    draw = is_draw()
    if not draw:
        winner = player_scores.index(max(player_scores))
        print(f"Player {winner+1} won with score {player_scores[winner]}!")
    else:
        print(f"Draw between players {draw[0]+1} and {draw[1]+1}")
        print()
