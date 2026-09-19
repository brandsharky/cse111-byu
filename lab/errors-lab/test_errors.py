from byu_pytest_utils import with_import, dialog, this_folder, test_files
import pytest


@with_import('errors', 'add_one_exception_handler')
def test_Q1_add_one_exception_handler(add_one_exception_handler):
    add_one_exception_handler()


@with_import('errors', 'validate_input')
def test_Q2_validate_input(validate_input):
    validate_input("1 call_this")
    validate_input("2")
    validate_input("exit")
    with pytest.raises(ValueError):
        validate_input("1")
        pytest.fail("validate_input('1') didn't raise an exception")
    with pytest.raises(ValueError):
        validate_input("1 this that")
        pytest.fail("validate_input('1 this that') didn't raise an exception")
    with pytest.raises(ValueError):
        validate_input("2 hello")
        pytest.fail("validate_input('2 hello') didn't raise an exception")
    with pytest.raises(ValueError):
        validate_input("3")
        pytest.fail("validate_input('3') didn't raise an exception")
    with pytest.raises(ValueError):
        validate_input("invalid input")
        pytest.fail("validate_input('invalid input') didn't raise an exception")


@with_import('errors', 'exception_handler')
def test_Q3_exception_handler(exception_handler, capsys):
    exception_handler()
    captured = capsys.readouterr()
    observed = captured.out.strip()
    assert "<class 'TypeError'>" in observed


@with_import('errors', 'in_range1')
def test_Q4_in_range1(in_range1):
    assert in_range1(9)
    assert not in_range1(-4)
    assert not in_range1(103)


@with_import('errors', 'in_range2')
def test_Q4_in_range2(in_range2):
    in_range2(9)
    with pytest.raises(ValueError):
        in_range2(-4)
        pytest.fail("in_range2(-4) didn't raise an exception")

    with pytest.raises(ValueError):
        in_range2(103)
        pytest.fail("in_range2(103) didn't raise an exception")


@with_import('errors', 'main')
def test_Q4_main_loop(main, monkeypatch):
    call_count = 0

    def mock_randint(a, b):
        nonlocal call_count
        call_count += 1
        return 1

    monkeypatch.setattr('random.randint', mock_randint)
    main()
    assert call_count == 1000, f"Expected 1000 random calls, got {call_count}"


@with_import('errors', 'bound_checker')
def test_Q5_bound_checker(bound_checker):
    assert bound_checker(10, 12, 2, 3)
    with pytest.raises(IndexError):
        bound_checker(10, 12, 59, 3)
        pytest.fail("bound_checker(10, 12, 59, 3) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 2, 13)
        pytest.fail("bound_checker(10, 12, 2, 13) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, -1, 3)
        pytest.fail("bound_checker(10, 12, -1, 3) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 2, -1)
        pytest.fail("bound_checker(10, 12, 2, -1) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 10, 12)
        pytest.fail("bound_checker(10, 12, 10, 12) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 10, 0)
        pytest.fail("bound_checker(10, 12, 10, 0) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 0, 12)
        pytest.fail("bound_checker(10, 12, 0, 12) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 11, 0)
        pytest.fail("bound_checker(10, 12, 11, 0) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 0, 13)
        pytest.fail("bound_checker(10, 12, 0, 13) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 11, 13)
        pytest.fail("bound_checker(10, 12, 11, 13) didn't raise an exception")


@with_import('age', 'validate_age')
def test_Q6_validate_age(validate_age):
    assert validate_age(123) == 123
    assert validate_age("12") == 12
    assert validate_age("0") == 0
    with pytest.raises(ValueError):
        validate_age("not an age")
        pytest.fail("validate_age('not an age') didn't raise an exception")
    with pytest.raises(ValueError):
        validate_age(124)
        pytest.fail("validate_age(124) didn't raise an exception")
    with pytest.raises(ValueError):
        validate_age("-1")
        pytest.fail("validate_age('-1') didn't raise an exception")


@dialog(test_files / "test_Q6_handle_user_input_valid.dialog.txt", this_folder / "age.py")
def test_Q6_handle_user_input_valid():
    ...


@dialog(test_files / "test_Q6_handle_user_input_invalid.dialog.txt", this_folder / "age.py")
def test_Q6_handle_user_input_invalid():
    ...
