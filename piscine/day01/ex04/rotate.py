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


def rotate90(arr):
    '''Rotates array 90 degrees clockwise'''
    N = len(arr)

    # Transpose of matrix (swap rows and columns)
    for i in range(N):
        for j in range(i + 1, N):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # Reverse rows
    for i in range(N):
        start = 0
        end = N - 1
        while (start < end):
            arr[i][start], arr[i][end] = arr[i][end], arr[i][start]
            start = start + 1
            end = end - 1
    return arr


def rotate():
    '''Rotates image and displays it'''
    try:
        img = ft_load("animal.jpeg")
        img_pixels = np.array(img)
        img_pixels_rotate = rotate90(img_pixels)
        img_pixels_rotate = rotate90(img_pixels)
        img_pixels_rotate = rotate90(img_pixels)
        img_rotate = Image.fromarray(img_pixels_rotate, 'L')

        img_rotate.show()

        print('\n________________________________________________\n')
        print('New shape after Transpose:', np.shape(img_pixels_rotate))
        print(img_pixels_rotate)
        return None
    except Exception as e:
        print('Error processing image')
        print(e)


@_guard_
def main():
    '''Main for tests and error handling'''
    rotate()


if __name__ == "__main__":
    main()
