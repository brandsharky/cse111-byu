from byu_pytest_utils import with_import


@with_import('tuples', 'print_odd_numbers')
def test_Q1_print_odd_numbers(print_odd_numbers, capfd):
    print_odd_numbers((1, 2, 3, 4, 5))
    out, err = capfd.readouterr()
    assert out == "1\n3\n5\n"

    print_odd_numbers((30, 121, 49, 33, 5, 0))
    out, err = capfd.readouterr()
    assert out == "121\n49\n33\n5\n"


@with_import('tuples', 'print_odd_indices')
def test_Q2_print_odd_indices(print_odd_indices, capfd):
    print_odd_indices((1, 2, 3, 4, 5))
    out, err = capfd.readouterr()
    assert out == "2\n4\n"

    print_odd_indices((30, 121, 49, 33, 5, 0))
    out, err = capfd.readouterr()
    assert out == "121\n33\n0\n"


@with_import('tuples', 'coordinates')
def test_Q3_coordinates(coordinates):
    output = coordinates([(1, 2), (1, 4), (3, 6)])
    assert output == ['Point(1, 2)', 'Point(1, 4)', 'Point(3, 6)']
    output = coordinates([(0, 4), (9, 10), (100, 3), (0, 0)])
    assert output == ['Point(0, 4)', 'Point(9, 10)', 'Point(100, 3)', 'Point(0, 0)']


@with_import('tuples', 'tuple_to_dict')
def test_Q4_tuple_to_dict(tuple_to_dict):
    output = tuple_to_dict((('a', 1), ('b', 2), ('c', 3)))
    assert output == {'a': 1, 'b': 2, 'c': 3}
    output = tuple_to_dict(((1, 'adam'), (2, 'sally'), (3, 'hannah'), (4, 'avery'), (5, 'bob')))
    assert output == {1: 'adam', 2: 'sally', 3: 'hannah', 4: 'avery', 5: 'bob'}


@with_import('tuples', 'move')
def test_Q5_move(move):
    assert move((1, 2), 3, 4) == (4, 6)
    assert move ((5, 2), -2, 0) == (3, 2)
