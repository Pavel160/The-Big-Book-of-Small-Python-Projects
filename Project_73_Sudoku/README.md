# Sudoku Game
**Author**: Al Sweigart (al@inventwithpython.com)

This is a console-based implementation of the popular Sudoku game in Python.

## Description

Sudoku is a logic puzzle where the goal is to fill a 9x9 grid with numbers from 1 to 9 such that:
- Each row contains numbers from 1 to 9 without repetition.
- Each column contains numbers from 1 to 9 without repetition.
- Each of the 3x3 subgrids contains numbers from 1 to 9 without repetition.
- Make sure the sudokupuzzles.txt file with puzzles is in the root directory.

## How to Play
1. Run the game:

```bash
python main.py
```
2. Follow the on-screen instructions. You can use the following commands:

- RESET — reset the current puzzle to its original state.
- NEW — load a new random puzzle.
- UNDO — undo the last move.
- ORIGINAL — display the original puzzle.
- QUIT — quit the game.
- Input moves in the format <letter><number> <digit>.

For example: A1 5 means "place the number 5 in cell A1."

## Project Files
- main.py — the entry point of the game.
- sudoku.py — contains the game logic and the SudokuGrid class.
- sudokupuzzles.txt — a text file containing pre-made puzzles.

## Example
### Initial Grid
```diff

5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```
### Solved Grid
```diff

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```
## License
See the [LICENSE](LICENSE) file for details.
