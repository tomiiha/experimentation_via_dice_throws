# A function to generate x amount of dice throws for both a rigged, and fair dice.
def throw_dice(x):
    fair_dice_results = []
    rigged_dice_results = []

    # The rigged dice will produce more 4,5,6 values.
    rigged_dice_numbers = [1, 2, 3, 4, 4, 5, 5, 6, 6]

    for _ in range(x):
        fair_dice_results.append(random.randint(1, 6))
        rigged_dice_results.append(random.choice(rigged_dice_numbers))

    return fair_dice_results, rigged_dice_results
