import random


class CarrotInBoxGame:

    def __init__(self):
        self.p1_name = ""
        self.p2_name = ""
        self.carrot_in_first_box = False

    def display_intro(self):
        print('''Carrot in a Box, by Al Sw al@inventwithpython.com

        This is a bluffing game for two human players. Each player has a box.
        One box has a carrot in it. To win, you must have the box with the
        carrot in it.

        This is a very simple and silly game.

        The first player looks into their box (the second player must close
        their eyes during this). The first player then says "There is a carrot
        in my box" or "There is not a carrot in my box". The second player then
        gets to decide if they want to swap boxes or not.
        ''')

    def get_player_names(self):
        self.p1_name = input('Human player 1, enter your name: ')
        self.p2_name = input('Human player 2, enter your name: ')

    def show_boxes(self):
        player_names = self.p1_name[:11].center(
            11) + '    ' + self.p2_name[:11].center(11)
        print('''HERE ARE TWO BOXES:
           __________     __________
          /         /|   /         /|
         +---------+ |  +---------+ |
         |   RED   | |  |   GOLD  | |
         |   BOX   | /  |   BOX   | /
         +---------+/   +---------+/''')
        print(player_names)

    def first_player_view(self):
        print(self.p1_name + ', you have a RED box in front of you.')
        print(self.p2_name + ', you have a GOLD box in front of you.')
        print()
        print(self.p1_name + ', you will get to look into your box.')
        print(self.p2_name.upper() + ', close your eyes and don\'t look!!!')
        input('When ' + self.p2_name + ' has closed their eyes, press Enter..')
        print()
        print(self.p1_name + ' here is the inside of your box:')
        self.carrot_in_first_box = random.randint(1, 2) == 1
        if self.carrot_in_first_box:
            print('''
           ___VV____
          |   VV    |
          |   VV    |
          |___||____|    __________
         /    ||   /|   /         /|
        +---------+ |  +---------+ |
        |   RED   | |  |   GOLD  | |
        |   BOX   | /  |   BOX   | /
        +---------+/   +---------+/
         (carrot!)''')
        else:
            print('''
           _________
          |         |
          |         |
          |_________|    __________
         /         /|   /         /|
        +---------+ |  +---------+ |
        |   RED   | |  |   GOLD  | |
        |   BOX   | /  |   BOX   | /
        +---------+/   +---------+/
        (no carrot!)''')
        input('Press Enter to continue...')
        print('\n' * 100)  # Очищаем экран.
        print(self.p1_name + ', tell ' + self.p2_name + ' to open their eyes.')

    def bluffing_phase(self):
        input('Press Enter to continue...')
        print()
        print(self.p1_name +
              ', say one of the following sentences to ' + self.p2_name + '.')
        print('  1) There is a carrot in my box.')
        print('  2) There is not a carrot in my box.')
        print()
        input('Then press Enter to continue...')

    def swap_phase(self):
        print()
        print(self.p2_name + ', do you want to swap boxes with ' +
              self.p1_name + '? YES/NO')
        while True:
            response = input('> ').upper()
            if not (response.startswith('Y') or response.startswith('N')):
                print(self.p2_name + ', please enter "YES" or "NO".')
            else:
                break

        first_box = 'RED '  # Обратите внимание на пробел после "D".
        second_box = 'GOLD'
        if response.startswith('Y'):
            self.carrot_in_first_box = not self.carrot_in_first_box
            first_box, second_box = second_box, first_box

        print(f'''HERE ARE THE TWO BOXES:
          __________     __________
         /         /|   /         /|
        +---------+ |  +---------+ |
        |   {first_box}  | |  |   {second_box}  | |
        |   BOX   | /  |   BOX   | /
        +---------+/   +---------+/''')
        input('Press Enter to reveal the winner...')
        print()

    def reveal_winner(self):
        if self.carrot_in_first_box:
            print('''
           ___VV____      _________
          |   VV    |    |         |
          |   VV    |    |         |
          |___||____|    |_________|
         /    ||   /|   /         /|
        +---------+ |  +---------+ |
        |   RED   | |  |   GOLD  | |
        |   BOX   | /  |   BOX   | /
        +---------+/   +---------+/''')
            print(f'{self.p1_name} is the winner!')
        else:
            print('''
           _________      ___VV____
          |         |    |   VV    |
          |         |    |   VV    |
          |_________|    |___||____|
         /         /|   /    ||   /|
        +---------+ |  +---------+ |
        |   GOLD  | |  |   RED   | |
        |   BOX   | /  |   BOX   | /
        +---------+/   +---------+/''')
            print(f'{self.p2_name} is the winner!')

        print('Thanks for playing!')

    def run_game(self):
        self.display_intro()
        self.get_player_names()
        self.show_boxes()
        self.first_player_view()
        self.bluffing_phase()
        self.swap_phase()
        self.reveal_winner()
