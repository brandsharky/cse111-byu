from byu_pytest_utils import dialog, test_files, this_folder
import random

random.seed(16)

@dialog(test_files / 'test_on.dialog.txt', this_folder / 'light_switches.py')
def test_LIGHT_SWITCHES_on():
    ...

@dialog(test_files / 'test_off.dialog.txt', this_folder / 'light_switches.py')
def test_LIGHT_SWITCHES_off():
    ...
