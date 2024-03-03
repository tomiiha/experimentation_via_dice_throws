def play_games(number_of_games,dice_throws):
    fair_dice_wins = 0
    rigged_dice_wins = 0
    ties = 0

    for _ in range(number_of_games):
        fair_dice, rigged_dice = throw_dice(dice_throws)

        if sum(fair_dice) > sum(rigged_dice):
            fair_dice_wins += 1
        elif sum(fair_dice) < sum(rigged_dice):
            rigged_dice_wins += 1
        else:
            ties += 1

    # Displaying the results
    print(f"Games Played: {dice_throws}")
    print(f"Fair Dice Wins: {fair_dice_wins}")
    print(f"Rigged Dice Wins: {rigged_dice_wins}")
    print(f"Ties: {ties}")

    return fair_dice, rigged_dice
