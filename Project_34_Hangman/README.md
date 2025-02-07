# README for Hangman Game

**Author**: Al Sweigart (al@inventwithpython.com)

About the Game
Hangman is a classic word-guessing game where the goal is to uncover a secret word by guessing one letter at a time. Each incorrect guess brings the hangman closer to completion. Can you save the day by guessing the word in time?

This version was adapted from Al Sweigart’s project in The Big Book of Small Python Projects.

## How It Works
1. The game selects a random word from a predefined category (Animals by default).
2. You guess letters to reveal the secret word.
3. Each wrong guess adds a new part to the hangman drawing.
4. You win if you uncover all the letters in the secret word before the hangman is fully drawn.
5. You lose if the hangman is completely drawn before you guess the word.
## Features
- ASCII art visuals that change with each incorrect guess.
- A predefined word list from the category Animals.
- Friendly prompts and feedback for invalid or repeated guesses.
- Clear game logic to determine wins and losses.
- Exit the game anytime with Ctrl+C.
## Setup
1. Ensure Python 3 is installed on your computer.
2. Copy the code into a file named hangman.py.
3. Open your terminal or command prompt and navigate to the file location.

## Running the Game
Run the game using the following command:

```bash

python main.py
```
## Game Controls
- Input a single letter for each guess.
- The game will notify you if:
  - You’ve guessed the letter before.
  - Your input is invalid (not a letter or more than one character).
## Modifications You Can Try
1. Change the Word List:

   - Modify the WORDS variable to include custom words.
Example:
```python

WORDS = 'APPLE BANANA CHERRY GRAPE MANGO'.split()
```
2. Customize the Hangman ASCII Art:

   - Replace the drawings in the HANGMAN_PICS variable to create a unique theme (e.g., a guillotine or a rocket).

3. Change the Category:

   - Update the CATEGORY variable to reflect your custom word list.

## Example Gameplay
```kotlin

Hangman, by Al Sweigart al@inventwithpython.com

 +--+
 |  |
    |
    |
    |
    |
=====
The category is: Animals

Guess a letter.
> E
```
## License
See the [LICENSE](LICENSE) file for details.
