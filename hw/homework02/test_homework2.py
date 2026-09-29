from pathlib import Path
from PIL import Image as PILImage, ImageChops
from byu_pytest_utils import this_folder, test_files, with_import, tier
from pytest import approx

core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)


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


@core
@with_import('homework2', 'darken')
def test_CORE_darken(darken):
    observed = darken(test_files / 'cougar.png', 0.8)
    compare_images(observed.image, test_files / 'cougar_darkened.key.png')


@core
@with_import('homework2', 'grayscale')
def test_CORE_grayscale(grayscale):
    observed = grayscale(test_files / 'cougar.png')
    compare_images(observed.image, test_files / 'cougar_grayscale.key.png')


@core
@with_import('homework2', 'sepia')
def test_CORE_sepia(sepia):
    observed = sepia(test_files / 'cougar.png')
    compare_images(observed.image, test_files / 'cougar_sepia.key.png')


@advanced
@with_import('homework2', 'flipped')
def test_ADVANCED_flipped_with_landscape(flipped):
    observed = flipped(test_files / 'landscape.png')
    compare_images(observed.image, test_files / 'landscape_flipped.key.png')


@advanced
@with_import('homework2', 'flipped')
def test_ADVANCED_flipped_with_flamingo_float(flipped):
    observed = flipped(test_files / 'flamingo-float.png')
    compare_images(observed.image, test_files / 'flamingo-float_flipped.key.png')


@excellent
@with_import('homework2', 'make_borders')
def test_EXCELLENT_make_borders_landscape(make_borders):
    observed = make_borders(test_files / 'landscape.png', 30, 0, 255, 0)
    compare_images(observed.image, test_files / 'landscape_border.key.png')


@excellent
@with_import('homework2', 'make_borders')
def test_EXCELLENT_make_borders_flamingo_float_10(make_borders):
    observed = make_borders(test_files / 'flamingo-float.png', 10, 0, 255, 255)
    compare_images(observed.image, test_files / 'flamingo-float_border_10.key.png')


@excellent
@with_import('homework2', 'make_borders')
def test_EXCELLENT_make_borders_flamingo_float_5(make_borders):
    observed = make_borders(
        test_files / 'flamingo-float.png', 5, 255, 125, 125)
    compare_images(observed.image, test_files / 'flamingo-float_border_5.key.png')


@excellent
@with_import('homework2', 'make_borders')
@with_import('homework2', 'flipped')
@with_import('homework2', 'sepia')
@with_import('homework2', 'grayscale')
@with_import('homework2', 'darken')
def test_EXCELLENT_docstrings_present(darken, grayscale, sepia, flipped, make_borders):
    assert darken.__doc__ is not None, "darken() is missing a docstring."
    assert grayscale.__doc__ is not None, "grayscale() is missing a docstring."
    assert sepia.__doc__ is not None, "sepia() is missing a docstring."
    assert flipped.__doc__ is not None, "flipped() is missing a docstring."
    assert make_borders.__doc__ is not None, "make_borders() is missing a docstring."
