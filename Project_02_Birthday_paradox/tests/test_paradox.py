# Импортируем класс BirthdayParadox
from birthday_paradox.birthday_paradox import BirthdayParadox


def test_getBirthdays():
    # Тестируем, что метод get_birthdays генерирует правильное количество дней рождения
    game = BirthdayParadox()
    birthdays = game.getBirthdays(10)
    assert len(birthdays) == 10, f"Expected 10 birthdays, but got {
        len(birthdays)}"


def test_getMatch():
    # Тестируем метод getMatch для проверки совпадений
    birthdays = ['2001-01-01', '2001-01-01', '2001-02-02']  # Пример данных
    game = BirthdayParadox()
    match = game.getMatch(birthdays)
    assert match == '2001-01-01', f"Expected match on '2001-01-01', but got {
        match}"
