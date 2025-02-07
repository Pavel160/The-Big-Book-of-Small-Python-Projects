from bagels.bagels import BagelsGame


def test_getSecretNum():
    game = BagelsGame()
    secret_number = game.getSecretNum()
    assert len(secret_number) == 3, "Число должно состоять из 3 цифр"
    assert len(set(secret_number)) == 3, "Цифры должны быть уникальными"
    assert secret_number.isdigit(), "Число должно содержать только цифры"


def test_getClues():
    game = BagelsGame()
    secret_number = "123"

    assert game.getClues(
        "123", secret_number) == "You got it!", "Сообщение должно быть 'You got it!' при правильном ответе"

    # Проверка различных комбинаций на "Fermi", "Pico" и "Bagels"
    assert game.getClues(
        "124", secret_number) == "Fermi Fermi", "Ожидается 'Fermi Fermi'"
    assert game.getClues(
        "231", secret_number) == "Pico Pico Pico", "Ожидается 'Pico Pico Pico'"
    assert game.getClues(
        "456", secret_number) == "Bagels", "Ожидается 'Bagels' при отсутствии совпадений"
    assert game.getClues(
        "321", secret_number) == "Fermi Pico Pico", "Ожидается 'Fermi Pico Pico' при частичных совпадениях"
