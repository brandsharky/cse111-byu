import random

# Q1
def add_one(number):
    """
    Returns the input number plus one.
    """
    return number + 1

def add_one_exception_handler():
    """
    This function catches the error from add_one and prints "Can't add 1 to that."
    instead of having the program crash.
    """
    try:
        add_one("apple")
        print("You added 1.")
    except TypeError:
        print("Can't add 1 to that.")



# Q2
def validate_input(user_input):
    input_list = user_input.split()
    if not input_list:
        raise ValueError("Input cannot be empty.")

    command = input_list[0]

    if command not in ["1", "2", "exit"]:
        raise ValueError("The options are 1, 2, or 'exit'")

    if command == "1" and len(input_list) != 2:
        raise ValueError("Option 1 requires one adiitional parameter")

    if command == "2" and len(input_list) != 1:
        raise ValueError("Option 2 takes no additional parameters")



# Q3
def exception_maker():
    raise TypeError

def exception_handler():
    """ Write a function that uses a try-except block to handle an exception.
    If an exception is thrown/raised, then print out something like:
    "Exception caught! Exception type: <<put the type of the exception here>>"
    """
    try:
        exception_maker()
    except Exception as e:
        print(f"Exception caught! Exception type: {type(e)}")



# Q4
def in_range1(n):
    """ Write a function that checks to see if n is
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    >>> in_range1(103)
    False
    """
    return 1 <= n <= 100


def in_range2(n):
    """ Redo in_range1, but instead of returning False, raise a ValueError
    if n is outside the range of 1-100.
    """
    if not (1 <= n <= 100):
        raise ValueError(f"{n} is not in range 1-100")
    return True


def main():
    """ Write code in the main function that generates 1000
    random numbers between 1 and 101 and calls both in_range1
    and in_range2 function to validate the numbers generated using
    both functions.
    """
    for i in range(1, 1001):
        num = random.randint(1, 101)
        print(f"{i}: {num}")

        if not in_range1(num):
            print(f"Failed in in_range1")
        else:
            print("")

        try:
            in_range2(num)
        except ValueError:
            print(f"Failed in in_range2")

        print()



# Q5
def bound_checker(x_dimension, y_dimension, x, y):
    """ If given an x and a y dimension which represent the maximum values on a grid
    (think of a square with dimensions x = 10, y = 12, for example),
    write a function that returns True if the x and y are within the grid,
    and throws an IndexError if they are out of bounds.
    >>> bound_checker(10, 12, 2, 3)
    True
    >>> bound_checker(10, 12, 59, 3)
    Traceback (most recent call last):
        ...
    IndexError
    """
    if (0 <= x <= x_dimension) and (0 <= y <= y_dimension):
        return True
    else:
        raise IndexError("Coordinates out of range.")









# add_one_exception_handler()
# validate_input("1 2")
# exception_handler()
# print(in_range1(100))
# print(in_range2(-4))
# main()
# print(bound_checker(10, 12, 59, 3))