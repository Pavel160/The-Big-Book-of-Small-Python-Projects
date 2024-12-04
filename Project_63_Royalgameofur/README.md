# Royal Game of Ur

**Author**: Al Sweigart (al@inventwithpython.com)

The Royal Game of Ur is one of the oldest known board games in history. Originating in Mesopotamia around 2600 BCE, it is a predecessor to many modern board games. This project offers a digital version of the game, allowing two players to compete using pawns, dice, and a game board.

## Features
- Two-player gameplay: Race to get all your pawns off the board before your opponent.
- Randomized dice rolls: Each turn's moves are determined by virtual dice rolls.
- Traditional rules: Mechanics include pawn movement, capturing opponent pieces, and safe spots.
- Optional animations: Visual representation of dice rolls and pawn movements.

## How to Play
1. ### Game Setup:

   - Each player starts with 7 pawns.
   - The goal is to move all your pawns across the board and off the end.

2. ### Dice Rolls:

   - Players roll four pyramid-shaped dice (with outcomes ranging from 0 to 4).
   - The roll determines how many spaces a pawn can move.

3. ### Pawn Movement:

- Choose one of your pawns and move it by the number rolled.
- If your pawn lands on an opponent’s pawn, the opponent’s pawn is sent back to the start.
- Certain spaces protect pawns from being captured.

4. ### Winning the Game:

   - The first player to move all their pawns across the board and off the final space wins.

## Technical Details
- Language: Python 3.x
- Libraries:
  - random for simulating dice rolls.
  - pygame (optional) for graphical visuals.
- Game Board: Represented as a 20-space grid.

## Planned Features
- Add AI to play against the computer.
- Implement online multiplayer mode.
- Improve board visuals and animations.
## Acknowledgments
- The game is based on archaeological discoveries of boards and pieces from Mesopotamia.
- Rules were reconstructed using the research of Irving Finkel, a historian of ancient games.

## License
See the [LICENSE](LICENSE) file for details.
