# Mancala Game
**Author**: Al Sweigart (al@inventwithpython.com)

The Mancala Game is a two-player strategy board game that is simple to learn yet offers deep strategic opportunities. This project implements the Mancala game in Python, allowing players to enjoy this classic directly in the terminal.

## Features
- Two-player mode: Play with a friend on the same device.
- Customizable pits: Easily modify the number of pits or stones in each pit.
- Turn mechanics: Includes standard Mancala rules such as "free turn" and "capture".
- Dynamic board display: Updates and displays the board after every move.

## How to Play
1. Objective: Collect the most stones in your store (Mancala) by the end of the game.
2. Setup:
   - Each player has a row of pits and a store.
   - Stones are distributed evenly in the pits.
3. Rules:
   - Players take turns picking stones from one of their pits.
   - Stones are distributed one by one into subsequent pits, including their store but skipping the opponent’s store.
   - If the last stone lands in an empty pit on the player's side, they capture all stones in the opposite pit along with the last stone.
   - If the last stone lands in the player’s store, they get a free turn.

4. Endgame:
   - The game ends when one side's pits are empty.
   - Remaining stones on the board are collected by the respective players.
   - The player with the most stones in their store wins.

## Project Structure
   - mancala.py: Contains the game logic and board setup.
   - main.py: Runs the game and manages player interaction.
   - config.py (optional): Stores customizable parameters like the number of pits or initial stones.

## Example Gameplay
```rust
Player 1's Store:  4 | 4 | 4 | 4 | 4 | 4 |   Store: 0
Player 2's Store:  4 | 4 | 4 | 4 | 4 | 4 |   Store: 0

Player 1, choose a pit (1-6): 3

Player 1's Store:  4 | 4 | 0 | 5 | 5 | 5 |   Store: 1
Player 2's Store:  5 | 5 | 5 | 4 | 4 | 4 |   Store: 0
```

## Customization
You can modify the game settings by adjusting the following parameters in config.py:

   - Number of pits: Default is 6 per player.
   - Initial stones per pit: Default is 4.
   - Custom board size: Easily adapt the game for larger or smaller boards.

## Future Enhancements
   - Add AI for single-player mode.
   - Online multiplayer support.
   - GUI version for a more interactive experience.

## License
See the [LICENSE](LICENSE) file for details.
