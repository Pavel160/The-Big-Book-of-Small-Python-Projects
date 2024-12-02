# Simple Substitution Cipher

**Author**: Al Sweigart (al@inventwithpython.com)

## Description
The Simple Substitution Cipher is a basic encryption algorithm where each letter in the plaintext is substituted with another letter. In this cipher, each letter of the alphabet is mapped to a different letter in a fixed way.

This cipher is commonly used in introductory cryptography exercises and can be implemented using a basic algorithm.

## Features
- Encrypt and decrypt messages using a simple substitution cipher.
- The program supports custom key generation (you can specify your own substitution key).
- Optionally, the cipher can handle both lowercase and uppercase letters.
- Supports both encryption and decryption functionalities.

## How It Works
In a Simple Substitution Cipher, each letter of the alphabet is replaced by another letter. For example:

- Plaintext: HELLO
- Ciphertext: ETBBS (This is just an example; the actual cipher depends on the substitution key).

The key is a string of 26 characters, each representing a letter from the alphabet. For example, if the key is:

```
WNOMTRCEHDXBFVSLKAGZIPYJQU
```
This means that A will be replaced with W, B with N, C with O, and so on.

## Installation
1. Clone or download the repository to your local machine.
Make sure you have Python 3 installed.
2. To run the program, simply execute the following command in your terminal or command prompt:

```bash
python main.py
```
## Usage
1. ### Encrypting a Message:

- Input a message that you would like to encrypt.
- Choose or provide a substitution key.
- The program will return the encrypted message.

2. ### Decrypting a Message:

- Input the encrypted message (ciphertext).
- Provide the same key that was used for encryption.
- The program will return the original message.

## Example
### Encryption:
```python

plaintext = "HELLO"
key = "WNOMTRCEHDXBFVSLKAGZIPYJQU"
ciphertext = encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")
```
### Decryption:
```python

ciphertext = "ETBBS"
key = "WNOMTRCEHDXBFVSLKAGZIPYJQU"
plaintext = decrypt(ciphertext, key)
print(f"Decrypted: {plaintext}")
```
### Output:
```makefile

Encrypted: ETBBS
Decrypted: HELLO
```
## Functions
### encrypt(plaintext, key)
Encrypts the provided plaintext using the given key and returns the encrypted ciphertext.

- plaintext: The message to be encrypted.
- key: A string of 26 characters (substitution key).

### decrypt(ciphertext, key)
Decrypts the provided ciphertext using the given key and returns the original plaintext.

- ciphertext: The message to be decrypted.
- key: The key used for encryption.

## Example Key
A sample substitution key might look like this:

```
QAZWSXEDCRFVTGBYHNUJMIKOLP
```
You can also create your own key to use for encryption and decryption.

## License
See the [LICENSE](LICENSE) file for details.
