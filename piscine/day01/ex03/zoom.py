from PIL import Image
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


def zoom(path: str) -> np.array:
    '''Zooms image and displays it'''
    try:
        img = Image.open(path)
        width, height = img.size
        left = 300
        top = 150
        right = left + width / 2
        bottom = top + height / 2
        img_zoomed = img.crop((left, top, right, bottom))
        newsize = (400, 400)
        img_zoomed.thumbnail(newsize)  # thumbnail keep the initial dimentions
        img_zoomed = img_zoomed.convert('L')  # greyscale
        img_zoomed = img_zoomed.crop((100, 0, 400, 300))  # to make square crop
        img_zoomed.show()

        arr_pixels = np.array(img_zoomed)
        new_width, new_height = img_zoomed.size
        print('Image size. width:', new_width, 'height:', new_height)
        print('New shape after slicing:',
              np.shape(arr_pixels))
        print('Scale:', new_width / width, new_height / height)
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
    print('\n________________________________________________\n')
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
