"""
Image Manipulation

Brandon Arroyo
September 29, 2026
"""

from byuimage import Image



def darken(filename: str, percent: float) -> Image:
    """
    Takes in a filenamefor an image and percent to darken the image and returns the darkened image.

    :param filename: A string representing the image which the user wants to use.
    :param percent: A float between 0 and 1 representing the percent which to darken the given image.

    :return: An image object of the resulting darkened image.
    """
    image = Image(filename)
    for pixel in image:
        pixel.red = pixel.red * (1.0 - percent)
        pixel.green = pixel.green * (1.0 - percent)
        pixel.blue = pixel.blue * (1.0 - percent)

    return image


def grayscale(filename: str) -> Image:
    """
    Takes in a filename and returns the image in grayscale(black and white);

    :param filename: A string representing the image which the user wants to use.

    :return: An image object of the resulting grayscaled image.
    """
    image = Image(filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) / 3
        pixel.red = average
        pixel.green = average
        pixel.blue = average

    return image


def sepia(filename: str) -> Image:
    """
    Takes in a filename and returns the image with the sepia filter applied.

    :param filename: A string representing the image which the user wants to use.

    :return: An image object of the resulting sepia filtered image.
    """
    image = Image(filename)
    for pixel in image:
        true_red = (0.393 * pixel.red) + (0.769 * pixel.green) + (0.189 * pixel.blue)
        true_green = (0.349 * pixel.red) + (0.686 * pixel.green) + (0.168 * pixel.blue)
        true_blue = (0.272 * pixel.red) + (0.534 * pixel.green) + (0.131 * pixel.blue)

        pixel.red, pixel.green, pixel.blue = true_red, true_green, true_blue

        if pixel.red > 255:
            pixel.red = 255

        if pixel.green > 255:
            pixel.green = 255

        if pixel.blue > 255:
            pixel.blue = 255

    return image


def flipped(filename: str) -> Image:
    """
    Takes in a filename and returns it flipped vertically as a new image.

    :param filename: A string representing the image which the user wants to use.

    :return: An image object of the given image flipped vertically.
    """
    old_image = Image(filename)
    flipped_image = Image.blank(old_image.width, old_image.height)

    for y in range(old_image.height):
        for x in range(old_image.width):
            old_pixel = old_image.get_pixel(x, y)
            new_pixel = flipped_image.get_pixel(x, old_image.height - y - 1)

            new_pixel.red, new_pixel.green, new_pixel.blue = old_pixel.red, old_pixel.green, old_pixel.blue

    return flipped_image


def make_borders(filename: str, thickness: int, red: int, green: int | float, blue: int | float) -> Image:
    """
    Takes in a filename, border thickness, border red, green, and blue value and returns the image with the given border added to it.

    :param filename: A string representing the image which the user wants to use.
    :param thickness: An integer representing the border's desired thickness.
    :param red: A integer or float representing the desired border red value.
    :param green: A integer or float representing the desired border green value.
    :param blue: A integer or float representing the desired border blue value.

    :return: An image object of the image with the desired border around it.
    """
    old_image = Image(filename)
    bordered_image = Image.blank(old_image.width + 2 * thickness, old_image.height + 2 * thickness)

    for pixel in bordered_image:
        pixel.red = red
        pixel.green = green
        pixel.blue = blue

    for y in range(old_image.height):
        for x in range(old_image.width):
            old_pixel = old_image.get_pixel(x, y)
            new_pixel = bordered_image.get_pixel(x + thickness, y + thickness)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    return bordered_image









if __name__ == "__main__":
    # solution = darken("test_files/cougar.png", 0.6)
    # solution.show()

    # gray = grayscale("test_files/cougar.png")
    # gray.show()

    # solution = sepia("test_files/cougar.png")
    # solution.show()

    # solution = flipped("test_files/landscape.png")
    # solution.show()

    bordered = make_borders("test_files/landscape.png", 30, 0, 255, 0)
    bordered.show()