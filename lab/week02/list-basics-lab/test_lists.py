from byu_pytest_utils import with_import


@with_import('lists', 'find_first_negative')
def test_Q2_find_first_negative(find_first_negative):
    output = find_first_negative([6, 200, -1, -20])
    assert output == -1
    output = find_first_negative([1, 400, 500])
    assert output == None
    output = find_first_negative([-5, 2, -3, -1])
    assert output == -5


@with_import('lists', 'flatten_list')
def test_Q3_flatten_list(flatten_list):
    output = flatten_list([[1, 2], [3, 4], [5]])
    assert output == [1, 2, 3, 4, 5]
    output = flatten_list([["a", "b"], "c", "d"])
    assert output == ['a', 'b', 'c', 'd']
    output = flatten_list([1, [5, 2], 8])
    assert output == [1, 5, 2, 8]
    output = flatten_list(['tigers', 'lions', 'leopards', 'jaguars'])
    assert output == ['tigers', 'lions', 'leopards', 'jaguars']


@with_import('lists', 'filter_less_than')
def test_Q4_filter_less_than(filter_less_than):
    output = filter_less_than([1, 2, 3, 4, 5], 3)
    assert output == [1, 2]
    output = filter_less_than([40, 20, 34, 40, 25, 19, 24], 25)
    assert output == [20, 19, 24]


@with_import('lists', 'even_weighted')
def test_Q5_even_weighted(even_weighted):
    assert even_weighted([1, 2, 3, 4, 5, 6]) == [0, 6, 20]
    assert even_weighted([9, 17, 4, 5, 4]) == [0, 8, 16]


@with_import('lists', 'couple')
def test_Q6_couple(couple):
    assert couple([1, 2, 3], [4, 5, 6]) == [[1, 4], [2, 5], [3, 6]]
    assert couple(['c', 6], ['s', '1']) == [['c', 's'], [6, '1']]


@with_import('lists', 'combine_lists')
def test_Q7_combine_lists(combine_lists):
    lstA = [1, 4, 2]
    lstB = [2, 8, 3]
    output = combine_lists(lstA, lstB)
    assert output == [1, 2, 3, 4, 8]

    lstA = [4, 3, 2, 1, 10, 145, -43]
    lstB = [4, 3, 2, 1, 10, 145, -43]
    output = combine_lists(lstA, lstB)
    assert output == [-43, 1, 2, 3, 4, 10, 145]

    lstA = [3.45, 2, 10, 4, 0, 12.3]
    lstB = [1]
    output = combine_lists(lstA, lstB)
    assert output == [0, 1, 2, 3.45, 4, 10, 12.3]


@with_import('lists', 'factors_list')
def test_Q8_factors_list(factors_list):
    assert factors_list(3) == [1]
    assert factors_list(4) == [1, 2]
    assert factors_list(9) == [1, 3]
    assert factors_list(10) == [1, 2, 5]
    assert factors_list(12) == [1, 2, 3, 4, 6]
    assert factors_list(16) == [1, 2, 4, 8]
    assert factors_list(17) == [1]
    assert factors_list(18) == [1, 2, 3, 6, 9]
    assert factors_list(20) == [1, 2, 4, 5, 10]