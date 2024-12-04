class CaesarCipherHacker:

    def __init__(self):
        self.symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def deciphering_symbol(self, message):
        # Проходим в цикле по всем возможным ключам.
        for key in range(len(self.symbols)):
            translated = ''
            for symbol in message:
                if symbol in self.symbols:
                    num = self.symbols.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(self.symbols)
                    translated += self.symbols[num]
                else:
                    translated += symbol
            print(f'Key #{key}: {translated}')

    def main(self):
        print('Caesar Cipher Hacker, by Al Sw al@inventwithpython.com')
        print('Enter the encrypted Caesar cipher message to hack.')
        message = input('> ')
        self.deciphering_symbol(message)
