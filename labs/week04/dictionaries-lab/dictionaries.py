# Q2
def word_count(text):
    """Your Code Here"""
    text = text.lower()
    words = text.split()
    word_dict = {}

    for word in words:
        word_dict[word] = words.count(word)

    return word_dict


# Q3
def find_key(dictionary, value):
    matches = []

    for key,dict_value in dictionary.items():
        if dict_value == value:
            matches.append(key)

    return matches


# Q4
def update_inventory(inventory, order):
    for key in order.keys():
        if key in inventory.keys():
            if order[key] > inventory[key]:
                inventory[key] = 0
            else:
                inventory[key] -= order[key]

    return inventory


# Q5
def filter_by_value(dictionary, min_value):
    filtered_dict = {key: value for key,value in dictionary.items() if value >= min_value}
    return filtered_dict


# Q6
def group_by_length(words):
    grouped_words = {}

    for word in words:
        if len(word) in grouped_words.keys():
            grouped_words[len(word)].append(word)
        else:
            grouped_words[len(word)] = [word]

    return grouped_words



# print(word_count("One Fish two fish red fish blue fish"))
# print(find_key({"band": "beetles", "book": "mistborn", "insect": "beetles"}, "beetles"))
# inventory = {"chocolate": 10, "graham crackers": 5, "marshmallows": 7}
# order = {"marshmallows": 3, "graham crackers": 10}
# print(update_inventory(inventory, order))
# print(filter_by_value({"class number": 111, "students": 378, "coding": 247}, 247))
# print(group_by_length(["cat", "dog", "bear", "fish"]))
print("Program Initialized")