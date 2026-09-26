from byuimage import Image



# Q1
def iron_puzzle(filename):
    image = Image(filename)
    for pixel in image:
        pixel.red = 0
        pixel.green = 0
        pixel.blue *= 10

    return image


# Q2
# def west_puzzle(filename):
#     image = Image(filename)
#     for y in range(image.height):
#         for x in range(image.width):
#             pixel = image.get_pixel(x, y)
#             pixel.red = 0
#             pixel.green = 0
#
#             if pixel.blue < 16:
#                 pixel.blue *= 16
#             else:
#                 pixel.blue = 0
#
#     return image


# Q3
# def darken(filename, percent):
#     image = Image(filename)
#     for pixel in image:
#         pixel.red = pixel.red * (1.0 - percent)
#         pixel.green = pixel.green * (1.0 - percent)
#         pixel.blue = pixel.blue * (1.0 - percent)
#
#     return image


# Q4
# def grayscale(filename):
#     image = Image(filename)
#     for pixel in image:
#         average = (pixel.red + pixel.green + pixel.blue) / 3.0
#         pixel.red = average
#         pixel.green = average
#         pixel.blue = average
#
#     return image


# Q5
# def sepia(filename):
#     image = Image(filename)
#     for pixel in image:
#         true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
#         true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
#         true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
#
#         pixel.red = true_red
#         pixel.green = true_green
#         pixel.blue = true_blue
#
#         if pixel.red > 255:
#             pixel.red = 255
#         if pixel.green > 255:
#             pixel.green = 255
#         if pixel.blue > 255:
#             pixel.blue = 255
#
#     return image


# Q6
# def create_left_border(filename, weight):
#     image = Image(filename)
#     larger_image = Image.blank(image.width + weight, image.height)
#
#     for y in range(larger_image.height):
#         for x in range(larger_image.width):
#             og_pixel = image.get_pixel(x-weight, y)
#             new_pixel = larger_image.get_pixel(x, y)
#             if x < weight:
#                 new_pixel.red = 0
#                 new_pixel.green = 0
#                 new_pixel.blue = 255
#             else:
#                 new_pixel.red = og_pixel.red
#                 new_pixel.green = og_pixel.green
#                 new_pixel.blue = og_pixel.blue
#
#     return larger_image


# Q7
# def create_stripes(filename):
#     original_image = Image(filename)
#     new_image = Image.blank(original_image.width + 50, original_image.height + 25)
#
#     for y in range(new_image.height):
#         for x in range(new_image.width):
#             pixel = new_image.get_pixel(x, y)
#             pixel.red = 255
#
#             if y % 2 == 1:
#                 pixel.red = 0
#                 pixel.green = 0
#                 pixel.blue = 255
#
#             if x % 2 == 0:
#                 pixel.red = 0
#                 pixel.green = 255
#                 pixel.blue = 0
#
#     return new_image


# Q8
# def copper_puzzle(filename):
#     image = Image(filename)
#     for pixel in image:
#         pixel.red = 0
#         pixel.green *= 20.0
#         pixel.blue *= 20.0
#
#     return image






# Q1
solution_image = iron_puzzle("test_files/iron.png")
solution_image.show()

# Q2
# solution_image = west_puzzle("test_files/west.png")
# solution_image.show()

# Q3
# darken("test_files/cougar.png", 0.6).show()

# Q4
# gray = grayscale("test_files/cougar.png")
# gray.show()

# Q5
# solution_image = sepia("test_files/cougar.png")
# solution_image.show()

# Q6
# solution = create_left_border("test_files/cougar.png", 25)
# solution.show()

# Q7
# solution = create_stripes("test_files/cougar.png")
# solution.show()

# Q8
# solution = copper_puzzle("test_files/copper.png")
# solution.show()
