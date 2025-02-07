# Three-Card Monte
**Author**: Al Sweigart (al@inventwithpython.com)

## Description
Three-Card Monte is a classic street game where the player must guess the location of a winning card after they are shuffled. This Python implementation simulates the game, providing an interactive experience for players to test their luck or skill.

## Game Features

1. Three cards are generated: one winning card ("Q" for Queen) and two losing cards ("X").
2. The cards are shuffled randomly.
3. The player is prompted to choose a card by its position.
4. The game checks the result:
   - If the player selects the winning card, they win.
   - Otherwise, they lose, and the correct card position is revealed.
5. Players are given the option to play again.

## Requirements
- Python 3.7 or higher.
- No external dependencies (only Python's built-in libraries are used).

## How to Play

1. Run the game:
```bash

python main.py
```
2. Follow the console instructions:
   - Watch the initial card setup.
   - Enter the corresponding to the card position (LEFT MIDDLE RIGHT).
3. Check the result: see if you correctly guessed the Queen's position.
4. Decide if you want to play again.

## License
See the [LICENSE](LICENSE) file for details.
