"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""

import datetime
import random


class BirthdayParadox:
    def __init__(self):
        pass


    def getBirthdays(self, numberOfBirthdays):
        """Возвращаем список объектов дат для случайных дней рождения."""
        birthdays = []
        for i in range(numberOfBirthdays):
            startOfYear = datetime.date(2001, 1, 1)
            randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
            birthday = startOfYear + randomNumberOfDays
            birthdays.append(birthday)
        return birthdays

    def getMatch(self, birthdays):
        """Возвращаем объект даты дня рождения, встречающегося
        несколько раз в списке дней рождения."""
        if len(birthdays) == len(set(birthdays)):
            return None
        for a, birthdayA in enumerate(birthdays):
            for b, birthdayB in enumerate(birthdays[a + 1:]):
                if birthdayA == birthdayB:
                    return birthdayA

    def main(self):
        # Отображаем вводную информацию:
        print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
        The Birthday Paradox shows us that in a group of N people, the odds
        that two of them have matching birthdays is surprisingly large.
        This program does a Monte Carlo simulation (that is, repeated random
        simulations) to explore this concept.
        (It's not actually a paradox, it's just a surprising result.)
        ''')
        # Создаем кортеж названий месяцев по порядку:
        MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        while True:  # Запрашиваем, пока пользователь не введет допустимое значение.
            print('How many birthdays shall I generate? (Max 100)')
            response = input('> ')
            if response.isdecimal() and (0 < int(response) <= 100):
                numBDays = int(response)
                break  # Пользователь ввел допустимое значение.
        print()
        # Генерируем и отображаем дни рождения:
        print('Here are', numBDays, 'birthdays:')
        birthdays = self.getBirthdays(numBDays)
        for i, birthday in enumerate(birthdays):
            if i != 0:
                # Выводим запятую для каждого дня рождения после первого.
                print(', ', end='')
            monthName = MONTHS[birthday.month - 1]
            dateText = '{} {}'.format(monthName, birthday.day)
            print(dateText, end='')
        print()
        print()
        # Выясняем, встречаются ли два совпадающих дня рождения.
        match = self.getMatch(birthdays)
        # Отображаем результаты:
        print('In this simulation, ', end='')
        if match is not None:
            monthName = MONTHS[match.month - 1]
            dateText = '{} {}'.format(monthName, match.day)
            print('multiple people have a birthday on', dateText)
        else:
            print('there are no matching birthdays.')
        print()
        # Производим 100 000 операций имитационного моделирования:
        print('Generating', numBDays, 'random birthdays 100,000 times...')
        input('Press Enter to begin...')
        print('Let\'s run another 100,000 simulations.')
        simMatch = 0  # Число операций моделирования с совпадающими днями рождения.
        for i in range(100_000):
            # Отображаем сообщение о ходе выполнения каждые 10 000 операций:
            if i % 10_000 == 0:
                print(i, 'simulations run...')
            birthdays = self.getBirthdays(numBDays)
            if self.getMatch(birthdays) is not None:
                simMatch = simMatch + 1
        print('100,000 simulations run.')
        # Отображаем результаты имитационного моделирования:
        probability = round(simMatch / 100_000 * 100, 2)
        print('Out of 100,000 simulations of', numBDays, 'people, there was a')
        print('matching birthday in that group', simMatch, 'times. This means')
        print('that', numBDays, 'people have a', probability, '% chance of')
        print('having a matching birthday in their group.')
        print('That\'s probably more than you would think!')
