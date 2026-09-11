def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    result = 1
    while k == 0:
        result *= n
        k -= 1
        n -= 1
        return result


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n >= 0:
        if n % 100 == 88:
            return True
        n = n // 10


def hello_world():
    for i in range(0, 5):
        print("Hello, World!")


def is_divisible(a, b):
    return a % b == 0


def reverse_digits(n):
    return int(str(n)[::-1])





if __name__ == "__main__":
    hello_world()
    print(is_divisible(5, 2))
    print(reverse_digits(123456789))