# 5 Puzzle Game

**Author**: Al Sweigart (al@inventwithpython.com)


The "15 Puzzle" (also known as the "Sliding Puzzle" or "Fifteen Puzzle") is a classic sliding puzzle where the goal is to arrange numbered tiles from 1 to 15 in a 4x4 grid by moving them into an empty space. The game ends when all the numbers are in the correct order.

## Description
The game starts with a random arrangement of the tiles on the grid. The objective is to move the tiles, one at a time, into the empty space, so that the numbers are in ascending order, from 1 to 15, and the empty space is in the bottom right corner.

### Game Rules:

- You can only move tiles that are adjacent to the empty space.
- The empty space allows you to slide tiles up, down, left, or right.
- The game ends when the numbers are arranged in the correct order.

## How to Start
1. Download or clone the repository.
2. Ensure that you have Python 3.x installed.
3. Run the game by executing the following command in the terminal:
```bash

python main.py
```
## Features
- Simple text-based or graphical representation of the board.
- Ability to move tiles using keyboard arrows or other keys.
- The game ends when the numbers are in the correct order.
- You can modify the difficulty by changing the initial arrangement of the tiles or using different solving algorithms

## Example
```plaintext
Initial layout of the tiles:

1  2  3  4
5  6  7  8
9  10 11 12
13 14 15  

Use the arrow keys to move the tiles.
```
## Implementation
The main components of the game include:

- 4x4 grid, represented as a 2D array.
- Tile movement algorithm, which moves tiles into the empty space while ensuring only adjacent tiles can be moved.
- Winning check, to verify if the tiles are in the correct order.

Notes
- The game can be implemented with a text-based interface or a graphical interface using libraries like pygame or tkinter.
- It's important to control the number of moves and shuffle the board correctly to ensure the puzzle is solvable.

## License
See the [LICENSE](LICENSE) file for details.
