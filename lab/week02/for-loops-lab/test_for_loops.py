from byu_pytest_utils import with_import, this_folder, test_files, dialog, ensure_missing
from pytest import approx
from pathlib import Path


@with_import('for_loops', 'every_other_letter')
def test_Q1_every_other_letter(every_other_letter):
    output = every_other_letter("hello")
    assert output == "hlo"
    output = every_other_letter("abcdefg")
    assert output == "aceg"
    output = every_other_letter("A")
    assert output == "A"


@dialog(test_files / 'test_Q2_print_triangle_5.dialog.txt', this_folder / 'for_loops.py')
def test_Q2_print_triangle_5():
    ...


@dialog(test_files / 'test_Q2_print_triangle_20.dialog.txt', this_folder / 'for_loops.py')
def test_Q2_print_triangle_20():
    ...

@with_import('for_loops', 'increment_numbers')
def test_Q3_increment_numbers(increment_numbers):
    lst = [1, 2, 3, 4, 5]
    increment_numbers(lst)
    assert lst == [2, 3, 4, 5, 6]
    lst = [-5, 4.2, 124, 23, 100, -93]
    increment_numbers(lst)
    assert lst == [-4, 5.2, 125, 24, 101, -92]


@with_import('for_loops', 'average_temperature')
def test_Q4_average_temperature(average_temperature):
    assert average_temperature([72.2, 68.7, 67.4, 77.3, 81.6, 83.7]) == approx(75.15)
    assert average_temperature([63.4, 70.8, 52.3, 74.6, 69.2, 54.3]) == approx(64.1)


@with_import('for_loops', 'hot_days')
def test_Q5_hot_days_return1(hot_days, capfd):
    result = hot_days([72.2, 68.7, 67.4, 77.3, 81.6, 83.7])
    out, _ = capfd.readouterr()

    assert out == "There were 2 day(s) more than 5 degrees above the average of 75.2.\n"
    assert result == 2


@with_import('for_loops', 'hot_days')
def test_Q5_hot_days_return2(hot_days, capfd):
    result = hot_days([63.4, 70.8, 52.3, 74.6, 69.2, 54.3])
    out, _ = capfd.readouterr()

    assert out == "There were 3 day(s) more than 5 degrees above the average of 64.1.\n"
    assert result == 3


@with_import('for_loops', 'reverse_lines')
@ensure_missing(this_folder / 'output.txt')
def test_Q6_reverse_lines_1(reverse_lines):
    reverse_lines('test_files/test_Q2_print_triangle_5.dialog.txt', 'output.txt')
    key = """
``02;evif; 5 4 3 2 1``
``02;ruof; 4 3 2 1``
``02;eerht; 3 2 1``
``02;owt; 2 1``
``02;eno; 1``
>>5<<
"""
    with open(this_folder / 'output.txt', 'r') as fin:
        assert fin.read() == key
    Path.unlink(this_folder / 'output.txt', missing_ok=True)


@with_import('for_loops', 'reverse_lines')
@ensure_missing(this_folder / 'output.txt')
def test_Q6_reverse_lines_2(reverse_lines):
    reverse_lines('test_files/cats.txt', 'output.txt')
    key = """Cats are great.
The Rusty-Spotted Cat is the smallest cat species.
The Siberian Tiger is the largest cat species.
There are only 4 species of cats that can roar: lions, leopards, jaguars, and tigers.
The roaring cats are in the genus Panthera.
The domestic cat (felis catus) is closely related to the African and European wildcats (F. lybica and F. silvestris)
The Florida panther is really a puma. It is the same species as the cougars in the Rocky Mountains.
Many cat species can purr, including cheetahs, bobcats, and cougars.
A cheetah's top speed ranges between 65 and 75 mph.
Hyenas are closely related to cats."""
    with open(this_folder / 'output.txt', 'r') as fin:
        assert fin.read() == key
    Path.unlink(this_folder / 'output.txt', missing_ok=True)
