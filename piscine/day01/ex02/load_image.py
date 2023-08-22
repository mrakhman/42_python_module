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
    try:
        img = Image.open(path)
        arr_pixels = np.array(img)
        print('The shape of the image is:', np.shape(arr_pixels))
        print(arr_pixels)
        return None
    except Exception as e:
        print('Error processing image')
        print(e)


@_guard_
def main():
    '''Main for tests and error handling'''
    ft_load("landscape.jpg")
    print()
    ft_load("animal.jpeg")
    print()
    ft_load("dog.png")
    print()
    ft_load('load_image.py')


if __name__ == "__main__":
    main()
