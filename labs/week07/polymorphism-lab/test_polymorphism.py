from byu_pytest_utils import with_import


@with_import('polymorphism', 'count_items')
def test_Q2_count_items(count_items):
    """Test the generic count_items function."""
    # Test with list
    assert count_items([1, 2, 3, 4]) == 4
    assert count_items([]) == 0

    # Test with string
    assert count_items("hello") == 5
    assert count_items("") == 0

    # Test with dictionary
    assert count_items({"a": 1, "b": 2}) == 2
    assert count_items({}) == 0

    # Test with tuple
    assert count_items((10, 20, 30)) == 3
    assert count_items(()) == 0


@with_import('polymorphism', 'sum_all')
def test_Q3_sum_all(sum_all):
    """Test the polymorphic sum_all function."""
    # Test with numbers
    assert sum_all([1, 2, 3], 0) == 6
    assert sum_all([5, 10, 15], 0) == 30
    assert sum_all([1.5, 2.5], 0) == 4.0

    # Test with strings
    assert sum_all(["Hello", " ", "World"], "") == "Hello World"
    assert sum_all(["a", "b", "c"], "") == "abc"

    # Test with lists
    assert sum_all([[1, 2], [3, 4], [5]], []) == [1, 2, 3, 4, 5]
    assert sum_all([[1], [2]], []) == [1, 2]


@with_import('polymorphism', 'is_valid_age')
def test_Q4_is_valid_age(is_valid_age):
    """Test type dispatching with age validation."""
    # Valid integer ages
    assert is_valid_age(0) == True
    assert is_valid_age(25) == True
    assert is_valid_age(120) == True

    # Invalid integer ages
    assert is_valid_age(-1) == False
    assert is_valid_age(-5) == False
    assert is_valid_age(121) == False
    assert is_valid_age(150) == False

    # Valid string ages
    assert is_valid_age("0") == True
    assert is_valid_age("30") == True
    assert is_valid_age("120") == True

    # Invalid string ages
    assert is_valid_age("-5") == False
    assert is_valid_age("150") == False
    assert is_valid_age("not a number") == False
    assert is_valid_age("12.5") == False


@with_import('polymorphism', 'are_equal')
def test_Q5_are_equal(are_equal):
    """Test flexible comparison with type coercion."""
    # Same type comparisons
    assert are_equal(5, 5) == True
    assert are_equal("hello", "hello") == True
    assert are_equal(5, 10) == False
    assert are_equal("5", "10") == False

    # Mixed type comparisons (int and str)
    assert are_equal(5, "5") == True
    assert are_equal("10", 10) == True
    assert are_equal(0, "0") == True

    # Float comparisons
    assert are_equal(5.0, 5) == True
    assert are_equal("5.0", 5) == True

    # Non-matching
    assert are_equal("hello", 5) == False
    assert are_equal(5, "hello") == False


@with_import('polymorphism', 'concat_all')
def test_Q6_concat_all(concat_all):
    """Test universal concatenation."""
    # Strings only
    assert concat_all(["Hello", " ", "World"]) == "Hello World"
    assert concat_all(["a", "b", "c"]) == "abc"

    # Numbers only
    assert concat_all([1, 2, 3]) == "123"
    assert concat_all([10, 20, 30]) == "102030"

    # Mixed types
    assert concat_all(["Number: ", 42, " is the answer"]) == "Number: 42 is the answer"
    assert concat_all([1, " plus ", 1, " equals ", 2]) == "1 plus 1 equals 2"

    # Empty list
    assert concat_all([]) == ""


@with_import('polymorphism', 'contains_item')
def test_Q7_contains_item(contains_item):
    """Test container checking across types."""
    # List
    assert contains_item([1, 2, 3], 2) == True
    assert contains_item([1, 2, 3], 4) == False

    # String
    assert contains_item("hello", "e") == True
    assert contains_item("hello", "z") == False

    # Dictionary (checks keys)
    assert contains_item({"a": 1, "b": 2}, "a") == True
    assert contains_item({"a": 1, "b": 2}, "c") == False

    # Set
    assert contains_item({1, 2, 3}, 2) == True
    assert contains_item({1, 2, 3}, 4) == False

    # Tuple
    assert contains_item((10, 20, 30), 20) == True
    assert contains_item((10, 20, 30), 40) == False


@with_import('polymorphism', 'format_output')
def test_Q8_format_output(format_output):
    """Test flexible formatting."""
    # Numbers
    assert format_output(3.14159) == "3.14"
    assert format_output(5) == "5.00"
    assert format_output(10.5) == "10.50"

    # Strings
    assert format_output("hello world") == "Hello world"
    assert format_output("HELLO") == "Hello"
    assert format_output("test") == "Test"

    # Lists
    assert format_output([1, 2, 3]) == "1, 2, 3"
    assert format_output(["a", "b", "c"]) == "a, b, c"

    # Tuples
    assert format_output((1, 2, 3)) == "1, 2, 3"

    # Dictionaries - order may vary, so check both possibilities
    result = format_output({"name": "Alice", "age": 30})
    assert result in ["name: Alice, age: 30", "age: 30, name: Alice"]


@with_import('polymorphism', 'reverse_it')
def test_Q9_reverse_it(reverse_it):
    """Test generic reversal."""
    # Strings
    assert reverse_it("hello") == "olleh"
    assert reverse_it("Python") == "nohtyP"
    assert reverse_it("") == ""

    # Lists
    assert reverse_it([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_it(["a", "b", "c"]) == ["c", "b", "a"]
    assert reverse_it([]) == []

    # Tuples
    assert reverse_it((10, 20, 30)) == (30, 20, 10)
    assert reverse_it((1,)) == (1,)
    assert reverse_it(()) == ()


@with_import('polymorphism', 'calculate')
def test_Q10_calculate(calculate):
    """Test polymorphic calculator."""
    # Addition - numbers
    assert calculate(5, 3, "add") == 8
    assert calculate(10, 20, "add") == 30
    assert calculate(1.5, 2.5, "add") == 4.0

    # Addition - strings
    assert calculate("Hello", "World", "add") == "HelloWorld"
    assert calculate("Hi ", "there", "add") == "Hi there"

    # Addition - lists
    assert calculate([1, 2], [3, 4], "add") == [1, 2, 3, 4]

    # Multiplication - numbers
    assert calculate(4, 5, "multiply") == 20
    assert calculate(3, 3, "multiply") == 9

    # Multiplication - strings
    assert calculate("Hi", 3, "multiply") == "HiHiHi"
    assert calculate("Go", 2, "multiply") == "GoGo"

    # Multiplication - lists
    assert calculate([1, 2], 2, "multiply") == [1, 2, 1, 2]
    assert calculate([0], 3, "multiply") == [0, 0, 0]

    # Repeat operation
    assert calculate("Go", 4, "repeat") == "GoGoGoGo"
    assert calculate([1], 3, "repeat") == [1, 1, 1]
    assert calculate("Test", 0, "repeat") == ""
