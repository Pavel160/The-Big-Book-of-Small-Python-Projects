from carrot_in_box.carrotinabox import CarrotInBoxGame


def test_reveal_winner():
    game = CarrotInBoxGame()

    if game.carrot_in_first_box:
        print(f'{game.p1_name} is the winner!')
    else:
        print(f'{game.p2_name} is the winner!')
