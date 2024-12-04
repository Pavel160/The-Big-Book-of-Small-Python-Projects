# 📄 README: Forest Fire Simulation
**Author**: Al Sweigart (al@inventwithpython.com)

## 🔥 Project Description
This project simulates the spread of a forest fire using a 2D grid. The forest is represented as a grid of cells, each of which can either be a tree, on fire, or empty space. The fire spreads to neighboring cells with a given probability. The goal is to observe how the fire consumes the forest and experiment with parameters that influence its behavior.

## 🚀 How to Run the Project
1. Install Python

Make sure Python 3.7 or higher is installed on your system.

## 🖥️ How the Model Works
1. The forest is created randomly:
Each cell in the grid can either be a tree or empty space based on the given density (INITIAL_TREE_DENSITY).

2. The fire is initiated:
A random tree is struck by lightning and starts to burn.

3. Fire Spread:
On each step, the fire may spread to neighboring trees with a probability (FIRE_CHANCE).

4. Stopping the simulation:
The simulation ends when no trees are left burning.

## ⚙️ Model Parameters
- Forest Size:
Adjust the WIDTH and HEIGHT constants to change the size of the grid.

- Tree Density:
The initial density of trees in the forest is controlled by the INITIAL_TREE_DENSITY parameter (range from 0.0 to 1.0).

- Tree Growth:
The chance for an empty space to grow into a tree is controlled by the GROW_CHANCE parameter.

- Fire Ignition:
The probability that a tree is struck by lightning and catches fire is controlled by the FIRE_CHANCE parameter.

- Pause Length:
Controls the speed of simulation. A value of PAUSE_LENGTH between 0.0 and 1.0. Setting it to 0.0 will make the simulation run faster, and 1.0 will slow it down.

## 🛠️ Possible Improvements
1. Add wind and humidity effects on the fire's behavior.
2. Implement a graphical visualization using libraries like pygame or matplotlib.
3. Add fire fighting intervention or controlled burns.
4. Create an animation of the fire spread in GIF format.

## 📸 Example Output
```
🌲🌲🌲🌲🔥🌲🌲
🌲🔥🔥🔥🔥🔥🌲
🌲🌲🌲🔥🌲🌲🌲
🌲🔥🔥🔥🔥🌲🌲
🌲🌲🌲🌲🌲🌲🌲
```

## 📝 License
See the [LICENSE](LICENSE) file for details.
