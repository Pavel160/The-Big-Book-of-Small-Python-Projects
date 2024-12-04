from config import MAX_GUESSES, NUM_DIGITS
import random


class BagelsGame:
    def __init__(self):
        pass

    def getSecretNum(self):
        """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
        numbers = list('0123456789')
        random.shuffle(numbers)
        return ''.join(numbers[:NUM_DIGITS])

    def getClues(self, guess, secretNum):
        """Возвращает строку с подсказками "Pico", "Fermi" и "Bagels"."""
        if guess == secretNum:
            return 'You got it!'
        clues = []
        for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                clues.append('Fermi')
            elif guess[i] in secretNum:
                clues.append('Pico')
        if not clues:
            return 'Bagels'
        clues.sort()
        return ' '.join(clues)

    def main(self):
        print(f'''Bagels, a deductive logic game.
        I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        Pico  - One digit is correct but in the wrong position.
        Fermi - One digit is correct and in the correct position.
        Bagels - No digit is correct.''')

        while True:
            secretNum = self.getSecretNum()
            print('I have thought up a number.')
            print(f'You have {MAX_GUESSES} guesses to get it.')

            numGuesses = 1
            while numGuesses <= MAX_GUESSES:
                guess = ''
                while len(guess) != NUM_DIGITS or not guess.isdecimal():
                    print(f'Guess #{numGuesses}:')
                    guess = input('> ')

                clues = self.getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break
                if numGuesses > MAX_GUESSES:
                    print(f'You ran out of guesses. The answer was {\
                          secretNum}.')

            if input('Do you want to play again? (yes or no)\n> ') \
                    .lower().startswith('y'):
                continue
            break

        print('Thanks for playing!')
