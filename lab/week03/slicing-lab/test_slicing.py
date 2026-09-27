from byu_pytest_utils import with_import

@with_import('slicing', 'drop_ends')
def test_Q2_drop_ends(drop_ends):
    assert drop_ends([1, 2, 3, 4, 5], 1) == [2, 3, 4]
    assert drop_ends([10, 20, 30, 40, 50, 60], 2) == [30, 40]
    assert drop_ends([1, 2], 1) == []


@with_import('slicing', 'extract_edges')
def test_Q3_extract_edges(extract_edges):
    assert extract_edges([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 5, 6, 7]
    assert extract_edges([10, 20, 30]) == [10, 20, 30]
    assert extract_edges([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert extract_edges([]) == []


@with_import('slicing', 'reverse_in_groups')
def test_Q4_reverse_in_groups(reverse_in_groups):
    assert reverse_in_groups([0, 1, 2, 3, 4, 5], 3) == [2, 1, 0, 5, 4, 3]
    assert reverse_in_groups([1, 2, 3, 4], 2) == [2, 1, 4, 3]
    assert reverse_in_groups([1, 2, 3], 1) == [1, 2, 3]
    assert reverse_in_groups([], 2) == []


@with_import('slicing', 'pig_latin')
def test_Q5_pig_latin(pig_latin):
    assert pig_latin("apple banana") == "appleyay ananabay"
    assert pig_latin("dog cat") == "ogday atcay"
    assert pig_latin("eat your greens") == "eatyay youryay reensgay"


@with_import('slicing', 'pig_latin_to_english')
def test_Q6_pig_latin_to_english(pig_latin_to_english):
    assert pig_latin_to_english("appleyay ananabay") == "apple banana"
    assert pig_latin_to_english("ogday atcay") == "dog cat"
    assert pig_latin_to_english("eatyay youryay reensgay") == "eat your greens"
    assert pig_latin_to_english("odingcay isyay osay uchmay unfay") == "coding is so much fun"
