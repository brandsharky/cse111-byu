# Q1
def print_odd_numbers(numbers):
    """
    Print all odd numbers from a tuple of integers.
    >>> print_odd_numbers((1, 2, 3, 4, 5))
    1
    3
    5
    """

    for num in numbers:
        if num % 2 == 1:
            print(num)


# Q2
def print_odd_indices(tple):
    """
    Print elements at odd indices from a tuple.
    >>> print_odd_indices((10, 20, 30, 40, 50))
    20
    40
    """
    for i in range(len(tple)):
        if i % 2 == 1:
            print(tple[i])


# Q3
def coordinates(points):
    """
    Convert a list of tuples into a list of formatted strings.
    >>> coordinates([(1, 2), (1, 4), (3, 6)])
    ['Point(1, 2)', 'Point(3, 4)', 'Point(5, 6)']
    """

    return [f"Point({2 * i + 1}, {y})" for i, (_, y) in enumerate(points)]


# Q4
def tuple_to_dict(tple):
    """
    Convert a tuple of key-value pairs into a dictionary.
    >>> tuple_to_dict((('a', 1), ('b', 2), ('c', 3)))
    {'a': 1, 'b': 2, 'c': 3}
    """

    dct = {}

    for inner_tple in tple:
        dct[inner_tple[0]] = inner_tple[1]

    return dct


# Q5
def move(point, dx, dy):
    """
    Move a point in 2D space by dx and dy.
    >>> move((1, 2), 3, 4)
    (4, 6)
    """

    copied_list = (point[0] + dx, point[1] + dy)
    return tuple(copied_list)



print("Program Initialized")
# print_odd_numbers((1, 2, 3, 4, 5))
# print_odd_indices((10, 20, 30, 40, 50))
# print(coordinates([(1, 2), (1, 4), (3, 6)]))
# print(tuple_to_dict((('a', 1), ('b', 2), ('c', 3))))
# print(move((1, 2), 3, 4))