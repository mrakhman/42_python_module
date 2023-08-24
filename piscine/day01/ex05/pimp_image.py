from PIL import Image, ImageOps
import numpy as np
from load_image import ft_load


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def ft_invert(pixels: np.ndarray) -> np.ndarray:
    '''Inverts colours of pixels'''
    # Subtracting 255 (max value possible in a given image channel)
    # from each pixel values
    return 255 - pixels


def ft_red(pixels: np.ndarray) -> np.ndarray:
    '''Keeps only red pixels of RGB'''
    # multiply green and blue channels by 0
    red = pixels.copy()
    red[:, :, 1] *= 0
    red[:, :, 2] *= 0
    return red


def ft_green(pixels: np.ndarray) -> np.ndarray:
    '''Keeps only green pixels of RGB'''
    # substract blue and red channels from pixels
    green = pixels.copy()
    green = green - ft_blue(pixels) - ft_red(pixels)
    return green


def ft_blue(pixels: np.ndarray) -> np.ndarray:
    '''Keeps only blue pixels of RGB'''
    # set red and green channels to 0
    blue = pixels.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    return blue


def ft_grey(pixels: np.ndarray) -> np.ndarray:
    '''Turns pixels from rgb to greyscale'''
    # grey = 0.2989*red + 0.5870*green + 0.1140*blue
    grey = np.dot(pixels[:, :, :3], [0.2989, 0.5870, 0.1140])
    return grey


def pimp_image():
    '''Rotates image and displays it'''
    try:
        img = ft_load("landscape.jpg")
        arr_pixels = np.array(img)

        # Original
        img.show()

        # Invert
        print('\n________________________________________________\n')
        print(ft_invert.__doc__)
        invert_pixels = ft_invert(arr_pixels)
        img_invert = Image.fromarray(invert_pixels)
        img_invert.show()

        # Red
        print('\n________________________________________________\n')
        print(ft_red.__doc__)
        red_pixels = ft_red(arr_pixels)
        img_red = Image.fromarray(red_pixels)
        img_red.show()

        # Green
        print('\n________________________________________________\n')
        print(ft_green.__doc__)
        green_pixels = ft_green(arr_pixels)
        img_green = Image.fromarray(green_pixels)
        img_green.show()

        # Blue
        print('\n________________________________________________\n')
        print(ft_blue.__doc__)
        blue_pixels = ft_blue(arr_pixels)
        img_blue = Image.fromarray(blue_pixels)
        img_blue.show()

        # Grey
        print('\n________________________________________________\n')
        print(ft_grey.__doc__)
        grey_pixels = ft_grey(arr_pixels)
        img_grey = Image.fromarray(grey_pixels)
        img_grey.show()

        print('\n________________________________________________\n')
        return None
    except Exception as e:
        print('Error processing image')
        print(e)


@_guard_
def main():
    '''Main for tests and error handling'''
    pimp_image()


if __name__ == "__main__":
    main()
