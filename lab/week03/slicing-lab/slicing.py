def drop_ends(lst, n):
    """
    Takes a list (`lst`) and a number (`n`) and returns a list with the same
    elements as the given list except without the first and and last `n`
    elements.

    >>> drop_ends([0, 1, 2, 3, 4, 5, 6], 2)
    [2, 3, 4]
    >>> drop_ends(['a', 'b', 'c', 'd', 'e'], 1)
    ['b', 'c', 'd']
    """
    return lst[0+n:-n]


def extract_edges(lst):
    """
    Takes a list and returns a new list containing the first three and last
    three elements. If the list has fewer than six elements, return the whole
    list unchanged.

    >>> extract_edges([1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 6, 7, 8]
    >>> extract_edges([10, 20, 30])
    [10, 20, 30]
    """
    if len(lst) > 6:
        front = lst[:3]
        back = lst[-3:]

        return front + back
    return lst


def reverse_in_groups(lst, n):
    """
    Takes a list (`lst`) and a group size (`n`) and breaks it into chunks of
    size `n`. Returns a list with each group reversed in a single list.

    >>> reverse_in_groups([0, 1, 2, 3, 4, 5], 3)
    [2, 1, 0, 5, 4, 3]
    >>> reverse_in_groups([1, 2, 3, 4], 2)
    [2, 1, 4, 3]
    """
    result = []
    for i in range(0, len(lst), n):
        chunk = lst[i:i + n]
        result.extend(chunk[::-1])
    return result


def pig_latin(text):
    """
    Takes a sentence as a string and translates it into Pig Latin following the
    typical convention.

    >>> pig_latin("apple banana")
    'appleyay ananabay'
    """
    vowels = ["a", "e", "i", "o", "u", "y"]

    words = text.split()
    translated = []

    for word in words:
        if word[0] in vowels:
            translated.append(word + "yay")
        else:
            translated.append(word[1:] + word[0] + "ay")

    return " ".join(translated)



def pig_latin_to_english(text):
    """
    Takes a sentence as a string and translates it back to English following the
    typical convention.

    >>> pig_latin_to_english("appleyay ananabay")
    'apple banana'
    """
    words = text.split()
    translated = []

    for word in words:
        if word.endswith("yay"):
            translated.append(word[:-3])
        elif word.endswith("ay"):
            base_word = word[:-2]
            translated.append(base_word[-1] + base_word[:-1])


    return " ".join(translated)





# print(drop_ends([0,1,2,3,4,5,6], 2))
# print(extract_edges([1,2,3,4,5,6,7,8]))
# print(extract_edges([10, 20, 30]))
# print(reverse_in_groups([0,1,2,3,4,5], 3))
print(pig_latin("apple banana"))
print(pig_latin_to_english("appleyay ananabay"))