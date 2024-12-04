from rhombuses.rhombuses import *

def test_outline_diamond_size_1(capsys):
    displayOutlineDiamond(1)
    captured = capsys.readouterr()  # Захватываем вывод
    expected_output = "/\\\n\\/"  # Ожидаемый вывод
    assert captured.out.strip() == expected_output  # Удаляем лишние символы новой строки с конца


def test_filled_diamond_size_1(capsys):
    displayFilledDiamond(1)
    captured = capsys.readouterr()  # Захватываем вывод
    expected_output = "/\\\n\\/"
    assert captured.out.strip() == expected_output  # Удаляем лишние символы новой строки с конца


def test_outline_diamond_size_2(capsys):
    displayOutlineDiamond(2)
    captured = capsys.readouterr()  # Захватываем вывод
    expected_output = " /\\\n/  \\\n\\  /\n \\/"
    assert captured.out.rstrip() == expected_output  # Удаляем лишние символы новой строки с конца


def test_filled_diamond_size_2(capsys):
    displayFilledDiamond(2)
    captured = capsys.readouterr()  # Захватываем вывод
    expected_output = " /\\\n//\\\\\n\\\\//\n \\/"
    assert captured.out.rstrip() == expected_output  # Удаляем лишние символы новой строки с конца
