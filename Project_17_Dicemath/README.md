# Arithmetic with Dice
**Author**: Al Sweigart (al@inventwithpython.com)

## Description
"Arithmetic with Dice" is a fun and educational game where players roll dice and solve arithmetic problems based on the results. It’s a great way to practice math skills while enjoying the randomness of dice rolls. The game supports multiple levels of difficulty and can be played solo or with friends.

## Features

- Roll dice to generate random numbers.
- Solve addition, subtraction, multiplication, or division problems using the dice results.
- Choose difficulty levels:
  - Easy: Single-digit operations.
  - Medium: Two-digit operations.
  - Hard: Mixed operations and larger numbers.
- Score tracking to challenge yourself or compete with others.

## How to Play

1. **Start the Game**: Run the program and select a difficulty level.
2. **Roll the Dice**: The game will simulate rolling one or more dice.
3. **Solve Problems**: Based on the dice rolls, solve the presented arithmetic problem.
4. **Earn Points**: Gain points for correct answers. The faster you solve, the more points you earn!
5. **Goal**: Achieve the highest score or beat your personal best.

## Requirements
- Python 3.7+
- Libraries listed in requirements-dev.txt

## Project Structure
- main.py — The main file to start the game.
- dicemath.py — Contains all game logic, including dice rolls, arithmetic operations, and scoring.
- config.py — Configuration settings, such as dice types, difficulty levels, and score multipliers.
- README.md — Project instructions and details.

## Example Output
Here’s an example of gameplay:
   ```yaml
Rolling the dice... 🎲 🎲
You rolled: 4 and 5
Solve: 4 + 5 = ?
Your answer: 9
Correct! You earned 10 points.
   ```

## License
See the [LICENSE](LICENSE) file for details.
