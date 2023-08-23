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
    '''Loads image, crops it, shows its title, format, size,
    shape (RGB channels), scale and array of pixels'''
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

        arr_pixels = np.array(img_zoomed)
        new_width, new_height = img_zoomed.size
        print('The shape of image is:', np.shape(arr_pixels))
        print('Scale:', new_width / width, new_height / height)
        print()
        print(arr_pixels)
        return img_zoomed
    except Exception as e:
        print('Error processing image')
        print(e)


@_guard_
def main():
    '''Main for tests and error handling'''
    # ft_load("animal.jpeg")
    pass


if __name__ == "__main__":
    main()
