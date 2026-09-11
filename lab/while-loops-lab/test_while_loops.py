from byu_pytest_utils import with_import, dialog, this_folder, test_files


@with_import('while_loops', 'print_ten')
def test_Q2_print_ten(print_ten, capsys):
    KEY = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
    print_ten()
    captured = capsys.readouterr()
    observed = captured.out.strip()
    assert observed == KEY


@with_import('while_loops', 'until_thirty')
def test_Q3_until_thirty(until_thirty):
    assert until_thirty(1) == 36
    assert until_thirty(2) == 30
    assert until_thirty(3) == 31
    assert until_thirty(4) == 32
    assert until_thirty(5) == 33
    assert until_thirty(6) == 34
    assert until_thirty(7) == 35


@dialog(test_files / "test_Q4_password_checker.txt", this_folder / "password_checker.py")
def test_Q4_password_checker():
    ...


@dialog(test_files / "test_Q5_shopping_cart.txt", this_folder / "shopping_cart.py")
def test_Q5_shopping_cart():
    ...
