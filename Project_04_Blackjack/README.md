# Blackjack Game
**Author**: Al Sweigart (al@inventwithpython.com)

This project is a simple implementation of the Blackjack card game in Python, with added test capabilities.

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Examples](#examples)
- [Testing](#testing)
- [License](#license)

## Overview
Blackjack, also known as 21, is a card game where the goal is to get as close to 21 as possible without going over. This project simulates a simple version of Blackjack, with classic rules and basic gameplay.

![DVD Logo Bouncing Example](https://media.istockphoto.com/id/1320296956/ru/%D0%B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F/%D0%BB%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF-%D0%B1%D0%BB%D1%8D%D0%BA%D0%B4%D0%B6%D0%B5%D0%BA-%D1%81-%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%BE%D0%B9-%D0%BB%D0%B5%D0%BD%D1%82%D0%BE%D0%B9-%D0%B8-%D0%BD%D0%B0-%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%BE%D0%BC-%D1%84%D0%BE%D0%BD%D0%B5-%D0%B8%D0%B7%D0%BE%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F-%D0%B8%D0%B3%D1%80%D0%B0-%D0%BA%D0%B0%D0%B7%D0%B8%D0%BD%D0%BE.jpg?s=1024x1024&w=is&k=20&c=UOQGxrczbnnVJdMPwEN-uMDrP0Xk7BkbsZ6ZxmiXs5U=)

## How It Works
In this game, a player competes against the dealer. Both start with two cards, and the player can choose to "hit" (take another card) or "stand" (keep their current hand). If a hand's total exceeds 21, it "busts" and loses.

Key functions include:
- Dealing cards to both the player and the dealer.
- Calculating the score of each hand.
- Determining the winner at the end of each round.

## Examples
During the game, you will be prompted to "hit" or "stand." After the round ends, the program will display the game result: whether the player wins, the dealer wins, or there is a tie.

## Testing
The project includes a suite of tests to verify various aspects of the game. The tests folder contains test modules to ensure correct functionality.

## Running Tests
1. Make sure you are in the project root directory.
2. Run all tests with the following command:

   ```bash
   pytest tests/

## License
See the [LICENSE](LICENSE) file for details.
