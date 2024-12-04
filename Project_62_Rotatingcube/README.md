# Rotating Cube Animation
**Author**: Al Sweigart (al@inventwithpython.com)

This program displays a 3D rotating cube in your terminal/command prompt. The cube rotates along all three axes (X, Y, Z) at different speeds, creating a dynamic and mesmerizing effect.

Tags: 3D, animation, math, graphics, terminal, rotating cube

## Description
This program creates a rotating 3D cube that is drawn using ASCII characters in the terminal. The cube continuously rotates along the X, Y, and Z axes, and you can stop the animation by pressing Ctrl-C. The program works on a variety of systems, including macOS, Linux, and Windows (using the cls or clear command to clear the screen).

## How It Works
The program uses basic 3D geometry and the Bresenham line algorithm to draw the lines of the cube. It calculates the rotations for each axis and adjusts the cube's vertices accordingly. Then, it projects the 3D coordinates onto a 2D plane to display the cube in the terminal window.

### Features:
- Rotating cube animation.
- Adjustable rotation speeds for the X, Y, and Z axes.
- ASCII art display using a customizable character (solid block by default).
- The cube is displayed in a terminal/command prompt window.

## Rotation Speed:
- The rotation speed for the X, Y, and Z axes can be adjusted by modifying the X_ROTATE_SPEED, Y_ROTATE_SPEED, and Z_ROTATE_SPEED constants.

## How to Use
1. Run the program in your terminal or command prompt.

   - This program must be run in a terminal/command prompt window.
2. Start the game:
   ```bash
   python main.py

3. Exit the program by pressing Ctrl-C.

## Installation
You don't need any external libraries to run the program. It uses Python's built-in modules such as math, time, sys, and os.

## License
See the [LICENSE](LICENSE) file for details.
