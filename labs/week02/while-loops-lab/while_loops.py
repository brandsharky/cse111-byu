def print_ten():
    n = 1
    while n <= 10:
        print(n)
        n += 1


def until_thirty(number):
    """
    >>> until_thirty(3)
    31
    >>> until_thirty(6)
    34
    """
    while number <= 30:
        number += 7

    print(number)


def shopping_cart():
    """*** YOUR CODE HERE ***"""
    """ Code in shopping_cart.py """


if __name__ == "__main__":
    print_ten()
    until_thirty(3)
    until_thirty(6)