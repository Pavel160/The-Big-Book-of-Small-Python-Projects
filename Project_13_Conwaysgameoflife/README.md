# Conway's "Game of Life"
**Author**: Al Sweigart (al@inventwithpython.com)

## Description

Conway's "Game of Life" is a cellular automaton devised by mathematician John Conway. It's a zero-player game, where the evolution is determined by its initial state and simple rules. Users set the starting conditions, and the program simulates how the "game" progresses over time.

---

## Rules

1. **Grid and Cells**:  
   - The game is played on a two-dimensional grid of cells.
   - Each cell can be either *alive* (1) or *dead* (0).

2. **Evolution Rules**:
   - A live cell with 2 or 3 live neighbors survives to the next generation.
   - A live cell with fewer than 2 live neighbors dies (underpopulation).
   - A live cell with more than 3 live neighbors dies (overpopulation).
   - A dead cell with exactly 3 live neighbors becomes alive (reproduction).

3. The game evolves generation by generation based on the above rules.

---

## Features

- Allows users to input custom initial states.
- Supports predefined patterns like "Glider," "Pulsar," and "Spaceships."
- Visualizes the grid as it evolves over time.
- (Optional) Exports the grid to a file for analysis.

## License
See the [LICENSE](LICENSE) file for details.
