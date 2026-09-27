def return_poem():
    return "By: Sarah Anderson\nSalty breeze dances,\nWhispering secrets untold,\nOcean’s lullaby."


def quotation(quote):
    return f"Don't forget the saying, \"{quote}\"."


def count_words(sentence):
    return len(sentence.strip().split())


def class_list(classes):
    return "\n".join(classes)


if __name__ == '__main__':
    # print(return_poem())
    # print(quotation("To be or Not to Be"))
    print(count_words(""))
    # print(class_list(["Math", "Science", "History"]))