# Ninety-Nine Bottles of Milk on the Wall (Silly Edition)
**Author**: Al Sweigart (al@inventwithpython.com)

This project prints the full lyrics to the song *"Ninety-Nine Bottles of Milk on the Wall"*. With each verse, the lyrics become sillier due to random modifications such as swapping letters, changing capitalization, or adding extra characters. It's a fun way to showcase basic Python programming with randomness and text manipulation.

## Features

- Dynamically generates the full lyrics for the song.
- Adds random "silly" effects to the lyrics, such as:
  - Replacing characters with spaces.
  - Changing letter case (upper/lower).
  - Swapping adjacent characters.
  - Doubling random characters.
- Supports customizable speed for text display.
- Handles user interruptions gracefully with `Ctrl-C`.

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Watch the lyrics scroll by, with each verse becoming sillier than the last!  
   Press `Ctrl-C` at any time to quit.


## Customization

- **Speed of text display:** Modify the `SPEED` constant in the code to change the delay between each character:
  ```python
  SPEED = 0.01  # Faster
  SPEED = 0.1   # Slower

- **Pause between lines:** Adjust the `LINE_PAUSE` constant for a longer or shorter pause after each line:
  ```python
  LINE_PAUSE = 1.5  # Default pause of 1.5 seconds

## Requirements
- Python 3.8 or higher

- Standard Python libraries (time, sys, random)

## License
See the [LICENSE](LICENSE) file for details.
