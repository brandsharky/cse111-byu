class Rectangle:
    def __init__(self, width, height):
        if not Rectangle.valid_rectangle(width, height):
            raise ValueError("Width and height need to be greater than 0.")
        self.width = width
        self.height = height


    def area(self, width, height):
        return width * height


    def is_square(self, width, height):
        return width == height



    @staticmethod
    def valid_rectangle(width, height):
        return width > 0 and height > 0