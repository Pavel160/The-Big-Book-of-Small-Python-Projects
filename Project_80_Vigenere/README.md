# Vigenère Cipher
**Author**: Al Sweigart (al@inventwithpython.com)

## Description
The Vigenère Cipher is a classical encryption technique that uses a series of Caesar ciphers based on a keyword. It encrypts text by shifting each letter in the plaintext according to the corresponding letter in the keyword, looping the keyword as necessary. This Python implementation provides tools for encrypting and decrypting messages using the Vigenère Cipher.

## Features

1. Encrypt plaintext messages using a keyword.
2. Decrypt ciphertext messages using the same keyword.
3. Handles uppercase and lowercase letters, ignoring non-alphabetic characters.
4. Easy-to-use console interface.

## Requirements

Python 3.7 or higher.

## How to Use

1. Run the program:
```bash

python main.py
```
2. Choose whether to encrypt or decrypt a message.
3. Enter the plaintext or ciphertext and the keyword when prompted.
4. The program will display the encrypted or decrypted message.

## How the Cipher Works

1. Encryption:
Each letter of the plaintext is shifted forward by the position of the corresponding letter in the keyword. For example:

   - Plaintext: A
   - Keyword: K (10th letter, so shift by 10)
   - Encrypted: K
2. Decryption:
The process is reversed, shifting letters backward by the keyword's position.

3. Non-alphabetic characters (e.g., spaces, punctuation) are preserved and not encrypted.

## License

See the [LICENSE](LICENSE) file for details.
