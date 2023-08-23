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
    # TODO: from here
    new = np.zeros(pixels.shape)
    new[::2] = pixels[::2]
    return new


def ft_green(pixels: np.ndarray) -> np.ndarray:
    '''Keeps only green pixels of RGB'''
    pass


def ft_blue(pixels: np.ndarray) -> np.ndarray:
    '''Keeps only blue pixels of RGB'''
    pass


def ft_grey(pixels: np.ndarray) -> np.ndarray:
    '''Makes pixels black and white (greyscale)'''
    pass


def pimp_image():
    '''Rotates image and displays it'''
    try:
        img = ft_load("landscape.jpg")
        arr_pixels = np.array(img)

        # Original
        # img.show()

        # Invert
        print('\n________________________________________________\n')
        print(ft_invert.__doc__)
        invert_pixels = ft_invert(arr_pixels)
        img_invert = Image.fromarray(invert_pixels)
        # img_invert.show()

        # Red
        print('\n________________________________________________\n')
        print(ft_red.__doc__)
        red_pixels = ft_red(arr_pixels)
        img_red = Image.fromarray(red_pixels)
        img_red.show()

        # print('\n________________________________________________\n')
        # print('New shape after Transpose:', np.shape(arr_pixels))
        # print(arr_pixels)
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
