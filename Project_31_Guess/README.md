# 📄 README: Guess the Number

**Author**: Al Sweigart (al@inventwithpython.com)

## 🎮 Project Description
"Guess the Number" is a simple and fun number-guessing game where the player attempts to guess a randomly chosen number within a specified range. With each guess, the game provides feedback indicating whether the guess was too high, too low, or correct.

## 🚀 How to Run the Project
1. Install Python
Ensure you have Python 3.7 or newer installed on your machine.

## 🖥️ How the Game Works
1. Random Number Generation
At the start of the game, a random number is chosen within a specified range (e.g., 1 to 100).

2. Player Input
The player enters their guess for the number.

3. Feedback

- If the guess is too high, the game responds with "Too high!"
- If the guess is too low, the game responds with "Too low!"
- If the guess is correct, the game congratulates the player and ends the session.

4. Attempts
Players have a limited or unlimited number of attempts, depending on the game mode.

## ⚙️ Configurable Settings
- Range of Numbers
Change the range of numbers by modifying constants in the code (e.g., 1–100, 1–1000).

- Maximum Attempts
Enable or disable a limit on the number of guesses.

- Difficulty Levels
Add or modify difficulty levels to customize the range and number of attempts.

## 🧩 Possible Enhancements
1. Add multiple difficulty levels with varying ranges and attempts.
2. Include a scoreboard to track the best performance.
3. Add a multiplayer mode where two or more players take turns guessing.
4. Create a graphical version using a library like tkinter or pygame.

## 📸 Example Gameplay
```mathematica

Welcome to Guess the Number!
I am thinking of a number between 1 and 100.
You have 10 attempts to guess it.

Enter your guess: 50
Too low!

Enter your guess: 75
Too high!

Enter your guess: 62
Yay! You guessed the number in 3 attempts.
```
## 📝 License
See the [LICENSE](LICENSE) file for details.
