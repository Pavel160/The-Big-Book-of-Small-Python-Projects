# Ninety-Nine Bottles of Milk on the Wall
**Author**: Al Sweigart (al@inventwithpython.com)

This project prints the full lyrics to the song *"Ninety-Nine Bottles of Milk on the Wall"*. It's a playful program that demonstrates basic Python programming concepts such as loops, conditionals, and user interruption handling.

## Description

The program starts with 99 bottles of milk and counts down as the lyrics progress. The song continues until no more bottles are left on the wall. Users can control the speed of the lyrics and stop the program at any time by pressing `Ctrl-C`.

## Features

- Dynamically generates the lyrics for the song.
- Adjustable pause duration between lines for custom playback speed.
- Handles user interruption (e.g., pressing `Ctrl-C` to quit).

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Sit back and watch the lyrics scroll on your screen.  
   Press `Ctrl-C` at any time to exit

## Requirements
   - Python 3.8 or higher
   - Standard Python libraries (time, sys)

## Customization

- You can adjust the playback speed by modifying the `PAUSE` variable in the code.  
  For example:
  ```python
  PAUSE = 2  # Seconds between lines (default: 2 seconds)

## License
See the [LICENSE](LICENSE) file for details.
