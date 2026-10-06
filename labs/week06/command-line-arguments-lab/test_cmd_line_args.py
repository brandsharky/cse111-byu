from byu_pytest_utils import dialog, test_files, this_folder, ensure_missing

@dialog(test_files / 'count_1.dialog.txt', 'count.py', 'argument', 8, 'cats', 30)
def test_Q2_count_1():
    ...

@dialog(test_files / 'count_2.dialog.txt', 'count.py')
def test_Q2_count_2():
    ...

@dialog(test_files / 'add.dialog.txt', 'math_args.py', 'add', 1, 5, 10)
def test_Q3_add():
    ...

@dialog(test_files / 'multiply.dialog.txt', 'math_args.py', 'multiply', 1, 5, 10)
def test_Q3_multiply():
    ...

@dialog(test_files / 'no_args.dialog.txt', 'math_args.py')
def test_Q3_no_args():
    ...

@dialog(test_files / 'invalid_command.dialog.txt', 'math_args.py', 'divide')
def test_Q3_invalid_command():
    ...

@dialog(test_files / 'invalid_numbers.dialog.txt', 'math_args.py', 'add', 'number')
def test_Q3_invalid_numbers():
    ...

@dialog(test_files / 'no_numbers.dialog.txt', 'math_args.py', 'multiply')
def test_Q3_no_numbers():
    ...

@dialog(test_files / 'no_flags.dialog.txt', 'flags.py', 'CS', '111', 'Rocks!')
def test_Q4_no_flags():
    ...


@dialog(test_files / 'p_flag.dialog.txt', 'flags.py', '-p', '1', '2', '3')
def test_Q5_p_flag():
    ...


@dialog(test_files / 'i_flag.dialog.txt', 'flags.py', '-i')
def test_Q5_i_flag():
    ...


@dialog(test_files / 'h_flag.dialog.txt', 'flags.py', '-h')
def test_Q5_h_flag():
    ...


@ensure_missing(this_folder / 'w_flag.output.txt')
@dialog(test_files / 'w_flag_with_no_content.dialog.txt', 'flags.py', '-w', 'w_flag.output.txt')
def test_Q6_w_flag_with_no_content():
    ...


@ensure_missing(this_folder / 'w_flag.output.txt')
@dialog(
    test_files / 'w_flag_with_content.dialog.txt',
    'flags.py', '-w', 'w_flag.output.txt', 'a', 'b', 'c', 'd',
    output_file='w_flag.output.txt'
)
def test_Q6_w_flag_with_content():
    ...


@dialog(test_files / 'r_flag.dialog.txt', 'flags.py', '-r', test_files / 'r_flag.input.txt')
def test_Q6_r_flag():
    ...
