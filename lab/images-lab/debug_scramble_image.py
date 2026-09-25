from byuimage import Image
from PIL.ImageChops import difference
from sys import argv

def compare_images(image1, image2):
    """
    Compares the images to make sure the scramble can be undone. There are no
    errors in this function.
    """
    image1 = image1.image
    image2 = image2.image

    assert image1.size == image2.size

    diff = difference(image1, image2)
    if bbox := diff.getbbox():
        for y in range(bbox[1], bbox[3]):
            for x in range(bbox[0], bbox[2]):
                pix1 = image1.getpixel((x,y))
                pix2 = image2.getpixel((x,y))
                assert abs(pix1[0] - pix2[0]) < 2, f'Red values at pixel ({x}, {y}) do not match!'
                assert abs(pix1[1] - pix2[1]) < 2, f'Green values at pixel ({x}, {y}) do not match!'
                assert abs(pix1[2] - pix2[2]) < 2, f'Blue values at pixel ({x}, {y}) do not match!'


# ***** Errors may occur below here *****
def scramble_image(input_file, output_file):
    """
    Scrambles an input image file by replacing the red pixels values with the
    values for the green pixels, the green pixels values with the blue pixels
    values, and the blues pixels values with the red pixels values.
    """
    image = Image(input_file)

    for pixel in image:
        tmp = pixel.green
        pixel.red = pixel.green
        pixel.green = pixel.blue
        pixel.blue = tmp

    image.save(output_file)

def verify_scramble(input_file, scramble_file):
    """
    Verifies a scramble by undoing it and comparing it to the source image. The
    scramble is defined in the `scramble_image` function.
    """
    unmodified = Image(input_file)
    scrambled = Image(scramble_file)

    for pixel in scrambled:
        tmp = pixel.red
        pixel.red = pixel.blue
        pixel.green = tmp
        pixel.blue = pixel.green

    compare_images(unmodified, scrambled)


# To test, run this function with the input image and the output image
def scramble(input_file, output_file):
    scramble_image(input_file, output_file)
    verify_scramble(input_file, output_file)


if __name__ == '__main__':
    scramble("test_files/cougar.png", "test_files/cougar_scrambled.png")

