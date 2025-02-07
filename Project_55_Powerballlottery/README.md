# Powerball Lottery Simulator
**Author**: Al Sweigart (al@inventwithpython.com)

Powerball Lottery Simulator is a Python project that allows you to simulate drawing Powerball lottery numbers, as well as generating a set of random tickets to compare against a winning set of numbers.

Tags: lottery, simulation, random

## Features
- Simulate a Powerball Draw: Randomly generate a set of Powerball numbers and the Powerball number.
- Random Ticket Generation: Generate random lottery tickets for comparison with the winning numbers.
- Winning Ticket Check: Compare generated tickets with the winning numbers to see if they match.
- Customizable Number of Tickets: Specify how many tickets you want to generate.

## Requirements
Python 3.x

## How It Works
- Powerball Draw: A Powerball draw consists of 5 numbers from 1 to 69, and 1 Powerball number from 1 to 26.
- Ticket Generation: The program generates random tickets, each with 5 numbers from 1 to 69 and 1 Powerball number from 1 to 26.
- Winning Ticket Check: After generating the winning Powerball numbers, it compares each ticket to the winning numbers to check if they match.

## Example
### Powerball Numbers:
```yaml
Winning Numbers: 1, 17, 23, 45, 68
Powerball: 10
```
### Generated Ticket:
```yaml
Your Ticket: 1, 17, 23, 45, 68 | Powerball: 10
```
### Result:
    Congratulations! You have won the Powerball!

## Usage
1. Run the script to generate a random set of Powerball winning numbers.
2. Specify how many tickets you want to generate.
3. The program will simulate the lottery draw and compare each generated ticket with the winning numbers.

## Example of Running the Program:
```python
Enter the number of tickets to generate: 5
Generating tickets...
Ticket #1: 3, 12, 19, 25, 44 | Powerball: 17
Ticket #2: 10, 15, 23, 34, 51 | Powerball: 10
Ticket #3: 1, 17, 23, 45, 68 | Powerball: 10
...
```

## License
See the [LICENSE](LICENSE) file for details.

