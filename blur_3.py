import cv2
import numpy as np
from numba import jit
import sys

def blur_image(src, dst=None):
    """
    A function that uses the package numba to blur images efficiently.
    The blurring in itself is done in the blur_image_array function.
    Input: 
        src (str): An image that you want to blur
        dst (str): The name for your new image. Defaults to not saving the image
    Output:
        An array containing the blurred image
    """
    src = cv2.imread(src)
    #padding the source image so there's adjacent pixels to use in the 
    #calculation for the edges
    src = np.pad(src, ((1,1),(1,1),(0,0)), "edge")
    blurred_image = np.array(blur_image_array(src))
    if (dst != None):
        cv2.imwrite(dst, blurred_image)
    return blurred_image

@jit(nopython=True)
def blur_image_array(arr):
    """
    A helper-function that takes a padded image array and uses the numba package
    to efficiently calculate the average value of all adjacent pixels in order 
    to blur the image.
    Input: 
        arr (str): A padded image array/list that you want to blur
    Output:
        A list containing the blurred image
    """
    height = arr.shape[0]-2 #-2 accounts for padding
    width = arr.shape[1]-2
    color = arr.shape[2]
    blurred_image = []
    for h in range(height):
        new_row = []
        for w in range(width):
            new_column = []
            for c in range(color):
                new_column.append((arr[h+1][w+1][c] + arr[h][w+1][c] + 
                arr[h+2][w+1][c] + arr[h+1][w][c] + arr[h+1][w+2][c] + 
                arr[h][w][c] + arr[h][w+2][c] + arr[h+2][w][c] + 
                arr[h+2][w+2][c]) // 9)
            new_row.append(new_column)
        blurred_image.append(new_row)
    return blurred_image

"""
Usage: python blur_3.py [file_source] [file_destionation]
"""

if __name__ == "__main__":
    #Assumes sys.argv[1] is source image and sys.argv[2] is destination
    if (len(sys.argv) == 2):
        blur_image(sys.argv[1])
    elif (len(sys.argv) == 3):
        blur_image(sys.argv[1], sys.argv[2])
    else:
        raise Exception("Wrong number of arguments!")