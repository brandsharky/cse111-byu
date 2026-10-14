"""
Homework 03 - The Grid Class

Brandon Arroyo
October 14, 2026
"""

from copy import deepcopy



class Grid:
    def __init__(self, width, height):
        """
        Create grid `array` width by height. Create a Grid object with
        a width, height, and array. Initially all locations hold None.
        >>> grid = Grid(2, 2)
        >>> grid.array
        [[None, None], [None, None]]
        """
        self.width = width
        self.height = height
        self.array = [[None] * self.width for i in range(self.height)]


    def __eq__(self, other):
        """
        >>> grid1 = Grid.build([[1, 1, 1], [2, 3, 5]])
        >>> grid2 = Grid.build([[1, 1, 1], [2, 3, 5]])
        >>> grid_lst = [[1, 1, 1], [2, 3, 5]]
        >>> grid1 == grid2
        True
        >>> grid1 == grid_lst
        True
        """
        if isinstance(other, Grid):
            return self.array == other.array
        else:
            return self.array == other


    def __str__(self):
        """
        >>> print(Grid(6, 2))
        Grid(6, 2, first = None)
        """
        return f"Grid({self.width}, {self.height}, first = {self.get(0, 0)})"


    def __repr__(self):
        """
        >>> repr(Grid.build([[5, 5], [3, 2]]))
        'Grid.build([[5, 5], [3, 2]])'
        """
        return f"Grid.build({self.array})"


    def in_bounds(self, x, y):
        """
        Returns True if (x, y) is in bounds
        >>> grid = Grid(3, 4)
        >>> grid.in_bounds(0, 0)
        True
        >>> grid.in_bounds(2, 3)
        True
        >>> grid.in_bounds(-1, -1)
        False
        >>> grid.in_bounds(3, 4)
        False
        """
        return 0 <= x < self.width and 0 <= y < self.height


    def _check_in_bounds(self, x, y):
        """
        Raises and IndexError if (x, y) is out of bounds.
        """
        if not self.in_bounds(x, y):
            raise IndexError(f"({x}, {y}) is out of bounds.")


    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        >>> grid = Grid(2,2)
        >>> grid.array = [[1, 2], [4, 5]]
        >>> grid.get(0, 1)
        4
        >>> grid.get(1, 0)
        2
        """
        self._check_in_bounds(x, y)
        return self.array[y][x]


    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        >>> grid = Grid(2, 2)
        >>> grid.set(1, 1, "Milk")
        >>> grid.set(1, 0, "Dud")
        >>> grid.array
        [[None, 'Dud'], [None, 'Milk']]
        """
        self._check_in_bounds(x, y)
        self.array[y][x] = val
        return None


    @staticmethod
    def check_list_malformed(lst):
        """
        Given a list that represents a 2D nested Grid, check that it has the
        right shape. Raise a ValueError if it is malformed.
        >>> Grid.check_list_malformed([[1, 2], [4, 5]])
        >>> Grid.check_list_malformed(1)
        Traceback (most recent call last):
        ...
        ValueError: Input must be a non-empty list of lists.
        >>> Grid.check_list_malformed([[1, 2], [4, 5, 6]])
        Traceback (most recent call last):
        ...
        ValueError: All items in list must be lists of the same length.
        >>> Grid.check_list_malformed([[1, 2], 3])
        Traceback (most recent call last):
        ...
        ValueError: Input must be a list of lists.
        """
        if not isinstance(lst, list) or not lst:
            raise ValueError("Input must be a non-empty list of lists.")

        for item in lst:
            if not isinstance(item, list):
                raise ValueError("Input must be a list of lists.")

        lengths = {len(row) for row in lst}
        if len(lengths) > 1:
            raise ValueError("All items in list must be lists of the same length.")


    @staticmethod
    def build(lst):
        """
        Given a list that represents a 2D nested Grid construct a Grid object.
        Grid.build([[1, 2, 3], [4, 5, 6]])
        >>> Grid.build([[1, 2, 3], [4, 5, 6]]).array
        [[1, 2, 3], [4, 5, 6]]
        """
        Grid.check_list_malformed(lst)
        grid = Grid(len(lst[0]), len(lst))
        grid.array = deepcopy(lst)
        return grid


    def copy(self):
        """
        Returns a Grid that is completely independent of the this one.
        >>> grid = Grid.build([[1, 2], [3, 4]])
        >>> grid_copy = grid.copy()
        >>> grid_copy.set(0, 0, 99)
        >>> grid.get(0, 0)
        1
        >>> grid_copy.get(0, 0)
        99
        """
        return Grid.build(self.array)


