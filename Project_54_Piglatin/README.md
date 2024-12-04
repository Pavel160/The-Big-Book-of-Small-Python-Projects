# Pig Latin Translator

**Author**: Al Sweigart (al@inventwithpython.com)

This Python program translates English messages into Pig Latin, a playful language transformation where words are modified by moving the first consonant or consonant cluster to the end of the word and adding "ay" (or "yay" if the word starts with a vowel).

Tags: short, word, language

## Features
- Converts an English message into Pig Latin.
- Handles punctuation and capitalization (upper case and title case).
- Optionally copies the result to the clipboard (requires pyperclip).

## Requirements
- Python 3.x
- Optional: pyperclip library for clipboard functionality. Install it using pip install pyperclip.

## How It Works
1. Vowel Check: If a word starts with a vowel, "yay" is added to the end.
2. Consonant Handling: If a word starts with consonants, the consonant or consonant cluster is moved to the end, followed by "ay".
3. Preserving Case: The program preserves the original case of words (uppercase or titlecase).
4. Punctuation Handling: It keeps non-alphabetic characters like punctuation marks at the beginning or end of words.

## Usage
1. Run the program.
2. Enter a message in English when prompted.
3. The message is translated into Pig Latin and printed.
4. If the pyperclip library is installed, the result is copied to the clipboard.

## Example
```scss
Igpay Atinlay (Pig Latin)
By Al Sweigart al@inventwithpython.com

Enter your message:
> Hello, how are you?

Ellohay, owhay areay ouyay?
(Copied pig latin to clipboard.)
```
## Code Overview
The code works in the following steps:

1. Input Handling: It accepts a message from the user.
2. Translation: Each word in the message is processed using the englishToPigLatin function, which:

   - Handles non-letter characters (punctuation).
   - Checks if the word starts with a vowel or consonant.
   - Translates the word into Pig Latin.

3. Clipboard Copying: If pyperclip is installed, the result is copied to the clipboard.

## License
See the [LICENSE](LICENSE) file for details.
