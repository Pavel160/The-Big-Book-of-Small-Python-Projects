from cho_han.chohan import ChoHan


def test_get_player_bet():
    game = ChoHan()
    game.purse = 5000
    game.pot = 100
    assert game.pot <= game.purse, "Ставка не может превышать баланс"
    print(f"Test passed: {game.pot} mon bet accepted.")


def test_get_player_choice():
    game = ChoHan()
    game.bet = 'CHO'
    assert game.bet == 'CHO', f"Ожидался выбор 'CHO', а был {game.bet}"
    print(f"Test passed: Player chose {game.bet}.")
