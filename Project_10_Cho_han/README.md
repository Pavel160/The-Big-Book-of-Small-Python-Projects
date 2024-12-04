# Cho-Han: The Japanese Dice Game
**Author**: Al Sweigart (al@inventwithpython.com)

Welcome to **Cho-Han**, a Python implementation of the traditional Japanese dice game! In this game, you'll place a bet on whether the sum of two dice will be **odd** ("Han") or **even** ("Cho"). Will you guess correctly or be out of luck? Only the roll of the dice can tell!

# How to Play
Once you have the game set up, playing is simple and fun! Just run the script and place your bet.

## Basic Gameplay Flow:
1. The game asks you to choose a bet: Cho (even) or Han (odd).
2. The computer rolls two dice and announces the result.
3. If your bet matches the sum of the dice (even or odd), you win! Otherwise, you lose.

## Example Run
   ```yaml
Welcome to Cho-Han! Make your bet.
Your options: Cho (even) / Han (odd)

Please enter your bet: Cho

Rolling the dice... 🎲
Dice 1: 4
Dice 2: 6
Sum: 10 (Even)

You win! The result was Cho! 🎉
   ```
### Or, if you're unlucky:
   ```yaml
Welcome to Cho-Han! Make your bet.
Your options: Cho (even) / Han (odd)

Please enter your bet: Han

Rolling the dice... 🎲
Dice 1: 2
Dice 2: 3
Sum: 5 (Odd)

Oops! You lose. The result was Han. Try again!
   ```
## Customize Your Game
You can tweak the game’s behavior by changing a few parameters in the code. For instance, you can modify the number of rounds or implement scoring features for a more competitive experience.

   ```python
game = Game(rounds=10)  # Set the game to play 10 rounds
   ```
## Testing

Want to ensure everything's working smoothly? Run the tests to verify that the dice rolls and betting system are functioning correctly.

Simply use pytest:
   ```bash
   pytest tests/
   ```

## License
See the [LICENSE](LICENSE) file for details.
