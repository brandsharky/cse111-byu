class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0


    def __str__(self):
        return f"{self.title} by {self.author}"


    def __repr__(self):
        return f"Book({self.id}, '{self.title}', '{self.author}')"



class Library:
    """A Library takes in an arbitrary amount of books, and has a
    dictionary of id numbers as keys, and Books as values.
    """

    def __init__(self, books):
        """Takes in an arbitrary number of book objects in a list and
        puts them in a books dictionary which takes the book
        id as the key and the book object as the value

        >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
        >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
        >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
        >>> l = Library([b1, b2, b3])
        >>> l.books[0].title
        'A Tale of Two Cities'
        >>> l.books[0].author
        'Charles Dickens'
        """
        self.books = {}
        for book in books:
            self.books[book.id] = book


    def __str__(self):
        book_strs = [str(book) for book in self.books.values()]
        return " | ".join(book_strs)


    def __repr__(self):
        book_reprs = [repr(book) for book in self.books.values()]
        return f"Library([{', '.join(book_reprs)}])"