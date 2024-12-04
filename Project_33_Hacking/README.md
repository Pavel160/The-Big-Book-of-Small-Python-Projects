# README for Hacking Minigame

**Author**: Al Sweigart (al@inventwithpython.com)

Hacking Minigame
A mini-game inspired by "Fallout 3" where players guess the secret password using clues from their previous guesses.

## Overview
This project recreates the classic hacking mini-game from "Fallout 3". The player must find the correct password hidden in "computer memory" by analyzing clues about how many letters match between their guesses and the actual password.

## How to Play
1. The game randomly selects a secret password and displays a list of potential passwords mixed into "computer memory" (decorated with random garbage characters for immersion).
2. You have 4 attempts to guess the correct password.
3. After each guess, you receive feedback on how many letters match in both position and value with the secret password.
4. Use the clues to narrow down the options and find the correct 
password before running out of attempts.

## Setup Instructions
1. Download the source code for the game.
2. Make sure to download the sevenletterwords.txt file from sevenletterwords.txt.
Save the file in the same directory as the script.
3. Run the script using Python:
```bash
python main.py
```
## Requirements
- Python 3.6 or later
- The file sevenletterwords.txt must be present in the same folder as the script.
## Features
- Randomly generates words and mixes them into a simulated computer memory display.
- Provides interactive feedback after each guess.
- Encourages logical deduction and critical thinking to crack the password.
## Future Enhancements
- Add difficulty levels with different word lengths or number of attempts.
- Implement a graphical interface for a more immersive experience.
- Add more customization options for the "computer memory" display.

## License
## License
See the [LICENSE](LICENSE) file for details.
