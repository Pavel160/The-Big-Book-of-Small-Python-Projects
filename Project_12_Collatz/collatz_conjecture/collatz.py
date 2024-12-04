import sys
import time


class CollatzSequence:
    def __init__(self, number):
        if not isinstance(number, int) or number <= 0:
            raise ValueError("Starting number must be an int greater than 0.")
        self.number = number

    def generate_sequence(self):
        num = self.number
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            sequence.append(num)
        return sequence

    def display_sequence(self):
        sequence = self.generate_sequence()
        for i, num in enumerate(sequence):
            end = ', ' if i < len(sequence) - 1 else '\n'
            print(num, end=end, flush=True)
            time.sleep(0.1)


def main():
    print('''Collatz Sequence, or, the 3n + 1 Problem
    By Al Sw al@inventwithpython.com

    The Collatz sequence is a sequence of numbers produced from a starting
    number n, following three rules:

    1) If n is even, the next number n is n / 2.
    2) If n is odd, the next number n is n * 3 + 1.
    3) If n is 1, stop. Otherwise, repeat.

    It is generally thought, but so far not mathematically proven, that
    every starting number eventually terminates at 1.
    ''')
    while True:
        response = input('Enter a starting number (greater than 0) or QUIT:\n> ')
        if response.upper() == 'QUIT':
            print("Goodbye!")
            sys.exit()
        if not response.isdecimal() or response == '0':
            print('You must enter an integer greater than 0.')
            continue

        number = int(response)
        collatz = CollatzSequence(number)
        collatz.display_sequence()
