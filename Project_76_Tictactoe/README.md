# Tic-Tac-Toe
**Author**: Al Sweigart (al@inventwithpython.com)

![Tic-Tac-Toe](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTkb_woUCzB7qe14EvBXCkoqppO60xc_4Gmg&s)

## Description
Tic-Tac-Toe (or "Noughts and Crosses") is a classic two-player game where the goal is to get three of your symbols in a row (horizontally, vertically, or diagonally) on a 3x3 grid. This Python implementation offers a simple console-based version of the game.

## Game Features

1. A 3x3 grid is displayed.
2. Two players take turns to place their symbols (X or O) on the grid.
3. The game checks for a winner or a draw after each move.
4. Offers the option to play again after the game ends.

## Requirements

Python 3.7 or higher.

## How to Play

1. Run the game:
```bash

python main.py
```
2. Follow the console instructions:
   - Players will be prompted to enter their moves by specifying the numbers (1-9)

3. The game will display the updated grid after each move.
A player wins by placing three of their symbols in a row (horizontally, vertically, or diagonally). If the grid is full and no player has won, the game ends in a draw.
After the game ends, players can choose to start a new game or exit.

## Example Gameplay

```sql

Welcome to Tic-Tac-Toe!


       | |   1 2 3
      -+-+-
       | |   4 5 6
      -+-+-
       | |   7 8 9
What is X's move? (1-9)
> 5

       | |   1 2 3
      -+-+-
       |X|   4 5 6
      -+-+-
       | |   7 8 9
```

## License
See the [LICENSE](LICENSE) file for details.
