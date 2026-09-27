import doctest
import inspect
from collections.abc import Callable
import textwrap
from byu_pytest_utils import with_import


def run_docstring_tests(func: Callable, exp_num: int = 0) -> None:
    """
    Runs the doctests on `func` with an optional required number of tests
    expressed by the `exp_num` parameter.
    """
    doc = inspect.getdoc(func)
    assert doc
    parser = doctest.DocTestParser()
    glob = {func.__name__: func}
    tests = parser.get_doctest(doc, glob, func.__name__, None, None)
    assert len(tests.examples) >= exp_num, f'Did not find at least {exp_num} doctest examples'

    runner = doctest.DocTestRunner()
    runner.run(tests)
    results = runner.summarize()

    assert results.failed == 0, f'Doctests failed: {results.failed}'


@with_import('code_practice', 'reverse_string')
def test_Q1_reverse_string(reverse_string):
    assert reverse_string("nohtyp") == "python"
    assert reverse_string("hi students") == "stneduts ih"

    run_docstring_tests(reverse_string)


@with_import('code_practice', 'fahrenheit_to_celsius')
def test_Q2_fahrenheit_to_celsius(fahrenheit_to_celsius):
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(95) == 35

    run_docstring_tests(fahrenheit_to_celsius)


@with_import('code_practice', 'count_vowels')
def test_Q3_count_vowels(count_vowels):
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou AEIOU") == 10

    run_docstring_tests(count_vowels, 4)


@with_import('code_practice', 'unique_words')
def test_Q4_unique_words(unique_words):
    output = unique_words('the lion can fly now')
    assert output == ['the', 'lion', 'can', 'fly', 'now']
    output = unique_words('The cat sat on the mat. Then the cat slept.')
    assert output == ['the', 'cat', 'sat', 'on', 'mat', 'then', 'slept']

    run_docstring_tests(unique_words, 3)


@with_import('code_practice', 'print_quotes')
def test_Q5_print_quotes(print_quotes, capfd):
    KEY = textwrap.dedent('''
        "Faith is not to have a perfect knowledge of things; therefore if ye have faith ye hope for things which are not seen, which are true."
        "Choose with care the words you speak and the messages you send."
        "True disciples are doers of the word."
        "Love is the greatest of all virtues."
        ''').lstrip('\n')
    print_quotes('test_files/quotes.txt')
    out, _ = capfd.readouterr()
    assert out == KEY

    run_docstring_tests(print_quotes, 2)
