# Langton's Ant

**Author**: Al Sweigart (al@inventwithpython.com)

Langton's Ant is a simulation of an artificial life algorithm, named after its inventor Chris Langton. The algorithm is simple yet produces complex behavior from simple rules. In the simulation, an ant moves on a 2D grid of cells, flipping the color of each cell it visits. Based on the cell's color, the ant will either turn left or right, creating a fascinating emergent pattern.

![Cartoon Ant](https://img.freepik.com/premium-vector/cartoon-ant-posing_29190-2107.jpg?uid=R173748318&ga=GA1.1.827076773.1731492049&semt=ais_hybrid)

## Features
- Simple grid-based simulation.
- Ant follows the Langton's Ant algorithm.
- Customizable grid size and iteration count.
- Visual representation of the ant’s path and movement.

## Requirements
- Python 3.x
- Pygame library for rendering (optional for graphical interface)
- If you want to run the graphical version, install pygame:

   ```bash

   pip install pygame
   ```
## Usage
### Run the Simulation
Run the program using the following command:

   ```bash

   python main.py
   ```
By default, the simulation will run with the grid size of 101x101 and iterate 11000 times. You can adjust these parameters in the code or pass them as arguments.

## Command-line Arguments
You can modify the default grid size and number of iterations via command-line arguments:

  ```bash

python langtons_ant.py --grid-size 101 --iterations 11000
   ```
Where --grid-size defines the grid dimensions, and --iterations defines how many steps the ant will take.

## How It Works
Langton's Ant operates on a grid of cells that are either "white" or "black". The ant starts at the center of the grid, facing a direction (typically right). It follows these rules:

1.  If the ant is on a white cell, it turns 90° clockwise, flips the color of the cell to black, and moves forward.
2.  If the ant is on a black cell, it turns 90° counterclockwise, flips the color of the cell to white, and moves forward.
The result is a chaotic but fascinating pattern that eventually stabilizes into a repeating loop.

### Example

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request with your changes.

## License
See the [LICENSE](LICENSE) file for details.


