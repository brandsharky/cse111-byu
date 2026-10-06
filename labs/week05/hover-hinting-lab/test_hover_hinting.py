import ast
from inspect import getsource
from pathlib import Path

from byu_pytest_utils import ensure_missing, test_files, this_folder, with_import


def get_func_calls(func):
    module = getsource(func)
    tree = ast.parse(module)
    func_names = []
    for func_node in ast.walk(tree):
        if isinstance(func_node, ast.Call) and isinstance(
            func_node.func, ast.Attribute
        ):
            called_name = func_node.func.attr
            func_names.append(called_name)
    return sorted(func_names)


@with_import("hover_hinting", "find_multiples")
def test_Q1_find_multiples(find_multiples):
    output = find_multiples(4, 7)
    assert output == "The first 7 multiples of 4 are: 4, 8, 12, 16, 20, 24, 28"
    output = find_multiples(1, 10)
    assert output == "The first 10 multiples of 1 are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"


@with_import("hover_hinting", "find_multiples")
def test_Q1_find_multiples_function_usage(find_multiples):
    func_calls = get_func_calls(find_multiples)
    assert func_calls == ["bar", "baz", "foo"]


@with_import("hover_hinting", "repeating_print")
def test_Q2_repeating_print(repeating_print):
    output = repeating_print(["hi", "bye"], [6, 2])
    expected = """Here are all the strings at there appropriate frequencies: 
1. hi hi hi hi hi hi
2. bye bye"""
    assert output == expected
    output = repeating_print(
        ["mother", "father", "childer", "sister", "brother"], [2, 7, 4, 8, 1]
    )
    expected = """Here are all the strings at there appropriate frequencies: 
1. mother mother
2. father father father father father father father
3. childer childer childer childer
4. sister sister sister sister sister sister sister sister
5. brother"""
    assert output == expected


@with_import("hover_hinting", "repeating_print")
def test_Q2_repeating_print_function_usage(repeating_print):
    func_calls = get_func_calls(repeating_print)
    assert func_calls == ["corge", "foo", "qux"]


@with_import("hover_hinting", "str_editor")
@ensure_missing(this_folder / "output1.txt")
def test_Q3_str_editor_1(str_editor):
    str_editor(test_files / "str_editor_1.txt", "e", "output1.txt")
    with open("output1.txt", "r") as output:
        with open(test_files / "key_str_editor_1.txt", "r") as expected:
            assert expected.read() == output.read()
    Path.unlink(this_folder / 'output1.txt', missing_ok=True)


@with_import("hover_hinting", "str_editor")
@ensure_missing(this_folder / "output2.txt")
def test_Q3_str_editor_2(str_editor):
    str_editor(test_files / "str_editor_2.txt", "b", "output2.txt")
    with open("output2.txt", "r") as output:
        with open(test_files / "key_str_editor_2.txt", "r") as expected:
            assert expected.read() == output.read()
    Path.unlink(this_folder / 'output2.txt', missing_ok=True)


@with_import("hover_hinting", "str_editor")
def test_Q3_str_editor_function_usage(str_editor):
    func_calls = get_func_calls(str_editor)
    assert func_calls == ["qux", "thud", "waldo"]
