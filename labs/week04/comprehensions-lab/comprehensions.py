# Q1
def reverse(lst):
    """
    Takes a list and returns a new list that is the reverse of the original list.
    >>> reverse([1, 2, 3])
    [3, 2, 1]
    >>> reverse(["a", "b", "c", "d"])
    ['d', 'c', 'b', 'a']
    >>> reverse([1])
    [1]
    """
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]


# Q2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return round(celsius, 2)

def convert_provo_highs_to_celsius(lst):
    """
    >>> convert_provo_highs_to_celsius([37, 44, 54, 62, 72, 82, 90, 87, 78, 66, 51, 38])
    [2.78, 6.67, 12.22, 16.67, 22.22, 27.78, 32.22, 30.56, 25.56, 18.89, 10.56, 3.33]
    """
    return [fahrenheit_to_celsius(f) for f in lst]


# Q3
def squares_in_range(start, stop):
    """
    Takes two integers, `start` and `stop` and returns a list of squares for
    all numbers in that range (inclusive).

    >>> squares_in_range(1, 5)
    [1, 4, 9, 16, 25]
    >>> squares_in_range(3, 3)
    [9]
    """
    return [n**2 for n in range(start, stop + 1)]


# Q4
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]


# Q5
def multiples_of_five_comprehension(numbers):
    """
    >>> multiples_of_five_comprehension([1, 5, 15, 60, 30, 2, 4])
    [5, 15, 60, 30]
    """
    return [number for number in numbers if number % 5 == 0]

def multiples_of_five_for_loop(numbers):
    """
    >>> multiples_of_five_for_loop([1, 5, 15, 60, 30, 2, 4])
    [5, 15, 60, 30]
    """
    multiples_of_five = []
    for number in numbers:
        if number % 5 == 0:
            multiples_of_five.append(number)

    return multiples_of_five


# Q6
def list_numbers_double_odds_for_loop(numbers):
    """
    >>> list_numbers_double_odds_for_loop([1, 2, 3, 4, 5])
    [2, 2, 6, 4, 10]
    """
    final_numbers = []
    for number in numbers:
        if number % 2 == 0:
            final_numbers.append(number)
        else:
            final_numbers.append(number * 2)
    return final_numbers

def list_numbers_double_odds_comprehension(numbers):
    """
    >>> list_numbers_double_odds_comprehension([1, 2, 3, 4, 5])
    [2, 2, 6, 4, 10]
    """
    return [number if number % 2 == 0 else number * 2 for number in numbers]


# Q7
def filter_by_value(dictionary, min_value):
    """
    >>> filter_by_value({'hi': 2, 'yo': 4, 'sup': 3, 'greetings': 1}, 3)
    {'yo': 4, 'sup': 3}
    """
    return {key: value for key,value in dictionary.items() if value >= min_value}


# Q8
def list_of_tuples(numbers):
    """
    >>> list_of_tuples([1, 2, 3, 4, 5, 6])
    [(1, 2), (3, 4), (5, 6)]
    >>> list_of_tuples([10, 20, 30])
    [(10, 20), (30, None)]
    """
    return [
        (numbers[i], numbers[i + 1]
        if i + 1 < len(numbers) else None)
        for i in range(0, len(numbers), 2)
    ]



print("Program Initialized")
# print(reverse([1,2,3]))
# print(convert_provo_highs_to_celsius([37, 44, 54, 62, 72, 82, 90, 87, 78, 66, 51, 38]))
# print(squares_in_range(1, 5))
# print(even_weighted([1, 2, 3, 4, 5, 6]))
# print(multiples_of_five_for_loop([1, 5, 15, 60, 30, 2, 4]))
# print(list_numbers_double_odds_comprehension([1, 2, 3, 4, 5]))
# print(filter_by_value({'hi': 2, 'yo': 4, 'sup': 3, 'greetings': 1}, 3))
# print(list_of_tuples([1, 2, 3, 4, 5, 6]))