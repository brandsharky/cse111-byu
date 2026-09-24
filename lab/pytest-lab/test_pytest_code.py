# Remember to import from the pytest_code file and pytest
import pytest
from pytest import approx, raises

from pytest_code import *



# Write your test code here for Q1
def test_product():
    assert product(3) == 6
    assert product(5) == 120

    with raises(ValueError):
        product(0)

    with raises(ValueError):
        product(-1)

    with raises(ValueError):
        product(1.5)

    with raises(ValueError):
        product("5")

def test_summation():
    assert summation(0) == 0
    assert summation(1) == 1
    assert summation(5) == 15

    with raises(ValueError):
        summation(-1)

    with raises(ValueError):
        summation(1.5)

    with raises(ValueError):
        summation("5")


# Q2
#####################################

def test_square():
    assert square(3) == 9


def test_sqrt():
    """*** YOUR CODE HERE ***"""


def test_mean():
    """*** YOUR CODE HERE ***"""


def test_median():
    """*** YOUR CODE HERE ***"""


def test_mode():
    """*** YOUR CODE HERE ***"""


def test_std_dev():
    """*** YOUR CODE HERE ***"""


def test_stat_analysis():
    """*** YOUR CODE HERE ***"""


#####################################

def test_accumulate():
    """*** YOUR CODE HERE ***"""


def test_product_short():
    """*** YOUR CODE HERE ***"""


def test_summation_short():
    """*** YOUR CODE HERE ***"""


def test_invert():
    """*** YOUR CODE HERE ***"""


def test_change():
    """*** YOUR CODE HERE ***"""


def test_invert_short():
    """*** YOUR CODE HERE ***"""


def test_change_short():
    """*** YOUR CODE HERE ***"""
