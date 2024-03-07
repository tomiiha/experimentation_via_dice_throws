# Experimentation via Dice Throws

A quick set of scripts to test out some automatic ways to run experimentation, metrics related to experimentation, and possible t-tests. All generated for fun, just to conceptualize approaches for some simple problems!

Scripts:
- throw_dice.py: A simple function to use to generate two sets of dice throw results, where one player is cheating (either cheating lightly, or heavily).
- play_games.py: Takes the generated dice throws and applies them to a made-up game, where two players keep throwing dice to determine the winner of a series of throw sets. As far as I know this isn't a real game, just made it up in the moment as a simple concept.
- analyze_dice_rolls.py: This script then takes the output of such a dice game, and applies some general statistics onto it to measure how the outcome could be tested. By default these outcomes are not printed, but can be.
- perform_t_test.py: This is the final script that based on the outcome of the analytics, either runs a t-test, or a Welch's t-test to evaluate whether with the sample generated, we can prove our friend is a cheater!
    - *Note: The scripts are not designed to always produce a meaningful result, and p-values are likely not going to be significant each time the scritps are run.*


