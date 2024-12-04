# LeetSpeak Translator

**Author**: Al Sweigart (al@inventwithpython.com)

This Python script translates English messages into leetspeak (1337speak), a form of writing that replaces letters with similar-looking characters, often used in online communities. The program uses a 70% chance to replace each character with its leetspeak equivalent, making each translation unique.

## Features

- Converts English text into leetspeak with random variations.
- Each character in the input message has a 30% chance of remaining unchanged and a 70% chance of being replaced with a corresponding leetspeak character.
- Optionally, the translated message can be copied to the clipboard using the `pyperclip` library.

## How It Works

1. The program takes an English message as input.
2. It iterates through each character in the message.
3. For each character, if there is a corresponding leetspeak character defined in the `charMapping` dictionary, the program randomly decides whether to replace it.
4. If the character is replaced, it is substituted with one of the possible leetspeak characters (with a 70% probability).
5. The transformed message is printed to the screen and copied to the clipboard (if `pyperclip` is installed).
6. Install Python (version 3.6 or higher).
7. If you want to copy the translated message to the clipboard, install the `pyperclip` library:

   ```bash
   pip install pyperclip

## Example
Input:

```
Hello, World!
```
Output:

```
]-[3||0, W0r1d!
```

## Customization
You can customize the leetspeak characters by modifying the charMapping dictionary in the script. For each letter, you can add multiple leetspeak alternatives.

## License
See the [LICENSE](LICENSE) file for details.
