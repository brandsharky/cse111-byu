from byu_pytest_utils import with_import


@with_import('strings', 'return_poem')
def test_return_poem(return_poem):
    assert return_poem() == "By: Sarah Anderson\nSalty breeze dances,\nWhispering secrets untold,\nOcean’s lullaby."


@with_import('strings', 'quotation')
def test_quotation(quotation):
    assert quotation("Actions speak louder than words") == 'Don\'t forget the saying, "Actions speak louder than words".'
    assert quotation("Carpe diem") == 'Don\'t forget the saying, "Carpe diem".'


@with_import('strings', 'count_words')
def test_count_words(count_words):
    assert count_words("Hello world") == 2
    assert count_words("Python is awesome!") == 3
    assert count_words("   Leading and trailing spaces   ") == 4
    assert count_words("") == 0


@with_import('strings', 'class_list')
def test_class_list(class_list):
    assert class_list(["Math", "Science", "History"]) == "Math\nScience\nHistory"
    assert class_list(["English"]) == "English"
    assert class_list([]) == ""
