from byu_pytest_utils import dialog, test_files, this_folder
import random

random.seed(536) # [95, 24, 80, 68, 71]

@dialog(test_files / 'test_A.dialog.txt', this_folder / 'grade.py')
def test_GRADE_A():
    ...

@dialog(test_files / 'test_F.dialog.txt', this_folder / 'grade.py')
def test_GRADE_F():
    ...

@dialog(test_files / 'test_B.dialog.txt', this_folder / 'grade.py')
def test_GRADE_B():
    ...
