"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short"""
import datetime


class CalendarMaker:

    DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday')
    MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')

    def __init__(self):
        self.year = self.get_year()
        self.month = self.get_month()

    def get_year(self):

        while True:  # Цикл для запроса у пользователя года.
            print('Enter the year for the calendar:')
            response = input('> ')
            if response.isdecimal() and int(response) > 0:
                return int(response)

    def get_month(self):

        while True:  # Цикл для запроса у пользователя месяца.
            print('Enter the month for the calendar, 1-12:')
            response = input('> ')
            if not response.isdecimal():
                print('Please enter a numeric month, like 3 for March.')
                continue
            month = int(response)
            if 1 <= month <= 12:
                return month

    def get_calendar_for(self, year, month):
        calText = ''  # calText содержит строковое значение с календарем.
        # Размещаем месяц и год вверху календаря:
        calText += (' ' * 34) + self.MONTHS[month - 1] + ' ' + str(year) + '\n'
        # Добавляем в календарь метки дней недели:
        # (!) Попробуйте заменить их аббревиатурами: SUN, MON, TUE и т. д.
        calText += '...Sunday.....Monday....Tuesday...Wednesday..Thursday....Friday....Saturday..\n'
        # Горизонтальная линия — разделитель недель:
        weekSeparator = ('+----------' * 7) + '+\n'
        # Пустые строки содержат по десять пробелов между разделителями дней |:
        blankRow = ('|          ' * 7) + '|\n'
        # Получаем первую дату месяца. (Модуль datetime берет на себя
        # все сложные нюансы календарных вычислений.)
        currentDate = datetime.date(year, month, 1)
        # Отнимаем от currentDate по дню, пока не дойдем до воскресенья.
        # (weekday() возвращает для воскресенья 6, а не 0.)
        while currentDate.weekday() != 6:
            currentDate -= datetime.timedelta(days=1)
        while True:  # Проходим в цикле по всем неделям в месяце.
            calText += weekSeparator
            # dayNumberRow — строка с метками номеров дней:
            dayNumberRow = ''
            for i in range(7):
                dayNumberLabel = str(currentDate.day).rjust(2)
                dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
                # Переходим к следующему дню.
                currentDate += datetime.timedelta(days=1)
            # Добавляем вертикальную линию после субботы.
            dayNumberRow += '|\n'
            # Добавляем в текст календаря строку с номерами
            # дней и 3 пустых строки.
            calText += dayNumberRow
            for i in range(3):  # (!) Попробуйте заменить 3 на 5 или 10.
                calText += blankRow
            # Проверяем, закончили ли мы обработку месяца:
            if currentDate.month != month:
                break
        # Добавляем горизонтальную линию в самом низу календаря.
        calText += weekSeparator
        return calText

    def save_calendar(self, cal_text):
        calendar_filename = 'calendar_{}_{}.txt'.format(self.year, self.month)
        with open(calendar_filename, 'w') as file_obj:
            file_obj.write(cal_text)
        print('Saved to ' + calendar_filename)

    def run(self):
        print('Calendar Maker, by Al Sw al@inventwithpython.com')
        cal_text = self.get_calendar_for(self.year, self.month)
        print(cal_text)
        self.save_calendar(cal_text)
