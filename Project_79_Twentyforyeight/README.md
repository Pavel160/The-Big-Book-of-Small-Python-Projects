# 2048 Game
**Author**: Al Sweigart (al@inventwithpython.com)

## Description
"2048" is a popular sliding tile puzzle game where the objective is to combine tiles with the same number to reach the number 2048. This Python implementation replicates the original game, allowing players to enjoy it via the console.

## Game Features

1. A 4x4 grid where tiles can slide up, down, left, or right.
2. Random tiles with a value of 2 (or occasionally 4) appear after each move.
3. Tiles with the same number merge when they collide during a move.
4. The game ends when no more moves are possible or the player reaches 2048.
5. Displays the player's score and the option to restart after losing or winning.

## Requirements

Python 3.7 or higher.

## How to Play

1. Run the game:
```bash

python main.py
```
2. Use the arrow keys to move tiles:
- W: Up
- A: Left
- S: Down
- D: Right

3. Tiles with the same number merge when moved into one another.
4. The game ends when the grid is full and no moves are possible or when the player reaches 2048.
5. Restart or exit after the game ends.

## Example Gameplay

```diff

Score: 8
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+
|    |   2|    |    |
+----+----+----+----+
|    |   4|    |    |
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+

Enter move (W/A/S/D): W
```

## License
See the [LICENSE](LICENSE) file for details.
