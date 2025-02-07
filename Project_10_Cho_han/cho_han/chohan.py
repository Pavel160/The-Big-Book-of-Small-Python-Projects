import random
import sys


class ChoHan:

    def __init__(self):
        self.purse = 5000  # Начальный баланс
        self.JAPANESE_NUMBERS = {
            1: 'ICHI',
            2: 'NI',
            3: 'SAN',
            4: 'SHI',
            5: 'GO',
            6: 'ROKU'
        }

    def run_game(self):
        print('''Cho-Han, by Al Sw al@inventwithpython.com
        In this traditional Japanese dice game, two dice are rolled in a bamboo
        cup by the dealer sitting on the floor. The player must guess if the
        dice total to an even (cho) or odd (han) number.
        ''')

        while True:  # Основной цикл игры
            self.get_player_bet()
            self.get_player_choice()
            self.play_round()

    def get_player_bet(self):
        while True:
            print(f'You have {self.purse} mon. How much do you bet? (or QUIT)')
            bet = input('> ')
            if bet.upper() == 'QUIT':
                print('Thanks for playing!')
                sys.exit()  # Заканчиваем игру
            if not bet.isdecimal():
                print('Please enter a number.')
            elif int(bet) > self.purse:
                print('You do not have enough money to make that bet.')
            else:
                self.pot = int(bet)
                break  # Ставка принята

    def get_player_choice(self):
        while True:
            print('CHO (even) or HAN (odd)?')
            bet = input('> ').upper()
            if bet != 'CHO' and bet != 'HAN':
                print('Please enter either "CHO" or "HAN".')
            else:
                self.bet = bet
                break  # Выбор принят

    def play_round(self):
        # Бросаем кости
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the floor, still covering the dice and asks for your bet.')
        print(f'The dice roll: {self.dice1} and {self.dice2}')

        # Определяем сумму
        total = self.dice1 + self.dice2
        print(f'Total: {total}')

        # Определяем, четная ли сумма (CHO) или нечетная (HAN)
        correct_bet = 'CHO' if total % 2 == 0 else 'HAN'

        # Открываем результат
        print(f'The dealer lifts the cup to reveal: {
              self.JAPANESE_NUMBERS[self.dice1]} - {self.JAPANESE_NUMBERS[self.dice2]}')
        print(f'You bet: {self.bet}, the correct bet was: {correct_bet}')

        # Проверяем, выиграл ли игрок
        if self.bet == correct_bet:
            print(f'You won! You take {self.pot} mon.')
            self.purse += self.pot  # Добавляем ставку в кошелек игрока
            house_fee = self.pot // 10
            print(f'The house collects a {house_fee} mon fee.')
            self.purse -= house_fee  # Сбор для игорного дома
        else:
            print('You lost!')
            self.purse -= self.pot  # Вычитаем ставку из кошелька игрока

        # Проверка, не закончились ли деньги
        if self.purse <= 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()  # Закрываем игру, если денег больше нет
