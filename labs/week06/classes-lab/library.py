class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0


class Library:
    """A Library takes in an arbitrary amount of books, and has a
    dictionary of id numbers as keys, and Books as values.
    >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    >>> l = Library([b1, b2, b3])
    >>> l.books[0].title
    'A Tale of Two Cities'
    >>> l.books[0].author
    'Charles Dickens'
    >>> l.read_book(1)
    'The Hobbit has been read 1 time(s)'
    >>> l.read_book(3) # No book with this id
    >>> l.read_author("Charles Dickens")
    'A Tale of Two Cities has been read 1 time(s)\\n'
    >>> l.read_author("J.R.R. Tolkien")
    'The Hobbit has been read 2 time(s)\\nThe Fellowship of the Ring has been read 1 time(s)\\n'

    >>> b1.times_read
    1
    >>> b2.times_read
    2
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


    def read_book(self, id):
        """Takes in an id of the book read, and
        returns that book's title and the number
        of times it has been read.

        >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
        >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
        >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
        >>> l = Library([b1, b2, b3])
        >>> l.read_book(1)
        'The Hobbit has been read 1 time(s)'
        >>> l.read_book(3) # No book with this id
        """
        if id in self.books:
            book = self.books[id]
            book.times_read += 1
            return f"{book.title} has been read {book.times_read} time(s)"


    def read_author(self, author):
        """Takes in the name of an author, then increments
        the number of times read and returns the title and number
        of times the book has been read for each book written
        by that author in a single string.
        Hint: Each book output should be on a different line.

        >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
        >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
        >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
        >>> l = Library([b1, b2, b3])
        >>> l.read_author("J.R.R. Tolkien")
        'The Hobbit has been read 1 time(s)\\nThe Fellowship of the Ring has been read 1 time(s)\\n'
        """
        result = ""
        for book in self.books.values():
            if book.author == author:
                result += self.read_book(book.id) + "\n"

        return result


    def add_book(self, book):
        """Takes in a book object and adds it to the books
        dictionary if the book id is not already taken."""
        if book not in self.books:
            self.books[book.id] = book