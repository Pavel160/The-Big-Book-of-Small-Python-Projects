# ROT13 Cipher
**Author**: Al Sweigart (al@inventwithpython.com)

This is a simple ROT13 cipher program that encodes and decodes messages using the ROT13 encryption method.

Tags: cipher, encryption, ROT13, encoding, decoding, cryptography, beginner

## Description
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 places after it in the alphabet. Since the alphabet has 26 letters, applying the ROT13 cipher twice will return the original text.

This program allows you to encode and decode messages using ROT13, making it a fun and simple way to "hide" text in plain sight. ROT13 is often used to obscure spoilers, puzzle answers, or sensitive information on websites.

### How It Works
- ROT13 shifts each letter of the input by 13 places in the alphabet.
  - For example, "A" becomes "N", "B" becomes "O", and so on.
- The cipher works the same way for both uppercase and lowercase letters.
- Non-alphabetic characters (numbers, punctuation, spaces) are not altered.

## Example:
- Input: Hello, World!
- ROT13 Output: Uryyb, Jbeyq!
- Decoding the ROT13 output will give you back the original message.

## How to Use
1. Run the program.
2. Enter a message: The program will prompt you to input the text you want to encode or decode.
3. Choose to encode or decode: You can either encode the message (if it's in plain text) or decode the message (if it's already in ROT13).
4. View the result: The program will display the encoded or decoded message.
5. Repeat: You can encode or decode multiple messages as needed.

## Example Usage
```plaintext

Enter your message to encode or decode: Hello, World!
Encoded message: Uryyb, Jbeyq!
```
## Getting Started
To run the program:

1. Clone or download the repository.
2. Run the rot13cipher.py script.
3. Start the game:
   ```bash
   python main.py

4. Enter a message when prompted and choose whether to encode or decode.

## License
See the [LICENSE](LICENSE) file for details.
