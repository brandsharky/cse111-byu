from byu_pytest_utils import with_import, tier
import pytest


core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)


@core
@with_import('Grid', 'Grid')
def test_CORE_check_list_malformed(Grid):
    with pytest.raises(ValueError):
        Grid.check_list_malformed(None)
        pytest.fail(
            f"Grid.check_list_malformed(None) didn't raise an exception")

    with pytest.raises(ValueError):
        Grid.check_list_malformed(1)
        pytest.fail(f"Grid.check_list_malformed(1) didn't raise an exception")

    with pytest.raises(ValueError):
        Grid.check_list_malformed('string')
        pytest.fail(
            f"Grid.check_list_malformed('string') didn't raise an exception")

    with pytest.raises(ValueError):
        Grid.check_list_malformed([])
        pytest.fail(f"Grid.check_list_malformed([]) didn't raise an exception")

    with pytest.raises(ValueError):
        Grid.check_list_malformed([1, 2])
        pytest.fail(
            f"Grid.check_list_malformed([1, 2]) didn't raise an exception")

    with pytest.raises(ValueError):
        Grid.check_list_malformed([['a', 'list'], 'not a list'])
        pytest.fail(
            f"Grid.check_list_malformed([['a', 'list'], 'not a list']) didn't raise an exception")

    with pytest.raises(ValueError):
        Grid.check_list_malformed([[1, 2, 3], [4, 5]])
        pytest.fail(
            f"Grid.check_list_malformed([[1, 2, 3], [4, 5]]) didn't raise an exception")

    Grid.check_list_malformed([[1, 2, 3], [4, 5, 6]])


@core
@with_import('Grid', 'Grid')
def test_CORE_build(Grid):
    lst = [[(x, y) for x in range(4)] for y in range(3)]
    grid = Grid.build(lst)

    assert grid.width == 4
    assert grid.height == 3
    for y in range(3):
        for x in range(4):
            assert grid.get(x, y) == (x, y)


@core
@with_import('Grid', 'Grid')
def test_CORE_get_and_set_in_bounds(Grid):
    grid = Grid(3, 4)

    for y in range(4):
        for x in range(3):
            grid.set(x, y, (x, y))

    for y in range(4):
        for x in range(3):
            assert grid.get(x, y) == (x, y)


@core
@with_import('Grid', 'Grid')
def test_CORE_grid_in_bounds_function(Grid):
    grid = Grid(3, 3)
    for y in range(3):
        for x in range(3):
            assert grid.in_bounds(x, y) == True

    for y in range(-1, 4):
        assert grid.in_bounds(-1, y) == False, f"grid.in_bounds(-1, {y}) returned True when it was out of bounds"
        assert grid.in_bounds(3, y) == False, f"grid.in_bounds(3, {y}) returned True when it was out of bounds"

    for x in range(-1, 4):
        assert grid.in_bounds(x, -1) == False, f"grid.in_bounds({x}, -1) returned True when it was out of bounds"
        assert grid.in_bounds(x, 3) == False, f"grid.in_bounds({x}, 3) returned True when it was out of bounds"


