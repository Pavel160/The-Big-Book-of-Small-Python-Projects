"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math"""

try:
    import pyperclip
except ImportError:
    pyperclip = None


class CaesarCipher:
    def __init__(self):
        self.symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt_or_decrypt(self, message, key, mode):
        translated = ''
        for symbol in message:
            if symbol in self.symbols:
                num = self.symbols.find(symbol)
                if mode == 'encrypt':
                    num += key
                elif mode == 'decrypt':
                    num -= key
                if num >= len(self.symbols):
                    num -= len(self.symbols)
                elif num < 0:
                    num += len(self.symbols)
                translated += self.symbols[num]
            else:
                translated += symbol

        return translated

    def copy_to_clipboard(self, translated, mode):
        if pyperclip:
            try:
                pyperclip.copy(translated)
                print(f'Full {mode}ed text copied to clipboard.')
            except Exception as e:
                print(f"Произошла ошибка при копировании в буфер обмена: {e}")

    def main(self):
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print('Caesar Cipher, by Al Sw al@inventwithpython.com')
        print('The Caesar cipher encrypts letters by shifting them over by a')
        print('key number. For example, a key of 2 means the letter A is')
        print('encrypted into C, the letter B encrypted into D, and so on.')
        print()

        # Спрашиваем у пользователя, хочет ли он шифровать или расшифровывать:
        while True:  # Повторяем вопрос, пока пользователь не введет e или d.
            print('Do you want to (e)ncrypt or (d)ecrypt?')
            response = input('> ').lower()
            if response.startswith('e'):
                mode = 'encrypt'
                break
            elif response.startswith('d'):
                mode = 'decrypt'
                break
            print('Please enter the letter e or d.')
        # Просим пользователя ввести ключ шифрования:
        while True:  # Повторяем вопрос
            maxKey = len(SYMBOLS) - 1
            print('Please enter the key (0 to {}) to use.'.format(maxKey))
            response = input('> ').upper()
            if not response.isdecimal():
                continue
            if 0 <= int(response) < len(SYMBOLS):
                key = int(response)
                break
        # Просим пользователя ввести сообщение для шифрования/расшифровки:
        print('Enter the message to {}.'.format(mode))
        message = input('> ')
        # Шифр Цезаря работает только с символами в верхнем регистре:
        message = message.upper()

        # Выполняем шифрование или расшифровку
        translated = self.encrypt_or_decrypt(message, key, mode)

        print(translated)
        self.copy_to_clipboard(translated, mode)
