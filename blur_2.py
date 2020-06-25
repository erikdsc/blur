import cv2
import numpy as np
import sys

def blur_image(src, dst=None):
    """
    A function that utilizes vectorization to blur images.
    Input: 
        src (str): An image that you want to blur
        dst (str): The name for your new image. Defaults to not saving the image
    Output:
        An array containing the blurred image
    """
    src = cv2.imread(src)
    height = src.shape[0]
    width = src.shape[1]    
    color = src.shape[2]
    src = src.astype("uint32")
    #padding the source image so there's adjacent pixels to use in the 
    #calculation for the edges
    src = np.pad(src, ((1,1),(1,1),(0,0)), "edge")

    array1 = src[:height, :width]
    array2 = src[1:height+1, :width]
    array3 = src[2:, :width]
    array4 = src[:height, 1:width+1]
    array5 = src[2:,1:width+1]
    array6 = src[:height, 2:]
    array7 = src[1:height+1, 2:]
    array8 = src[2:, 2:]
    blurred_image = (src[1:-1, 1:-1] + array1 + array2 + array3 + array4 + 
                                       array5 + array6 + array7 + array8)/ 9
    blurred_image = blurred_image.astype("uint8")
    if (dst != None):
        cv2.imwrite(dst, blurred_image)
    return blurred_image

"""
Usage: python blur_2.py [file_source] [file_destionation]
"""

if __name__ == "__main__":
    #Assumes sys.argv[1] is source image and sys.argv[2] is destination
    if (len(sys.argv) == 2):
        blur_image(sys.argv[1])
    elif (len(sys.argv) == 3):
        blur_image(sys.argv[1], sys.argv[2])
    else:
        raise Exception("Wrong number of arguments!")


