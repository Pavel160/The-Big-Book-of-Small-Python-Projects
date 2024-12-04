# Collatz Hypothesis Game
**Author**: Al Sweigart (al@inventwithpython.com)

## Description

The "Collatz Hypothesis Game" is an interactive program based on the famous Collatz Conjecture. The player inputs a number, and the program generates the sequence of steps defined by the conjecture until it reaches 1. 

The goal is to help players understand how the conjecture works and explore sequences for different starting numbers.

---

## Collatz Conjecture Rules

1. Start with any positive integer `n`.
2. If the number is even, divide it by 2:  
   `n → n / 2`
3. If the number is odd, multiply it by 3 and add 1:  
   `n → 3 * n + 1`
4. Repeat the process until `n` equals 1.

---

## Features

- Accepts a starting number from the user.
- Displays the sequence of steps leading to 1.
- Shows the total number of steps.
- (Optional) Visualizes the sequence as a graph.

## Usage

1. Ensure Python (version 3.x or higher) is installed.

## Running Tests
1. Make sure you are in the project root directory.
2. Run all tests with the following command:

   ```bash
   pytest tests/

## License
See the [LICENSE](LICENSE) file for details.
