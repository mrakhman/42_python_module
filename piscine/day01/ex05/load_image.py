from PIL import Image
import numpy as np


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def ft_load(path: str) -> np.array:
    '''Loads image, shows its shape (RGB channels) and array of pixels'''
    try:
        img = Image.open(path)
        arr_pixels = np.array(img)

        print('The shape of image is:', np.shape(arr_pixels))
        print()
        print(arr_pixels)
        return img
    except Exception as e:
        print('Error processing image')
        print(e)


@_guard_
def main():
    '''Main for tests and error handling'''
    # ft_load("landscape.jpg")
    pass


if __name__ == "__main__":
    main()
