def find_first_negative(numbers):
    """
    Given a list of numbers, this function should return the first negative number appearing in the list.
    If the list contains no negative numbers, the function returns None
    >>> find_first_negative([6, 200, -1, -20])
    -1
    >>> find_first_negative([1, 400, 500])
    None
    >>> find_first_negative([-5, 2, -3, -1])
    -5
    """

    i = 0
    while i < len(numbers):
        num = numbers[i]
        if num < 0:
            return num
        i += 1

    return None


def flatten_list(lst):
    """
    This function takes a list of lists and returns a single list that contains all the elements of the original lists.
    >>> flatten_list([[1, 2], [3, 4], [5]])
    [1, 2, 3, 4, 5]
    >>> flatten_list([["a", "b"], "c", "d"])
    ['a', 'b', 'c', 'd']
    >>> flatten_list([1, [5, 2], 8])
    [1, 5, 2, 8]
    """

    flat_list = []

    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            for j in lst[i]:
                flat_list.append(j)
        else:
            flat_list.append(lst[i])

        i += 1

    return flat_list


def filter_less_than(lst, n):
    """
    Returns a list of all the numbers from lst that are less than n.
    >>> filter_less_than([1, 2, 3, 4, 5], 3)
    [1, 2]
    >>> filter_less_than([40, 20, 34, 40, 25, 19, 24], 25)
    [20, 19, 24]
    """

    return list(filter(lambda item: item < n, lst))


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """

    even_list = []

    i = 0
    while i < len(s):
        if i % 2 == 0:
            even_list.append(s[i] * i)
        i += 1

    return even_list


def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """

    assert len(s) == len(t)

    couples = []

    i = 0
    while i < len(s):
        couples.append([s[i], t[i]])
        i += 1

    return couples


def combine_lists(lstA, lstB):
    """
    Returns a sorted list of the combined elements of lstA and lstB, with the duplicates removed.
    >>> lstA = [1, 4, 2]
    >>> lstB = [2, 8, 3]
    >>> combine_lists(lstA, lstB)
    [1, 2, 3, 4, 8]
    """

    combined = []

    for item in lstA + lstB:
        if item not in combined:
            combined.append(item)

    return sorted(combined)


def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """

    factors = []

    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    return factors



# print(find_first_negative([5, 2, 3, -1]))
# print(flatten_list([1, [5, 2], 8]))
# print(filter_less_than([40, 20, 34, 40, 25, 19, 24], 25))
# print(even_weighted([1, 2, 3, 4, 5, 6]))
# print(couple([1, 2, 3], [4, 5, 6]))
# print(couple(['c', 6], ['s', '1']))
# print(combine_lists([1, 4, 2], [2, 8, 3]))
# print(factors_list(73))