# A function to generate x amount of dice throws for both a rigged, and fair dice.
def throw_dice(x,rigging=1):
    fair_dice_results = []
    rigged_dice_results = []

    # The lightly rigged dice will produce more 6 values.
    if rigging == 1:
        rigged_dice_numbers = [1, 2, 3, 4, 5, 6, 6]

    # The heavily rigged dice will produce more 4,5,6 values.
    elif rigging == 2:
        rigged_dice_numbers = [1, 2, 3, 4, 4, 5, 5, 6, 6]
        
    else:
        # Handling cases where rigging is not 1 or 2
        raise ValueError("Invalid rigging option. Please choose 1 or 2.")

    for _ in range(x):
        fair_dice_results.append(random.randint(1, 6))
        rigged_dice_results.append(random.choice(rigged_dice_numbers))

    return fair_dice_results, rigged_dice_results
