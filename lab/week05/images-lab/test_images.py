from PIL import Image as PILImage, ImageChops
from byu_pytest_utils import test_files, with_import, ensure_missing, this_folder
import pytest
from pytest import approx
from pathlib import Path
import sys


sys.path.append(str(test_files))
import image_solutions  # type: ignore[import]


def compare_images(obs: Path | PILImage.Image, exp: Path | PILImage.Image, *, min_pixel_match_ratio: float = 1.0):
    assert 0 <= min_pixel_match_ratio <= 1, "min_pixel_match_ratio must be between 0 and 1."

    if not isinstance(obs, PILImage.Image):
        observed = PILImage.open(obs).convert('RGB')
    else:
        observed = obs
    if not isinstance(exp, PILImage.Image):
        expected = PILImage.open(exp).convert('RGB')
    else:
        expected = exp

    obs_stem = obs.stem if isinstance(obs, Path) else "image"

    try:
        assert observed.size == expected.size, f"Image sizes don't match. Expected `{expected.size}`, but got `{observed.size}`."

        diff = ImageChops.difference(observed, expected)
        bbox = diff.getbbox()
        if not bbox:
            return

        if min_pixel_match_ratio == 1.0:
            for y in range(bbox[1], bbox[3]):
                for x in range(bbox[0], bbox[2]):
                    observed_pixel = observed.getpixel((x, y))
                    expected_pixel = expected.getpixel((x, y))
                    if not observed_pixel or not expected_pixel:
                        assert False, f"Failed to get pixels at ({x}, {y})!"

                    if isinstance(observed_pixel, (float, int)) or isinstance(expected_pixel, (float, int)):
                        assert False, "Failed to get correct pixel type!"

                    try:
                        assert observed_pixel[0] == approx(expected_pixel[0], abs=2), f"The pixels' red values at ({x}, {y}) don't match. Expected `{expected_pixel[0]}`, but got `{observed_pixel[0]}`. Check the diff image ({obs_stem}.diff.png) for details."
                        assert observed_pixel[1] == approx(expected_pixel[1], abs=2), f"The pixels' green values at ({x}, {y}) don't match. Expected `{expected_pixel[1]}`, but got `{observed_pixel[1]}`. Check the diff image ({obs_stem}.diff.png) for details."
                        assert observed_pixel[2] == approx(expected_pixel[2], abs=2), f"The pixels' blue values at ({x}, {y}) don't match. Expected `{expected_pixel[2]}`, but got `{observed_pixel[2]}`. Check the diff image ({obs_stem}.diff.png) for details."
                    except AssertionError as e:
                        if isinstance(obs, Path):
                            diff.save(this_folder / f'{obs_stem}.diff.png')
                        raise e
            return

        total_pixels = observed.width * observed.height
        matching_pixels = 0
        first_mismatch = None
        for y in range(observed.height):
            for x in range(observed.width):
                observed_pixel = observed.getpixel((x, y))
                expected_pixel = expected.getpixel((x, y))
                if not observed_pixel or not expected_pixel:
                    assert False, f"Failed to get pixels at ({x}, {y})!"

                if isinstance(observed_pixel, (float, int)) or isinstance(expected_pixel, (float, int)):
                    assert False, "Failed to get correct pixel type!"

                red_matches = observed_pixel[0] == approx(expected_pixel[0], abs=2)
                green_matches = observed_pixel[1] == approx(expected_pixel[1], abs=2)
                blue_matches = observed_pixel[2] == approx(expected_pixel[2], abs=2)
                if red_matches and green_matches and blue_matches:
                    matching_pixels += 1
                elif first_mismatch is None:
                    first_mismatch = (x, y, observed_pixel, expected_pixel)

        match_ratio = matching_pixels / total_pixels
        if match_ratio < min_pixel_match_ratio:
            if isinstance(obs, Path):
                diff.save(this_folder / f'{obs_stem}.diff.png')

            mismatch_message = ""
            if first_mismatch is not None:
                x, y, observed_pixel, expected_pixel = first_mismatch
                mismatch_message = f" First mismatch at ({x}, {y}): expected `{expected_pixel}`, got `{observed_pixel}`."
            assert False, (
                f"Only {match_ratio * 100:.2f}% of pixels matched, but at least "
                f"{min_pixel_match_ratio * 100:.2f}% is required.{mismatch_message} "
                f"Check the diff image ({obs_stem}.diff.png) for details."
            )
    finally:
        if isinstance(obs, Path):
            obs.unlink(missing_ok=True)


@with_import('images', 'iron_puzzle')
def test_iron_puzzle(iron_puzzle):
    observed = iron_puzzle(test_files / 'iron.png')
    compare_images(observed.image, image_solutions.iron_solution)


@with_import('images', 'west_puzzle')
def test_west_puzzle(west_puzzle):
    observed = west_puzzle(test_files / 'west.png')
    compare_images(observed.image, image_solutions.west_solution)


@with_import('images', 'darken')
def test_darken(darken):
    observed = darken(test_files / 'cougar.png', 0.8)
    compare_images(observed.image, test_files / 'cougar_darkened.key.png')


@with_import('images', 'grayscale')
def test_grayscale(grayscale):
    observed = grayscale(test_files / 'cougar.png')
    compare_images(observed.image, test_files / 'cougar_grayscale.key.png')


@with_import('images', 'sepia')
def test_sepia(sepia):
    observed = sepia(test_files / 'cougar.png')
    compare_images(observed.image, test_files / 'cougar_sepia.key.png')


@with_import('images', 'create_left_border')
def test_create_left_border(create_left_border):
    observed = create_left_border(test_files / 'cougar.png', 25)
    compare_images(observed.image, test_files / 'cougar_bordered.key.png')


@with_import('images', 'create_stripes')
def test_create_stripes(create_stripes):
    observed = create_stripes(test_files / 'cougar.png')
    compare_images(observed.image, image_solutions.striped_solution)


@with_import('images', 'copper_puzzle')
def test_copper_puzzle(copper_puzzle):
    observed = copper_puzzle(test_files / 'copper.png')
    compare_images(observed.image, image_solutions.copper_solution)


@ensure_missing(this_folder / "scrambled_cougar.png")
@with_import('debug_scramble_image', 'verify_scramble')
@with_import('debug_scramble_image', 'scramble')
def test_scramble_puzzle(scramble, verify_scramble):
    output = this_folder / 'scrambled_cougar.png'
    scramble(test_files / 'cougar.png', output)
    compare_images(PILImage.open(output), test_files / "cougar_scrambled.png")
    verify_scramble(test_files / "cougar.png", output)
    with pytest.raises(AssertionError):
        verify_scramble(output, test_files / 'cougar.png')
    output.unlink(missing_ok=True)
