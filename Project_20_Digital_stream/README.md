# Digital Stream

**Author**: Al Sweigart (al@inventwithpython.com)

"Digital Stream" is a screensaver inspired by the visual effects from the movie "The Matrix". The program creates an animation of a stream of "0"s and "1"s that scrolls smoothly across the screen. It uses the terminal to display the animation.

![The Matrix](https://klike.net/uploads/posts/2023-02/1676529656_1.jpg)

## Features:
- Simulation of the effects seen in the movie "The Matrix".
- Customizable settings such as stream length and density.
- Works in the terminal, using standard output.
- Simple to use and configure.

## Configuration Parameters:
- MIN_STREAM_LENGTH: Minimum length of a stream (default is 6).
- MAX_STREAM_LENGTH: Maximum length of a stream (default is 14).
- PAUSE: Pause between frames (default is 0.1 seconds).
- STREAM_CHARS: List of characters used for the stream (default is ['0', '1']).
- DENSITY: Density of streams in columns (ranges from 0.0 to 1.0, default is 0.02).

## Controls:
Press Ctrl + C to quit the program.

## Example:
The program generates a visual effect where lines of "0"s and "1"s continuously scroll across the terminal, creating a flowing stream effect that gradually fades off the screen.

## License:
See the [LICENSE](LICENSE) file for details.

