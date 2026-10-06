"""
Project 01 - Image Processing

Brandon Arroyo
October 4, 2026
"""

import sys
from byuimage import Image



def validate_commands(args:list[str]) -> bool:
    """
    Takes in a list of arguments from the command prompt and returns a boolean of whether they are valid.

    :param args: A list of strings with the operation first, then the rest of the corresponding arguments.

    :return: A boolean of whether the operation is known, has the right number of arguments, and the right type of arguments.

    :raises ValueError: If one of the numeric values isn't an integer of float.

    >>> validate_commands(["-d", "image.jpg"])
    True
    >>> validate_commands(["-d"])
    False
    >>> validate_commands(["-k", "input.jpg", "output.jpg", "a"])
    False
    >>> validate_commands(["-b", "input.jpg", "output.jpg", "20", "255", "0", "0"])
    True
    >>> validate_commands(["-y", "foreground.jpg", "background.jpg", "output.jpg", "90", "1.3"])
    True
    >>> validate_commands(["-y", "foreground.jpg", "background.jpg", "output.jpg", "90"])
    False
    >>> validate_commands([])
    False
    """
    if len(args) == 2 and args[0] == "-d":
        return True

    if len(args) == 4 and args[0] == "-k":
        try:
            float(args[3])
        except ValueError:
            return False
        return True

    if len(args) == 3 and args[0] in ("-s", "-g", "-f", "-m"):
        return True

    if len(args) == 7 and args[0] == "-b":
        try:
            float(args[3])
            float(args[4])
            float(args[5])
            float(args[6])
        except ValueError:
            return False
        return True

    if len(args) == 7 and args[0] == "-c":
        try:
            float(args[6])
        except ValueError:
            return False
        return True

    if len(args) == 5 and args[0] == "-y":
        try:
            float(args[5])
            float(args[6])
        except ValueError:
            return False
        return True

    if len(args) == 6 and args[0] == "-y":
        try:
            float(args[4])
            float(args[5])
        except ValueError:
            return False
        return True

    return False


def load_image(filename:str) -> Image:
    """
    Takes in a filename and returns said file as an Image object.

    :param filename: A string of the file desired to be turned into an image.

    :return: An image object of the desired filename.
    """
    return Image(filename)


def apply_filter(input_file:str, output_file:str, pixel_function, *extra_args:float) -> None:
    """
    Takes in an input file, output file, the desired filter function, and additional arguments for the filter function; applies the filter function with the extra arguments to the input file and saves it to the desired output file.

    :param input_file: A string of the image file to have the filter applied to.
    :param output_file: A string of the resulting filtered file's desired name.
    :param pixel_function: A function call of the desired filter.
    :param *extra_args: Floats of the additional required arguments for the desired filter.

    :return: None

    :raises FileNotFoundError: If input_file doesn't exist.
    """
    image = load_image(input_file)

    for pixel in image:
        pixel_function(pixel, *extra_args)

    image.save(output_file)


def darken_pixel(pixel, percent:float) -> None:
    """
    Takes in a pixel and a percent to darken it by.

    :param pixel: A pixel to darken.
    :param percent: A float to darken the pixel by.

    :return: None
    """
    pixel.red = pixel.red * (1.0 - percent)
    pixel.green = pixel.green * (1.0 - percent)
    pixel.blue = pixel.blue * (1.0 - percent)


def sepia_pixel(pixel) -> None:
    """
    Takes in a pixel and applies the sepia filter to it.

    :param pixel: A pixel to have the sepia filter applied to.

    :return: None
    """
    true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
    true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
    true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue

    pixel.red = true_red
    pixel.green = true_green
    pixel.blue = true_blue

    if pixel.red > 255:
        pixel.red = 255
    if pixel.green > 255:
        pixel.green = 255
    if pixel.blue > 255:
        pixel.blue = 255


def grayscale_pixel(pixel) -> None:
    """
    Takes in a pixel to have the grayscale filter applied to.

    :param pixel: A pixel object to be turned to grayscale.

    :return: None
    """
    average = (pixel.red + pixel.green + pixel.blue) / 3.0
    pixel.red = average
    pixel.green = average
    pixel.blue = average


def flip_position(x:int, y:int, width:int, height:int) -> tuple[int, int]:
    """
    Takes in an x position, y position, width of an image, and height of an image and return a tuple of the x value and the calculated y value.

    :param x: An integer of the x position.
    :param y: An integer of the y position.
    :param width: An integer of the width of the image.
    :param height: An integer of the height of the image.

    :return: A tuple of the x coordinate and the calculated y coordinate.
    """
    return x, height - 1 - y


def mirror_position(x:int, y:int, width:int, height:int) -> tuple[int, int]:
    """
    Takes in an x position, y position, width of an image, and height of an image and return a tuple of the calculated x value and the y value.

    :param x: An integer of the x position.
    :param y: An integer of the y position.
    :param width: An integer of the width of the image.
    :param height: An integer of the height of the image.

    :return: A tuple of the calculated x coordinate and the y coordinate.
    """
    return width - 1 - x, y


def move_pixels(input_file:str, output_file:str, new_position) -> None:
    """
    Takes in an input file, an output file, and the function to call on the input file, which is saved to the output file.

    :param input_file: A string of the desired input image file.
    :param output_file: A string representing the name of the file to save the image too.
    :param new_position: A function to call on the input file.

    :return: None

    :raises FileNotFoundError: If input_file doesn't exist.
    """
    image = load_image(input_file)
    moved = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            new_x, new_y = new_position(x, y, image.width, image.height)
            old_pixel = image.get_pixel(x, y)
            new_pixel = moved.get_pixel(new_x, new_y)
            red = old_pixel.red
            green = old_pixel.green
            blue = old_pixel.blue

            new_pixel.red, new_pixel.green, new_pixel.blue = red, green, blue

    moved.save(output_file)


