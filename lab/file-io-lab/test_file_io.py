from byu_pytest_utils import test_files, this_folder, with_import, ensure_missing, dialog
import textwrap
from pathlib import Path

@with_import('file_io', 'count_lines')
def test_Q1_count_lines(count_lines):
    output = count_lines(test_files / 'text.txt')
    assert output == 3
    output = count_lines(test_files / 'python.txt')
    assert output == 10


@with_import('file_io', 'write_n_times')
@ensure_missing(this_folder / 'output.txt')
def test_Q2_write_n_times(write_n_times):
    text = "Python is cool!"
    KEY = textwrap.dedent("""
        Python is cool!
        Python is cool!
        Python is cool!
        Python is cool!
        Python is cool!
        Python is cool!
        """).lstrip('\n')

    write_n_times(this_folder / 'output.txt', text, 6)
    with open(this_folder / 'output.txt', 'r') as file:
        assert file.read() == KEY
    Path.unlink(this_folder / 'output.txt', missing_ok=True)


@ensure_missing(this_folder / 'favorites.txt')
@dialog(test_files / 'test_Q3_favorite_movies.dialog.txt', this_folder / 'favorites.py')
def test_Q3_favorite_movies():
    KEY = textwrap.dedent("""
        Interstellar
        The Lion King
        Wicked
        Spirited Away
        Howl's Moving Castle
        """).lstrip('\n')

    with open(this_folder / 'favorites.txt', 'r') as file:
        assert file.read() == KEY
    Path.unlink(this_folder / 'favorites.txt', missing_ok=True)


@with_import('file_io', 'filter_lines')
@ensure_missing(this_folder / 'output.txt')
def test_Q4_filter_lines(filter_lines):
    KEY = textwrap.dedent("""
        Python is a powerful programming language.
        Python supports multiple programming paradigms.
        File I/O is an essential part of many Python programs.
        Python has built-in functions for file operations.
        Practice is key when learning Python!
        """).lstrip('\n')

    filter_lines(test_files / 'python.txt', this_folder / 'output.txt', 'Python')
    with open(this_folder / 'output.txt', 'r') as file:
        assert file.read() == KEY
    Path.unlink(this_folder / 'output.txt', missing_ok=True)


@with_import('file_io', 'copy_file')
@ensure_missing(this_folder / 'output.txt')
def test_Q5_copy_file(copy_file):
    KEY = textwrap.dedent("""
        1: They say you should never eat dirt.
        2: It's not nearly as good as an onion.
        3: It's not as good as the CS pun on my shirt.
        """).lstrip('\n')

    copy_file(test_files / 'text.txt', this_folder / 'output.txt')
    with open(this_folder / 'output.txt', 'r') as fin:
        assert fin.read() == KEY
    Path.unlink(this_folder / 'output.txt', missing_ok=True)


@with_import('file_io', 'reverse_lines')
@ensure_missing(this_folder / 'output.txt')
def test_Q6_reverse_lines(reverse_lines):
    KEY = textwrap.dedent("""
        Hyenas are closely related to cats.
        A cheetah's top speed ranges between 65 and 75 mph.
        Many cat species can purr, including cheetahs, bobcats, and cougars.
        The Florida panther is really a puma. It is the same species as the cougars in the Rocky Mountains.
        The domestic cat (felis catus) is closely related to the African and European wildcats (F. lybica and F. silvestris)
        The roaring cats are in the genus Panthera.
        There are only 4 species of cats that can roar: lions, leopards, jaguars, and tigers.
        The Siberian Tiger is the largest cat species.
        The Rusty-Spotted Cat is the smallest cat species.
        Cats are great.
        """).lstrip('\n')

    reverse_lines(test_files / 'cats.txt', this_folder / 'output.txt')
    with open(this_folder / 'output.txt', 'r') as fin:
        assert fin.read() == KEY
    Path.unlink(this_folder / 'output.txt', missing_ok=True)


@with_import('file_io', 'merge_files')
@ensure_missing(this_folder / "python_cats.txt")
def test_Q7_merge_files_1(merge_files):
    KEY = textwrap.dedent("""
        Python is a powerful programming language.
        Cats are great.
        It is widely used in data science and web development.
        The Rusty-Spotted Cat is the smallest cat species.
        Python supports multiple programming paradigms.
        The Siberian Tiger is the largest cat species.
        File I/O is an essential part of many Python programs.
        There are only 4 species of cats that can roar: lions, leopards, jaguars, and tigers.
        Reading and writing files is easy with the 'with open' syntax.
        The roaring cats are in the genus Panthera.
        Python has built-in functions for file operations.
        The domestic cat (felis catus) is closely related to the African and European wildcats (F. lybica and F. silvestris)
        You can read a file line by line using a loop.
        The Florida panther is really a puma. It is the same species as the cougars in the Rocky Mountains.
        Writing to a file will overwrite its contents unless you append.
        Many cat species can purr, including cheetahs, bobcats, and cougars.
        Always close your files or use 'with' to handle it automatically.
        A cheetah's top speed ranges between 65 and 75 mph.
        Practice is key when learning Python!
        Hyenas are closely related to cats.
        """).lstrip('\n')

    merge_files(test_files / "python.txt", test_files / "cats.txt", this_folder / "python_cats.txt")
    with open(this_folder / 'python_cats.txt', 'r') as fin:
        assert fin.read() == KEY
    Path.unlink(this_folder / 'python_cats.txt', missing_ok=True)


@with_import('file_io', 'merge_files')
@ensure_missing(this_folder / "cats_text.txt")
def test_Q7_merge_files_2(merge_files):
    KEY = textwrap.dedent("""
        Cats are great.
        They say you should never eat dirt.
        The Rusty-Spotted Cat is the smallest cat species.
        It's not nearly as good as an onion.
        The Siberian Tiger is the largest cat species.
        It's not as good as the CS pun on my shirt.
        There are only 4 species of cats that can roar: lions, leopards, jaguars, and tigers.
        The roaring cats are in the genus Panthera.
        The domestic cat (felis catus) is closely related to the African and European wildcats (F. lybica and F. silvestris)
        The Florida panther is really a puma. It is the same species as the cougars in the Rocky Mountains.
        Many cat species can purr, including cheetahs, bobcats, and cougars.
        A cheetah's top speed ranges between 65 and 75 mph.
        Hyenas are closely related to cats.
        """).lstrip('\n')

    merge_files(test_files / "cats.txt", test_files / "text.txt", this_folder / "cats_text.txt")
    with open(this_folder / 'cats_text.txt', 'r') as fin:
        assert fin.read() == KEY
    Path.unlink(this_folder / 'cats_text.txt', missing_ok=True)