@core
@with_import('Grid', 'Grid')
def test_CORE_get_set_out_of_bounds(Grid):
    grid = Grid(3, 3)
    for y in range(3):
        for x in range(3):
            grid.get(x, y)
            grid.set(x, y, None)

    for y in range(-1, 4):
        with pytest.raises(IndexError):
            grid.get(-1, y)
            pytest.fail(f"{grid}.get(-1, {y}) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(-1, y, None)
            pytest.fail(f"{grid}.set(-1, {y}, None) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.get(3, y)
            pytest.fail(f"{grid}.get(3, {y}) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(3, y, None)
            pytest.fail(f"{grid}.set(3, {y}, None) didn't raise an exception")

    for x in range(-1, 4):
        with pytest.raises(IndexError):
            grid.get(x, -1)
            pytest.fail(f"{grid}.get({x}, -1) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(x, -1, None)
            pytest.fail(f"{grid}.set({x}, -1, None) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.get(x, 3)
            pytest.fail(f"{grid}.get({x}, 3) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(x, 3, None)
            pytest.fail(f"{grid}.set({x}, 3, None) didn't raise an exception")


@advanced
@with_import('Grid', 'Grid')
def test_ADVANCED_copy(Grid):
    lst = [[(x, y) for x in range(4)] for y in range(3)]
    grid = Grid.build(lst)
    copy = grid.copy()

    # makes sure that a deep copy was made
    for y in range(3):
        for x in range(4):
            grid.set(x, y, None)

    assert copy.width == 4
    assert copy.height == 3
    for y in range(3):
        for x in range(4):
            assert copy.get(x, y) == (x, y)


@advanced
@with_import('Grid', 'Grid')
def test_ADVANCED_eq(Grid):
    grid1 = Grid.build([[1, 1, 1], [2, 3, 5], [1, 1, 1], [1, 4, 2]])
    grid2 = Grid.build([[1, 1, 1, 2], [3, 5, 1, 1], [1, 1, 4, 2]])
    grid3 = Grid.build([[5, 2, 3], [3, 4, 1], [1, 2, 4], [3, 4, 2]])
    grid4 = Grid.build([[1, 1, 1], [2, 3, 5], [1, 1, 1], [1, 4, 2]])
    grid5 = [[1, 1, 1, 2], [3, 5, 1, 1], [1, 1, 4, 2]]
    grid6 = [[1, 1, 1], [2, 3, 5], [1, 1, 1], [1, 4, 2]]
    grid7 = Grid.build([[1, 1, 1], [2, 3, 5]])
    grid8 = Grid.build([[5, 5, 2], [4, 1, 5]])
    grid9 = [[1, 1, 1], [2, 3, 5]]

    assert grid1 != None
    assert grid1 != 1
    assert grid1 != 'string'

    assert grid1 != grid2
    assert grid1 != grid3
    assert grid1 == grid4
    assert grid1 != grid5
    assert grid1 == grid6
    assert grid1 != grid7
    assert grid1 != grid8
    assert grid1 != grid9

    assert grid2 != grid3
    assert grid2 != grid4
    assert grid2 == grid5
    assert grid2 != grid6
    assert grid2 != grid7
    assert grid2 != grid8
    assert grid2 != grid9

    assert grid3 != grid4
    assert grid3 != grid5
    assert grid3 != grid6
    assert grid3 != grid7
    assert grid3 != grid8
    assert grid3 != grid9

    assert grid4 != grid5
    assert grid4 == grid6
    assert grid4 != grid7
    assert grid4 != grid8
    assert grid4 != grid9

    assert grid5 != grid6
    assert grid5 != grid7
    assert grid5 != grid8
    assert grid5 != grid9

    assert grid6 != grid7
    assert grid6 != grid8
    assert grid6 != grid9

    assert grid7 != grid8
    assert grid7 == grid9

    assert grid8 != grid9


@excellent
@with_import('Grid', 'Grid')
def test_EXCELLENT_repr(Grid):
    grid = Grid.build([[5, 4, 3, 3, 4], [4, 1, 5, 2, 2]])
    assert repr(grid) == 'Grid.build([[5, 4, 3, 3, 4], [4, 1, 5, 2, 2]])'

    grid.set(0, 0, 3)
    assert repr(grid) == 'Grid.build([[3, 4, 3, 3, 4], [4, 1, 5, 2, 2]])'

    grid = Grid.build([[5, 5], [3, 2]])
    assert repr(grid) == 'Grid.build([[5, 5], [3, 2]])'


@excellent
@with_import('Grid', 'Grid')
def test_EXCELLENT_str(Grid):
    grid = Grid(6, 2)
    assert str(grid) == 'Grid(6, 2, first = None)'

    grid.set(0, 0, 1)
    assert str(grid) == 'Grid(6, 2, first = 1)'


def class_docstring_test(cls):
    owner = getattr(cls, '__module__', None) or getattr(cls, '__name__', None)
    for func in dir(cls):
        attr = getattr(cls, func)
        if callable(attr) and getattr(attr, '__module__', None) == owner:
            if func.startswith('__') or func == 'main':
                continue
            assert getattr(cls, func).__doc__ is not None, f"{func}() is missing a docstring"


@excellent
@with_import('Grid', 'Grid')
def test_EXCELLENT_docstrings_present(Grid):
    class_docstring_test(Grid)
