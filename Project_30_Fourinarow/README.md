# 📄 README: Connect Four
**Author**: Al Sweigart (al@inventwithpython.com)

## 🎮 Project Description
"Connect Four" is a classic two-player board game where the objective is to line up four of your pieces in a row—horizontally, vertically, or diagonally—before your opponent does. The game is played on a grid, with each player taking turns dropping their pieces into columns. The winner is the first player to line up four pieces in a row.

## 🚀 How to Run the Project
1. Install Python

Make sure you have Python 3.7 or newer installed on your computer.

## 🖥️ How the Game Works
1. Game Board
The game is played on a 7x6 grid, where players take turns dropping their pieces into columns. The pieces fall to the lowest available row in that column.

2. Objective
Players aim to line up four of their pieces in a row—either horizontally, vertically, or diagonally. The first player to achieve this wins.

2. Game Continuation
The game continues until one player lines up four pieces in a row or the board is completely filled, resulting in a draw.


## ⚙️ Game Parameters
- Game Board:
The default game board is 7 columns by 6 rows. The number of rows and columns can be adjusted in the settings.

- Players:
The game is designed for two players, who take turns. Each player uses a different symbol (e.g., "X" and "O").

- Winning:
The first player to line up four pieces in a row—either horizontally, vertically, or diagonally—wins.

- Draw:
If the board is filled and no player has lined up four pieces, the game results in a draw.

## 🧩 Possible Enhancements
1. Add a graphical user interface using the pygame library.
2. Implement a single-player mode against a computer opponent with AI.
3. Add a difficulty setting for the AI.
4. Implement save and load game functionality.

## 📸 Example Game Board
```mathematica

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   | X |   |   |   |
|   |   | O | X | O |   |   |
|   |   | O | X | O | O |   |
| O | O | X | X | O | O |   |
```

## 📝 License
See the [LICENSE](LICENSE) file for details.

