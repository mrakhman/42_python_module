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


def zoom(path: str) -> np.array:
    '''Zooms image and displays it'''
    try:
        img = Image.open(path)
        width, height = img.size
        left = 300
        top = 150
        right = left + width / 3
        bottom = top + height / 3
        img_zoomed = img.crop((left, top, right, bottom))
        newsize = (300, 300)
        img_zoomed = img_zoomed.resize(newsize)
        img_zoomed.show()

    # TODO: describe new zoomed image like in subject!

        # arr_pixels = np.array(img)
        # print('Image title:', path)
        # print('Image format:', img.format)
        # print('Image size. width:', width, 'height:', height)
        # print('The shape of the image (aka 3 RGB channels):',
        #   np.shape(arr_pixels))
        # print('Scale:', width / width, height / height)
        return None
    except Exception as e:
        print('Error processing image')
        print(e)


@_guard_
def main():
    '''Main for tests and error handling'''
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
