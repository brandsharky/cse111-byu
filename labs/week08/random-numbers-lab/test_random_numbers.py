import random
import pytest
from byu_pytest_utils import with_import


@with_import('random_numbers', 'roll_die')
def test_Q1_roll_die(roll_die):
    with pytest.raises(ValueError):
        roll_die(0)
    random.seed(12345)
    assert roll_die(6) == 4  # deterministic with seed


@with_import('random_numbers', 'roll_dice')
def test_Q2_roll_dice(roll_dice):
    with pytest.raises(ValueError):
        roll_dice(-1, 6)
    with pytest.raises(ValueError):
        roll_dice(3, 0)
    random.seed(2024)
    rolls = roll_dice(5, 6)
    assert len(rolls) == 5
    assert all(1 <= r <= 6 for r in rolls)
    assert rolls == [4, 2, 6, 5, 3]


@with_import('random_numbers', 'simulate_coin_flips')
def test_Q3_simulate_coin_flips(simulate_coin_flips):
    with pytest.raises(ValueError):
        simulate_coin_flips(-1)
    random.seed(7)
    h, t = simulate_coin_flips(10)
    assert (h, t) == (7, 3)


@with_import('random_numbers', 'random_float_range')
def test_Q4_random_float_range(random_float_range):
    with pytest.raises(ValueError):
        random_float_range(2.0, 2.0)
    with pytest.raises(ValueError):
        random_float_range(5.0, 2.0)
    random.seed(11)
    v = random_float_range(1.5, 3.5)
    assert 1.5 <= v < 3.5
    assert v == pytest.approx(2.404759107019637)


@with_import('random_numbers', 'choose_random_element')
def test_Q5_choose_random_element(choose_random_element):
    assert choose_random_element([]) is None
    random.seed(21)
    assert choose_random_element(['a', 'b', 'c', 'd']) == 'b'


@with_import('random_numbers', 'shuffle_list')
def test_Q6_shuffle_list(shuffle_list):
    data = [1, 2, 3, 4, 5, 6]
    data_copy = list(data)
    random.seed(99)
    out = shuffle_list(data)
    assert data == data_copy  # original not mutated
    assert out == [5, 1, 3, 2, 6, 4]


@with_import('random_numbers', 'weighted_choice')
def test_Q7_weighted_choice(weighted_choice):
    with pytest.raises(ValueError):
        weighted_choice([], [])
    with pytest.raises(ValueError):
        weighted_choice([1, 2], [1])
    with pytest.raises(ValueError):
        weighted_choice([1], [-1])
    with pytest.raises(ValueError):
        weighted_choice([1], [0])
    random.seed(42)
    choice = weighted_choice(['a', 'b', 'c'], [1, 3, 6])
    # r = 6.394267984578837 so choice should be 'c'
    assert choice == 'c'


@with_import('random_numbers', 'estimate_pi')
def test_Q8_estimate_pi(estimate_pi):
    with pytest.raises(ValueError):
        estimate_pi(0)
    random.seed(0)
    pi_est = estimate_pi(1000)
    # exact numbers with seed 0: 782 inside => 3.128
    assert pi_est == pytest.approx(3.128, abs=1e-12)
