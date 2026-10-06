from byu_pytest_utils import with_import
import pytest


@with_import('student_grades', 'StudentGrades')
def test_Q2_add_student(StudentGrades, capfd):
    grades = StudentGrades()
    assert len(grades.students) == 0

    grades.add_student("Maya")
    assert len(grades.students) == 1
    assert "Maya" in grades.students.keys()
    assert grades.students["Maya"] == []

    out, err = capfd.readouterr()
    assert out == "Added student: Maya\n"


@with_import('student_grades', 'StudentGrades')
def test_Q2_record_grade(StudentGrades, capfd):
    grades = StudentGrades()
    grades.add_student("Maya")
    out, err = capfd.readouterr()
    grades.add_student("Kyle")
    out, err = capfd.readouterr()

    grades.record_grade("Maya", 88)
    out, err = capfd.readouterr()
    assert out == "Recorded grade 88 for Maya\n"

    grades.record_grade("Maya", 92)
    out, err = capfd.readouterr()
    assert out == "Recorded grade 92 for Maya\n"

    grades.record_grade("Kyle", 83)
    out, err = capfd.readouterr()
    assert out == "Recorded grade 83 for Kyle\n"

    assert grades.students["Maya"] == [88, 92]
    assert grades.students["Kyle"] == [83]


@with_import('student_grades', 'StudentGrades')
def test_Q2_get_average(StudentGrades, capfd):
    grades = StudentGrades()
    grades.add_student("Iris")
    out, err = capfd.readouterr()

    grades.get_average("Iris")
    out, err = capfd.readouterr()
    assert out == "Iris has no grades recorded.\n"

    grades.record_grade("Iris", 50)
    out, err = capfd.readouterr()
    grades.record_grade("Iris", 100)
    out, err = capfd.readouterr()
    grades.record_grade("Iris", 92)
    out, err = capfd.readouterr()
    grades.get_average("Iris")
    out, err = capfd.readouterr()
    assert out == "Iris's average grade is 80.67\n"

    grades.get_average("Lois")
    out, err = capfd.readouterr()
    assert out == "Lois is not in the system.\n"


@with_import('library', 'Library')
@with_import('library', 'Book')
def test_Q3_library_read_and_read_author(Book, Library):
    b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    l = Library([b1, b2, b3])

    assert l.books[0].title == 'A Tale of Two Cities'
    assert l.books[0].author == 'Charles Dickens'
    assert l.read_book(1) == 'The Hobbit has been read 1 time(s)'
    assert l.read_book(3) == None

    tcase1 = l.read_author("Charles Dickens")
    tcase2 = l.read_author("J.R.R. Tolkien")

    assert tcase1.strip() == 'A Tale of Two Cities has been read 1 time(s)'
    assert tcase2.strip() == 'The Hobbit has been read 2 time(s)\nThe Fellowship of the Ring has been read 1 time(s)'

    assert b1.times_read == 1
    assert b2.times_read == 2


@with_import('library', 'Library')
@with_import('library', 'Book')
def test_Q3_library_add_book(Book, Library):
    b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    l = Library([b1, b2])

    b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    l.add_book(b3)
    l.add_book(Book(2, "The Sorcerer's Stone", "J.K. Rowling"))

    assert 0 in l.books.keys() and 1 in l.books.keys()
    assert l.books[0] == b1 and l.books[1] == b2
    assert 2 in l.books.keys()
    assert l.books[2] == b3


@with_import('mascot', 'Mascot')
def test_Q4_do_backflip(Mascot, capfd):
    cosmo = Mascot('Cosmo', 3)
    cosmo.do_backflip()
    out, err = capfd.readouterr()
    assert out == "Great backflip!\n"
    assert cosmo.energy == 2
    assert cosmo.cash == 10

    cosmo.do_backflip()
    out, err = capfd.readouterr()
    assert out == "Too tired :(\n"
    assert cosmo.energy == 2
    assert cosmo.cash == 10


@with_import('mascot', 'Mascot')
def test_Q4_go_to_event(Mascot, capfd):
    cosmo = Mascot('Cosmo', 3)
    assert cosmo.events == []

    cosmo.go_to_event('football')
    out, err = capfd.readouterr()
    assert out == "Went to: football\n"
    cosmo.go_to_event('basketball')
    out, err = capfd.readouterr()
    assert out == "Went to: basketball\n"
    cosmo.go_to_event('orientation')
    out, err = capfd.readouterr()
    cosmo.go_to_event('football again')
    out, err = capfd.readouterr()
    cosmo.go_to_event('ice skating')
    out, err = capfd.readouterr()
    cosmo.go_to_event('pi day')
    out, err = capfd.readouterr()
    assert out == "Went to: pi day\n"
    assert cosmo.events == ['football', 'basketball', 'orientation', 'football again', 'ice skating', 'pi day']

    cosmo.go_to_event('more football')
    out, err = capfd.readouterr()
    assert out == "Been at too many events\n"
    assert cosmo.events == ['football', 'basketball', 'orientation', 'football again', 'ice skating', 'pi day']


@with_import('physics_utils', 'PhysicsUtils')
def test_Q5_physics_utils(PhysicsUtils):
    assert 2.0 == PhysicsUtils.density(10, 5)
    assert 80.0 == PhysicsUtils.density(240, 3)

    assert 8.0 == PhysicsUtils.kinetic_energy(4, 2)
    assert 45.0 == PhysicsUtils.kinetic_energy(10, 3)


@with_import('rectangle', 'Rectangle')
def test_Q6_rectangle_init(Rectangle):
    Rectangle(3, 3.5)
    with pytest.raises(ValueError):
        Rectangle(-2, 5)
        Rectangle(40, -1)


@with_import('rectangle', 'Rectangle')
def test_Q6_rectangle_area(Rectangle):
    rectangle = Rectangle(3, 3)
    assert 9 == rectangle.area()
    rectangle = Rectangle(14, 2)
    assert 28 == rectangle.area()


@with_import('rectangle', 'Rectangle')
def test_Q6_rectangle_is_square(Rectangle):
    rectangle = Rectangle(8, 8)
    assert rectangle.is_square()
    rectangle = Rectangle(2, 100)
    assert not rectangle.is_square()
