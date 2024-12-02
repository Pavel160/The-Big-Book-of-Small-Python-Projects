from collatz_conjecture.collatz import CollatzSequence

def test_generate_sequence():
    """Тест генерации последовательности для различных стартовых чисел."""

    # Тест для n = 1
    seq = CollatzSequence(1)
    assert seq.generate_sequence() == [1]

    # Тест для n = 2
    seq = CollatzSequence(2)
    assert seq.generate_sequence() == [2, 1]

    # Тест для n = 3
    seq = CollatzSequence(3)
    assert seq.generate_sequence() == [3, 10, 5, 16, 8, 4, 2, 1]

    # Тест для n = 6
    seq = CollatzSequence(6)
    assert seq.generate_sequence() == [6, 3, 10, 5, 16, 8, 4, 2, 1]