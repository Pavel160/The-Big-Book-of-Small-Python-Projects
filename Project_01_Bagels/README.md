# Bagels Game 🥯
**Author**: Al Sweigart (al@inventwithpython.com)

## Project Description
"Bagels" is a number-guessing puzzle game where the player has to guess a randomly generated number. The program provides feedback on each guess with clues such as "Pico," "Fermi," or "Bagels" to guide the player toward the correct answer.

## How to Play
1. The program generates a random three-digit number with unique digits.
2. The player enters a guess.
3. The program responds with clues:
   - **Pico** — one digit is correct but in the wrong position.
   - **Fermi** — one digit is correct and in the correct position.
   - **Bagels** — no digits are correct.
4. The player continues guessing until the correct number is found.

## Technology Stack
- **Language:** Python 3.12
- **Development Environment:** PyCharm or VSCode (optional)

## Installation and Running the Game
1. Clone the repository:
   ```bash
   git clone https://github.com/Pavel160/bagels.git

2. Navigate to the project directory:
   ```bash
   cd bagels

3. Install any dependencies (if applicable):
   ```bash
   pip install -r requirements-dev.txt

4. Run the game:
   ```bash
   python main.py

## Project Structure
- `main.py` — main file to run the game.
- `bagels.py` — contains the game logic.
- `config.py` — project configuration settings.
- `tests/` — folder with tests to verify code functionality.
  - For example, `test_bagels.py` may contain tests to check clues and game logic.

## Running Tests
1. Make sure you are in the project root directory.
2. Run tests using pytest:
   ```bash 
   pytest tests/

## Example Usage
   ```yaml
Guess the number: 123
Result: Fermi Pico

Guess the number: 456
Result: Bagels
   ```

## License
See the [LICENSE](LICENSE) file for details.