def make_borders(input_file:str, output_file:str, thickness:int, red:int, green:int, blue:int) -> None:
    """
    Takes in an input file, and output file, desired border thickness, and integers for the desired red, green, and blue values; adds the border to the input_file and saves it to output_file.

    :param input_file: A string representing the desired input file to apply the border to.
    :param output_file: A string representing the name of the file to save the file as.
    :param thickness: An integer representing the desired border thickness for the image.
    :param red: An integer of the desired red value of the border.
    :param green: An integer of the desired green value of the border.
    :param blue: An integer of the desired blue value of the border.

    :return: None

    :raise FileNotFoundError: If input file doesn't exist.
    """
    image = load_image(input_file)
    bordered_image = Image.blank(image.width + 2 * int(thickness), image.height + 2 * int(thickness))

    for y in range(bordered_image.height):
        for x in range(bordered_image.width):
            pixel = bordered_image.get_pixel(x, y)
            pixel.red = red
            pixel.green = green
            pixel.blue = blue

    for y in range(image.height):
        for x in range(image.width):
            old_pixel = image.get_pixel(x, y)
            new_pixel = bordered_image.get_pixel(x + int(thickness), y + int(thickness))
            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    bordered_image.save(output_file)


def make_collage(input1:str, input2:str, input3:str, input4:str, output_file:str, thickness:int) -> None:
    """
    Takes in four images, a desired output file, and border thickness and saves the four images as a collage with the border thickness applied as the output file.

    :param image1: A string of the first image to add to the collage.
    :param image2: A string of the second image to add to the collage.
    :param image3: A string of the third image to add to the collage.
    :param image4: A string of the fourth image to add to the collage.
    :param output_file: A string representing the name to save the collage as.
    :param thickness: An integer of the desired collage border.

    :returns: None

    :raises FileNotFoundError: If any of the input images don't exist.
    """
    image1 = load_image(input1)
    image2 = load_image(input2)
    image3 = load_image(input3)
    image4 = load_image(input4)

    thickness = int(thickness)

    width = image1.width
    height = image1.height

    collage_width = (width * 2) + (thickness * 3)
    collage_height = (height * 2) + (thickness * 3)

    collage = Image.blank(collage_width, collage_height)

    # Set entire collage black
    for pixel in collage:
        pixel.red = 0
        pixel.green = 0
        pixel.blue = 0

    # Image 1
    for y in range(height):
        for x in range(width):
            old_pixel = image1.get_pixel(x, y)
            new_pixel = collage.get_pixel(x + thickness, y + thickness)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    # Image 2
    for y in range(height):
        for x in range(width):
            old_pixel = image2.get_pixel(x, y)
            new_pixel = collage.get_pixel(x + width + thickness * 2, y + thickness)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    # Image 3
    for y in range(height):
        for x in range(width):
            old_pixel = image3.get_pixel(x, y)
            new_pixel = collage.get_pixel(x + thickness, y + height + thickness * 2)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    # Image 4
    for y in range(height):
        for x in range(width):
            old_pixel = image4.get_pixel(x, y)
            new_pixel = collage.get_pixel(x + width + thickness * 2, y + height + thickness * 2)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    collage.save(output_file)


def detect_green(pixel, threshold:float, factor:float) -> bool:
    """
    Takes in a pixel and determines if it is green enough using the threshold and factor.

    :param pixel: A pixel object to test the green value.
    :param threshold: A float of the desired green value to test.
    :param factor: A float representing the green value to factor.

    :return: A boolean representing if the green value passes or fails.
    """
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False


def green_screen(foreground_file:str, background_file:str, output_file:str, threshold:float, factor:float) -> None:
    """
    Takes in a foreground image, background image, the desired output name, a threshold of green, and a factor to check.

    :param foreground_file: A string representing the foreground image.
    :param background_file: A string representing the background image.
    :param output_file: A string representing the desired name of the file to be saved.
    :param threshold: A float representing the green value threshold.
    :param factor: A float representing the factor of the green value.

    :return: None

    :raises FileNotFoundError: If foreground_file or background_file doesn't exist.
    """
    foreground = load_image(foreground_file)
    background = load_image(background_file)

    threshold = float(threshold)
    factor = float(factor)

    for y in range(foreground.height):
        for x in range(foreground.width):
            foreground_pixel = foreground.get_pixel(x, y)

            if not detect_green(foreground_pixel, threshold, factor):
                background_pixel = background.get_pixel(x, y)

                background_pixel.red = foreground_pixel.red
                background_pixel.green = foreground_pixel.green
                background_pixel.blue = foreground_pixel.blue

    background.save(output_file)


def main():
    args = sys.argv[1:]
    if validate_commands(args):
        if args[0] == "-d":
            load_image(args[1]).show()
        elif args[0] == "-k":
            apply_filter(args[1], args[2], darken_pixel, float(args[3]))
        elif args[0] == "-s":
            apply_filter(args[1], args[2], sepia_pixel)
        elif args[0] == "-g":
            apply_filter(args[1], args[2], grayscale_pixel)
        elif args[0] == "-f":
            move_pixels(args[1], args[2], flip_position)
        elif args[0] == "-m":
            move_pixels(args[1], args[2], mirror_position)
        elif args[0] == "-b":
            make_borders(args[1], args[2], int(args[3]), int(args[4]), int(args[5]), int(args[6]))
        elif args[0] == "-c":
            make_collage(args[1], args[2], args[3], args[4], args[5], int(args[6]))
        elif args[0] == "-y":
            green_screen(args[1], args[2], args[3], float(args[4]), float(args[5]))

    else:
        print("Invalid command")










if __name__ == "__main__":
    main()