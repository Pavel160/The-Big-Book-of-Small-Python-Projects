# Lucky Stars 🎲✨  
**Author**: Al Sweigart (al@inventwithpython.com)


A "press your luck" game inspired by *Zombie Dice* from Steve Jackson Games. Roll dice to gather as many stars as possible, but beware: if you roll three skulls, you lose all your stars for that turn!  

This program was created by **Al Sweigart** and is available as part of *The Big Book of Small Python Projects*.  

---

## How to Play  
- Each player takes turns rolling dice to collect stars 🌟.  
- On your turn:  
  1. You draw **3 random dice** (Gold, Silver, or Bronze) from the dice cup.  
  2. Roll the dice to reveal **Stars**, **Skulls**, or **Question Marks**.  
  3. Decide if you want to roll again or keep your stars for points.  
- **Be careful!** If you roll **3 or more Skulls ☠️**, you lose all your stars for that turn.  
- Gold dice are more likely to roll Stars, while Bronze dice have more Skulls.  

---

## Rules  
- Stars add to your score for the turn.  
- Question Marks let you roll again, keeping their dice for the next roll.  
- Skulls do not reset between rolls, so the risk of losing increases.  
- Once a player scores **13 points**, the game enters the final round, where each other player gets one last turn.  
- The player with the highest score at the end wins!  

---

## Setup and Requirements  

### Prerequisites  
- **Python 3.6+** installed on your system.  
- Basic understanding of how to run Python scripts.  

### Installation  
1. Clone or download the script from this repository.  
2. Navigate to the folder containing the script.  

### Running the Game  
Run the game with:  

```bash
python main.py
```

## Example Output
```vbnet
Lucky Stars 🎲✨  

A "press your luck" game where you roll dice to gather Stars, avoid Skulls, and keep Question Marks!  

How many players are there?  
> 2  

What is player #1's name?  
> Alice  

What is player #2's name?  
> Bob  

SCORES: Alice = 0, Bob = 0  

It is Alice's turn.  
Rolling the dice...  
+-----------+ +-----------+ +-----------+  
|     .     | |    ___    | |           |  
|    ,O,    | |   /   \   | |           |  
| 'ooOOOoo' | |  |() ()|  | |     ?     |  
|   `OOO`   | |   \ ^ /   | |           |  
|   O' 'O   | |    VVV    | |           |  
+-----------+ +-----------+ +-----------+  
GOLD         SILVER        BRONZE  

Stars collected: 1   Skulls collected: 1  

Do you want to roll again? (Y/N)
```

## Game Mechanics
The game uses 13 dice:

- 6 Gold Dice (3 Stars, 2 Question Marks, 1 Skull)
- 4 Silver Dice (2 Stars, 2 Question Marks, 2 Skulls)
- 3 Bronze Dice (1 Star, 2 Question Marks, 3 Skulls)

Each roll has a random outcome based on the dice's probabilities.

## Customization
Feel free to modify the game:

- Change the number of dice or their composition in the cup variable.
- Adjust the point limit to win by editing the if playerScores[playerNames[turn]] >= 13 condition.
- Customize the dice faces by modifying the STAR_FACE, SKULL_FACE, and QUESTION_FACE lists.

## License
See the [LICENSE](LICENSE) file for details.
