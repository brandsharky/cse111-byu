from byu_pytest_utils import with_import

@with_import('comprehensions', 'reverse')
def test_Q1_reverse(reverse):
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse(["a", "b", "c", "d"]) == ['d', 'c', 'b', 'a']
    assert reverse([1]) == [1]


@with_import('comprehensions', 'convert_provo_highs_to_celsius')
def test_Q2_convert_provo_highs_to_celsius(convert_provo_highs_to_celsius):
    result = convert_provo_highs_to_celsius([37, 44, 54, 62, 72, 82, 90, 87, 78, 66, 51, 38])
    assert result == [2.78, 6.67, 12.22, 16.67, 22.22, 27.78, 32.22, 30.56, 25.56, 18.89, 10.56, 3.33]
    result = convert_provo_highs_to_celsius([32, 50, 27, 25, 100, 26, 47])
    assert result == [0.0, 10.0, -2.78, -3.89, 37.78, -3.33, 8.33]


@with_import('comprehensions', 'squares_in_range')
def test_Q3_squares_in_range(squares_in_range):
    assert squares_in_range(1, 5) == [1, 4, 9, 16, 25]
    assert squares_in_range(3, 3) == [9]
    assert squares_in_range(0, 2) == [0, 1, 4]
    assert squares_in_range(-2, 2) == [4, 1, 0, 1, 4]


@with_import('comprehensions', 'even_weighted')
def test_Q4_even_weighted(even_weighted):
    assert even_weighted([1, 2, 3, 4, 5, 6]) == [0, 6, 20]
    assert even_weighted([9, 17, 4, 5, 4]) == [0, 8, 16]


@with_import('comprehensions', 'multiples_of_five_for_loop')
def test_Q5_multiples_of_five(multiples_of_five_for_loop):
    assert multiples_of_five_for_loop([1, 5, 15, 60, 30, 2, 4]) == [5, 15, 60, 30]
    assert multiples_of_five_for_loop([10, 11, 12, 13, 14, 15, 21, 25, 400, 5000]) == [10, 15, 25, 400, 5000]


@with_import('comprehensions', 'list_numbers_double_odds_comprehension')
def test_Q6_list_numbers_double_odds(list_numbers_double_odds_comprehension):
    assert list_numbers_double_odds_comprehension([1, 2, 3, 4, 5]) == [2, 2, 6, 4, 10]
    assert list_numbers_double_odds_comprehension([2, 4, 6, 7]) == [2, 4, 6, 14]


@with_import("comprehensions", "filter_by_value")
def test_Q7_filter_by_value(filter_by_value):
    d = {"a": 1, "b": 5, "c": 3}
    assert filter_by_value(d, 3) == {"b": 5, "c": 3}
    assert filter_by_value(d, 6) == {}
    assert filter_by_value({}, 1) == {}


@with_import('comprehensions', 'list_of_tuples')
def test_Q8_list_of_tuples(list_of_tuples):
    assert list_of_tuples([1, 2, 3, 4, 5, 6]) == [(1, 2), (3, 4), (5, 6)]
    assert list_of_tuples([10, 20, 30]) == [(10, 20), (30, None)]
    
