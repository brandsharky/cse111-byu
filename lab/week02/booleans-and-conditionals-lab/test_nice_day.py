from byu_pytest_utils import dialog, test_files, this_folder
import random

random.seed(0)


@dialog(test_files / 'test_yes_nice_day.dialog.txt', this_folder / 'nice_day.py')
def test_NICE_DAY_yes():
    ...


@dialog(test_files / 'test_not_nice_day.dialog.txt', this_folder / 'nice_day.py')
def test_NICE_DAY_not():
    ...
