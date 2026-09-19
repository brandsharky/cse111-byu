import pytest
from pathlib import Path
from byu_pytest_utils import with_import, run_python_script, this_folder, test_files, ensure_missing, tier
from inspect import getsource
import ast

core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)


@core
@with_import("admissions", "check_row_types")
def test_CORE_check_row_types(check_row_types):
    assert not check_row_types([])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7])
    assert check_row_types([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7, 8])
    assert not check_row_types(["1", "2", "3", "4", "5", "6", "7", "8"])
    assert not check_row_types([""])


@core
@with_import("admissions", "main")
@with_import("admissions", "convert_row_type")
@with_import("admissions", "check_row_types")
def test_CORE_check_row_types_usage(check_row_types, convert_row_type, main):
    module = getsource(main)
    tree = ast.parse(module)
    calls = []
    for func_node in ast.walk(tree):
        if isinstance(func_node, ast.Call) and isinstance(func_node.func, ast.Name):
            calls.append(func_node)
    calls.sort(key=lambda node: (node.lineno, node.col_offset))
    converted = False
    found = False
    for call in calls:
        call_name = call.func.id
        # check_row_types(convert_row_type(row)) is converted-then-checked too,
        # but the outer call sorts first, so catch the nested form directly
        if call_name == check_row_types.__name__ and any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id == convert_row_type.__name__
            for node in ast.walk(call)
        ):
            found = True
        if call_name == convert_row_type.__name__:
            converted = True
        if converted and call_name == check_row_types.__name__:
            found = True
    assert found, (
        "main() must call check_row_types() on a row that has already been "
        "passed through convert_row_type()."
    )


# Run the student file
@pytest.fixture(scope="module")
@ensure_missing(this_folder / "student_scores.csv")
@ensure_missing(this_folder / "chosen_students.csv")
@ensure_missing(this_folder / "outliers.csv")
@ensure_missing(this_folder / "chosen_improved.csv")
@ensure_missing(this_folder / "better_improved.csv")
@ensure_missing(this_folder / "composite_chosen.csv")
def run_program():
    script = this_folder / "admissions.py"
    try:
        run_python_script(script)
    except Exception as e:
        return e


def compare_files(output_file: Path, expected_file: Path):
    try:
        with open(output_file, 'r') as out_file, open(expected_file, 'r') as expect_file:
            assert out_file.read() == expect_file.read(), "Output file does not match expected file"
        output_file.unlink(missing_ok=True)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Couldn't find the output file: {e}")


# Compare the output files to the expected files
@core
def test_CORE_student_scores(run_program):
    if run_program != None: # check to see if the fixture returned any errors before trying to compare files
        raise run_program
    compare_files(this_folder / "student_scores.csv", test_files / "student_scores.key.csv")


@core
def test_CORE_chosen_students(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "chosen_students.csv", test_files / "chosen_students.key.csv")


@core
def test_CORE_outliers(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "outliers.csv", test_files / "outliers.key.csv")


@core
def test_CORE_chosen_improved(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "chosen_improved.csv", test_files / "chosen_improved.key.csv")


@advanced
def test_ADVANCED_better_improved(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "better_improved.csv", test_files / "better_improved.key.csv")


@excellent
def test_EXCELLENT_composite_chosen(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "composite_chosen.csv", test_files / "composite_chosen.key.csv")
