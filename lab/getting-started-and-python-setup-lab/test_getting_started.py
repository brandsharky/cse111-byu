from byu_pytest_utils import with_import, max_score

@with_import("getting_started", "eighteen_seventy_five")
def test_eighteen_seventy_five(eighteen_seventy_five):
    assert eighteen_seventy_five() == 1875
