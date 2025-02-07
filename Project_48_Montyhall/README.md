# Monty Hall Paradox
**Author**: Al Sweigart (al@inventwithpython.com)

This project simulates the Monty Hall Paradox, a famous probability puzzle that demonstrates how switching your choice can significantly improve your chances of winning.

## Description

The Monty Hall Paradox is based on a game show scenario. A player is presented with three doors:
- Behind one door is a prize (e.g., a car).
- Behind the other two doors are non-prizes (e.g., goats).  

The player picks a door. The host, who knows what is behind each door, opens one of the remaining doors to reveal a non-prize. The player is then given the option to either **stay** with their original choice or **switch** to the other unopened door.  

Statistically, switching doors increases the chance of winning from 1/3 to 2/3.

## Features

- Simulates multiple rounds of the Monty Hall game to demonstrate the probabilities.
- Allows the user to configure the number of simulations.
- Outputs results as text, with an optional graphical representation.

## Usage

1. Run the simulation:
    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to configure the number of iterations and analyze the results.

## Requirements
   - Python 3.8 or higher
   - Standard Python libraries (random, unittest) or additional dependencies listed in requirements-dev.txt

## License
See the [LICENSE](LICENSE) file for details.
