def count_items(collection):
    """
    Returns the number of items in any collection.

    >>> count_items([1, 2, 3, 4])
    4
    >>> count_items("hello")
    5
    >>> count_items({"a": 1, "b": 2})
    2
    """
    return len(collection)


def sum_all(items, initial_value):
    """
    Sums all items starting with an initial value.

    >>> sum_all([1, 2, 3], 0)
    6
    >>> sum_all(["Hello", " ", "World"], "")
    'Hello World'
    >>> sum_all([[1, 2], [3, 4], [5]], [])
    [1, 2, 3, 4, 5]
    """
    total = initial_value
    for item in items:
        total += item
    return total


def is_valid_age(age):
    """
    Validates age as either an integer or string representation.

    >>> is_valid_age(25)
    True
    >>> is_valid_age("30")
    True
    >>> is_valid_age(150)
    False
    >>> is_valid_age("not a number")
    False
    >>> is_valid_age(-5)
    False
    """
    if isinstance(age, int):
        return 0 <= age <= 120
    elif isinstance(age, str):
        try:
            return 0 <= int(age) <= 120
        except ValueError:
            return False
    return False


def are_equal(val1, val2):
    """
    Compares two values with type coercion for numbers and strings.

    >>> are_equal(5, 5)
    True
    >>> are_equal(5, "5")
    True
    >>> are_equal("10", 10)
    True
    >>> are_equal("hello", "hello")
    True
    >>> are_equal(5, 10)
    False
    """
    if isinstance(val1, str) and isinstance(val2, (int, float)):
        try:
            return float(val1) == val2
        except ValueError:
            return False
    if isinstance(val2, str) and isinstance(val1, (int, float)):
        try:
            return float(val2) == val1
        except ValueError:
            return False
    return val1 == val2


def concat_all(items):
    """
    Concatenates all items, converting numbers to strings.

    >>> concat_all(["Hello", " ", "World"])
    'Hello World'
    >>> concat_all([1, 2, 3])
    '123'
    >>> concat_all(["Number: ", 42, " is the answer"])
    'Number: 42 is the answer'
    """
    return "".join(str(item) for item in items)


def contains_item(container, item):
    """
    Checks if an item exists in various container types.

    >>> contains_item([1, 2, 3], 2)
    True
    >>> contains_item("hello", "e")
    True
    >>> contains_item({"a": 1, "b": 2}, "a")
    True
    >>> contains_item({1, 2, 3}, 4)
    False
    """
    return item in container


def format_output(value):
    """
    Formats different types of values for display.

    >>> format_output(3.14159)
    '3.14'
    >>> format_output("hello world")
    'Hello world'
    >>> format_output([1, 2, 3])
    '1, 2, 3'
    >>> format_output({"name": "Alice", "age": 30})
    'name: Alice, age: 30'
    """
    if isinstance(value, (int, float)):
        return f"{value:.2f}"
    if isinstance(value, str):
        return value.capitalize()
    if isinstance(value, (list, tuple)):
        return ", ".join(str(item) for item in value)
    if isinstance(value, dict):
        return ", ".join(f"{key}: {val}" for key, val in value.items())


def reverse_it(collection):
    """
    Reverses any collection type.

    >>> reverse_it("hello")
    'olleh'
    >>> reverse_it([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse_it((10, 20, 30))
    (30, 20, 10)
    """
    return collection[::-1]


def calculate(val1, val2, operation):
    """
    Performs polymorphic operations on values.

    >>> calculate(5, 3, "add")
    8
    >>> calculate("Hello", "World", "add")
    'HelloWorld'
    >>> calculate(4, 5, "multiply")
    20
    >>> calculate("Hi", 3, "multiply")
    'HiHiHi'
    >>> calculate([1, 2], 2, "multiply")
    [1, 2, 1, 2]
    >>> calculate("Go", 4, "repeat")
    'GoGoGoGo'
    >>> calculate([1], 3, "repeat")
    [1, 1, 1]
    """
    if operation == "add":
        return val1 + val2
    if operation == "multiply":
        return val1 * val2
    if operation == "repeat":
        if not isinstance(val2, int):
            raise ValueError("The second value must be an int")
        return val1 * val2
    raise ValueError(f"Unknown operation: {operation}")