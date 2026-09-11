import random
from byu_pytest_utils import with_import, dialog, test_files, this_folder

random.seed(35)


@dialog(test_files / 'test_hello_world.dialog.txt', this_folder / 'functions.py')
def test_Q1_hello_world():
    ...


@with_import('functions', 'is_divisible')
def test_Q2_is_divisible(is_divisible):
    assert is_divisible(81, 9)
    assert not is_divisible(100, 9)


@with_import('functions', 'falling')
def test_Q3_falling(falling):
    output = falling(6, 3)
    assert output == 120
    output = falling(4, 1)
    assert output == 4
    output = falling(4, 0)
    assert output == 1


@with_import('functions', 'double_eights')
def test_Q4_double_eights(double_eights):
    assert double_eights(88)
    assert double_eights(2882)
    assert double_eights(880088)
    assert double_eights(12345) == False
    assert double_eights(80808080) == False


@with_import('functions', 'reverse_digits')
def test_Q5_reverse_digits(reverse_digits):
    output = reverse_digits(1234)
    assert output == 4321
    output = reverse_digits(5732081)
    assert output == 1802375


@with_import('date', 'format_date')
def test_Q6_format_date(format_date):
    output = format_date(10, 2, 2013)
    assert output == '10/02/2013'
    output = format_date(12, 30)
    assert output == '12/30/2025'


@dialog(test_files / 'test_converter_f.dialog.txt', this_folder / 'converter.py')
def test_Q7_converter_f():
    ...


@dialog(test_files / 'test_converter_c.dialog.txt', this_folder / 'converter.py')
def test_Q7_converter_c():
    ...


@dialog(test_files / 'test_rock_paper_scissors_win.dialog.txt', this_folder / 'rock_paper_scissors.py')
def test_Q8_rock_paper_scissors_win():
    ...


@dialog(test_files / 'test_rock_paper_scissors_tie.dialog.txt', this_folder / 'rock_paper_scissors.py')
def test_Q8_rock_paper_scissors_tie():
    ...


@dialog(test_files / 'test_rock_paper_scissors_lose.dialog.txt', this_folder / 'rock_paper_scissors.py')
def test_Q8_rock_paper_scissors_lose():
    ...


@with_import('date', 'format_date')
def test_Q9_valid_date(format_date):
    output = format_date(12, 30)
    assert output == '12/30/2025'
    output = format_date(2, 29, 2024)
    assert output == '02/29/2024'

    assert not format_date(12, 12, -4)
    assert not format_date(14, 1, 2004)
    assert not format_date(6, 31, 1782)
    assert not format_date(2, 29)
