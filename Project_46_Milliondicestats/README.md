# Dice Rolling Simulation
**Author**: Al Sweigart (al@inventwithpython.com)

## Description

This project simulates the rolling of dice a million times and analyzes the statistical outcomes. It collects data on how frequently each number (from 1 to 6) appears on a standard 6-sided die, calculates probabilities, and visualizes the results.

## Requirements

To run this project, you will need to install the following dependencies:

- Python 3.x
- Matplotlib (for visualizing the results)

You can install the dependencies by running:

```bash
pip install -r requirements-dev.txt
```

## Simulation Details
- Dice Rolls: The simulation rolls a standard 6-sided die a million times.
- Output: The results of the simulation are presented in both numerical form (frequency of each die face) and a visual histogram (probability distribution).
- Statistical Analysis: The program calculates the expected probabilities for each number (1 to 6) and compares them to the actual frequencies obtained from the simulation.

## Expected Results
- Theoretical Probability: Each face of a fair 6-sided die should have a 1/6 probability (approximately 16.67%).
- Simulation Results: After a million rolls, the frequency distribution should be close to the theoretical probability, though some slight variations may occur due to randomness.

## License
See the [LICENSE](LICENSE) file for details.
