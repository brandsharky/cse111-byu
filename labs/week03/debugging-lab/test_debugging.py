from byu_pytest_utils import with_import

@with_import('debugging', 'even_digit_counter')
def test_digit_counter(even_digit_counter):
    assert even_digit_counter(1112) == 1
    assert even_digit_counter(1832233) == 3
    assert even_digit_counter(134) == 1


@with_import('debugging', 'largest_factor')
def test_largest_factor(largest_factor):
    assert largest_factor(0) == 0
    assert largest_factor(2) == 1
    assert largest_factor(1) == 1
    assert largest_factor(3) == 1
    assert largest_factor(4) == 2
    assert largest_factor(8) == 4
    assert largest_factor(7) == 1
    assert largest_factor(9) == 3
    assert largest_factor(16) == 8
    assert largest_factor(25) == 5


@with_import('debugging', 'missing_digits')
def test_missing_digits(missing_digits):
    assert missing_digits(33) == 0
    assert missing_digits(1278) == 4
    assert missing_digits(1122) == 0
    assert missing_digits(9) == 0


@with_import('debugging', 'square_root')
def test_square_root(square_root):
    result, iterations = square_root(9)
    assert result == 3.0000
    assert iterations <= 24

    result, iterations = square_root(16)
    assert result == 4.0000
    assert iterations <= 24

    result, iterations = square_root(10)
    assert result == 3.1623
    assert iterations <= 24

    result, iterations = square_root(3)
    assert result == 1.7321
    assert iterations <= 22
