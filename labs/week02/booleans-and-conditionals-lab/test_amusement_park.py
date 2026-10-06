from byu_pytest_utils import dialog, test_files, this_folder
import random

random.seed(210) # 48, 24, 67

@dialog(test_files / 'test_ride_with_adult.dialog.txt', this_folder / 'amusement_park.py')
def test_AMUSEMENT_PARK_ride_with_adult():
    ...

@dialog(test_files / 'test_no_ride.dialog.txt', this_folder / 'amusement_park.py')
def test_AMUSEMENT_PARK_no_ride():
    ...

@dialog(test_files / 'test_ride.dialog.txt', this_folder / 'amusement_park.py')
def test_AMUSEMENT_PARK_ride():
    ...
