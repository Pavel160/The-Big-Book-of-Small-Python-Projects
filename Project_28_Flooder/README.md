# Flooder
**Author**: Al Sweigart (al@inventwithpython.com)

Flooder is a vibrant board game where the goal is to fill the entire board with a single color or shape. Inspired by the game Flood It!, it also includes a mode for colorblind players, making it accessible to a broader audience.

## 🎮 How to Play
1. Objective:
Your task is to make the entire board one color or shape within a limited number of moves.

2. Game Modes:

Color Mode: Play with bright colors like red, green, blue, etc.
Shape Mode: Symbols like ♥, ♦, ▲ replace colors for better accessibility.

3. Rules:

Start from the top-left corner.
On each turn, select a color or shape to flood the adjacent tiles.
Your selection changes the connected tiles to the new color/shape.
Continue until the board is uniform or you run out of moves.

4. Winning Condition:

You win by filling the board with one color/shape before running out of moves.

## ⚙️ Game Features
- Custom Board Sizes: Change board dimensions in the code to make the game easier or harder.
- Accessibility: A colorblind-friendly mode replaces colors with distinct shapes.
- Challenge Options: Modify the number of moves allowed for added difficulty.

## 🖥️ System Requirements
1. Python 3.x or later.

2. Install the bext module:
```bash
pip install bext
```


## ▶️ How to Run
1. Open your terminal.
2. Navigate to the folder containing flooder.py.
3. Run the game with:
```bash
python main.py
```

## 🛠️ Customization Options
You can adjust the game settings by editing constants in the code:

- BOARD_WIDTH and BOARD_HEIGHT control the board size.
- MOVES_PER_GAME sets the maximum number of moves.
- Edit SHAPES_MAP to replace shapes in the Shape Mode.

## License
See the [LICENSE](LICENSE) file for details.


