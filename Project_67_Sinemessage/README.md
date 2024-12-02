# Sine Message

**Author**: Al Sweigart (al@inventwithpython.com)

This program displays a message in a sinusoidal wave pattern on the terminal. It uses the sine function to create a "wave-like" effect for the message, making it appear to oscillate from left to right across the screen.

You can customize the message to display, and the program will continuously animate the message in a sinusoidal pattern until interrupted.

## Features:
- Displays any custom message with a sinusoidal wave effect.
- Works in the terminal or command prompt.
- Press Ctrl-C to quit the program.

## Requirements:
- Python 3.x
- No additional libraries required other than the Python standard library.

## How It Works:
1. The program asks you to enter a message.
2. It calculates the required width of the terminal and adjusts the message to fit within the terminal.
3. The message is displayed in a sinusoidal pattern, moving from left to right in a wave.
4. The program continuously animates the message until you press Ctrl-C to stop it.

## Usage:
1. Run the Python script.
2. Enter your desired message when prompted.
3. Watch as the message appears to wave across the screen.
4. To stop the animation, press Ctrl-C.

## Example:
```sh
Sine Message, by Al Sweigart al@inventwithpython.com
(Press Ctrl-C to quit.)

What message do you want to display? (Max 40 chars.)
> Hello, world!
     Hello, world!
        Hello, world!
            Hello, world!
       Hello, world!
  Hello, world!
```
## Code Explanation:
- The program uses the sine function (math.sin) to create the wave effect.
- The message is dynamically padded with spaces depending on the current sine value.
- The program continuously updates the wave pattern with a small delay (time.sleep(0.1)), giving the effect of movement.

## License
See the [LICENSE](LICENSE) file for details.
