from byu_pytest_utils import with_import

@with_import('dictionaries', 'word_count')
def test_word_count(word_count):
    assert word_count("The cat and the dog and the cat") == {
        "the": 3,
        "cat": 2,
        "and": 2,
        "dog": 1
    }
    assert word_count("") == {}
    assert word_count("HELLO hello") == {"hello": 2}


@with_import('dictionaries', 'find_key')
def test_find_key(find_key):
    dictionary = {"a": 1, "b": 2, "c": 1}
    assert sorted(find_key(dictionary, 1)) == ["a", "c"]
    assert find_key(dictionary, 3) == []
    assert find_key({}, 1) == []


@with_import('dictionaries', 'update_inventory')
def test_update_inventory(update_inventory):
    inventory = {"apple": 10, "banana": 5}
    order = {"banana": 3, "apple": 15}
    expected = {"apple": 0, "banana": 2}
    assert update_inventory(inventory.copy(), order) == expected


@with_import('dictionaries', 'filter_by_value')
def test_filter_by_value(filter_by_value):
    d = {"a": 1, "b": 5, "c": 3}
    assert filter_by_value(d, 3) == {"b": 5, "c": 3}
    assert filter_by_value(d, 6) == {}
    assert filter_by_value({}, 1) == {}


@with_import('dictionaries', 'group_by_length')
def test_group_by_length(group_by_length):
    words = ["cat", "snake", "bear", "fish", "lion"]
    result = group_by_length(words)
    expected = {3: ['cat'], 4: ['bear', 'fish', 'lion'], 5: ['snake']}
    assert result == expected
    assert group_by_length([]) == {}
