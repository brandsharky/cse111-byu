from byu_pytest_utils import dialog, test_files, this_folder
import random

random.seed(0)

@dialog(test_files / 'test_TRIANGLE_valid.dialog.txt', this_folder / 'triangle.py')
def test_TRIANGLE_valid_1():
    ...

@dialog(test_files / 'test_TRIANGLE_invalid.dialog.txt', this_folder / 'triangle.py')
def test_TRIANGLE_invalid():
    ...

@dialog(test_files / 'test_TRIANGLE_valid.dialog.txt', this_folder / 'triangle.py')
def test_TRIANGLE_valid_2():
    ...
