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
    '''Loads image and shows its title, format, size, shape (RGB channels),
     scale and array of pixels'''
    try:
        img = Image.open(path)
        arr_pixels = np.array(img)
        print('Image title:', path)
        print('Image format:', img.format)
        width, height = img.size
        print('Image size. width:', width, 'height:', height)
        print('The shape of the image (aka 3 RGB channels):',
              np.shape(arr_pixels))
        print('Scale:', width / width, height / height)
        print()
        print(arr_pixels)
        return None
    except Exception as e:
        print('Error processing image')
        print(e)


@_guard_
def main():
    '''Main for tests and error handling'''
    ft_load("animal.jpeg")


if __name__ == "__main__":
    main()
