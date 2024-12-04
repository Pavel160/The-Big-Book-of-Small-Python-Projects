# Deep Cave
Author: Al Sweigart

Description: An animation of an endlessly deep cave that seems to stretch infinitely into the earth. The program dynamically generates a tunnel whose width and position change randomly with each update.

## 🔍 Features
Real-time animation: The program creates a dynamic tunnel, giving the illusion of infinite depth.
Realistic behavior: The left walls and the tunnel gap adjust randomly, simulating natural cave bends.
Customizable settings: The tunnel width and animation speed can be easily adjusted.

## 🚀 How to Run the Program
### Requirements
- Python 3.x or higher
- Operating System: Windows, macOS, or Linux

## ⚙️ Settings
At the start of the file, you can customize the following constants:

- WIDTH: Sets the width of the tunnel (default is 70). Try lowering it to 30 or increasing it for experiments.
- PAUSE_AMOUNT: Controls the animation speed (default is 0.05). Decrease it to 0 for instant updates or increase it to 1.0 for a slower pace.

## 🔧 How It Works
1. Initialization: The program initializes the starting width of the left wall (leftWidth) and the gap (gapWidth).
2. Tunnel Display: Inside an infinite loop, the program prints rows of # (walls) and spaces (the tunnel gap).
3. Random Adjustments: The left wall and gap widths are adjusted randomly based on dice rolls.
4. Exit: Press Ctrl+C at any time to stop the program.

## 🧪 Experiment Ideas
- Change Tunnel Width: Modify WIDTH to make the tunnel narrower (e.g., 30) or wider (e.g., 100).
- Dynamic Gap Behavior: Uncomment the code that adjusts the gapWidth to make the gap dynamic.
- Pause Duration: Set PAUSE_AMOUNT to 0 for instant updates or to 1.0 for a more deliberate animation pace.

## License
See the [LICENSE](LICENSE) file for details.
