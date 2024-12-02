# Seven-Segment Display Module

**Author**: Al Sweigart (al@inventwithpython.com)

The Seven-Segment Display Module is designed to convert numbers into graphical representations using a seven-segment display. It can be used for building digital clocks, counters, timers, and other applications requiring visual representation of numbers.

## Features of the Module
Main Function: getSevSegStr(number, minWidth=0)
- Description:

Converts a given number into a string that visually represents it on a seven-segment display.

- Arguments:

   - number: The number (integer or float) to be converted.
   - minWidth: The minimum width of the number. If the number is shorter than this width, it is padded with leading zeros.
- Return Value:

A string consisting of three lines of characters representing the seven-segment display.

## Running Directly
### If the module is executed directly, it will display instructions on how to use it:

```bash
python main.py
```
## License
See the [LICENSE](LICENSE) file for details.
