import cv2
import numpy as np
import sys

"""
Usage: python blur_1.py [file_source] [file_destination]
"""

def blur_image(src, dst=None):
    """
    A function that utilizes python loops to blur all image indices.
    Input: 
        src (str): An image that you want to blur
        dst (str): The name for your new image. Defaults to not saving the image
    Output:
        An array containing the blurred image
    """
    src = cv2.imread(src)
    #src = cv2.resize(src, (0 , 0) , fx =0.5 , fy =0.5)
    blurred_image = src.copy()
    height = src.shape[0]
    width = src.shape[1]
    color = src.shape[2]
    #padding the source image so there's adjacent pixels to use in the 
    #calculation for the edges
    src = np.pad(src, ((1,1),(1,1),(0,0)), "edge")
    #creates image where all pixels will be given the average value of all 
    #adjacent pixels
    for h in range(height):
        for w in range(width):
            for c in range(color):
                blurred_image[h, w, c] = (np.int16(src[h+1][w+1][c]) + 
                src[h][w+1][c] + src[h+2][w+1][c] + src[h+1][w][c] + 
                src[h+1][w+2][c] + src[h][w][c] + src[h][w+2][c]
                + src[h+2][w][c] + src[h+2][w+2][c]) // 9
    if (dst != None):
        cv2.imwrite(dst, blurred_image)
    return blurred_image

"""
Usage: python blur_1.py [file_source] [file_destionation]
"""

if __name__ == "__main__":
    #Assumes sys.argv[1] is source image and sys.argv[2] is destination
    if (len(sys.argv) == 2):
        blur_image(sys.argv[1], sys.argv[1])
    elif (len(sys.argv) == 3):
        blur_image(sys.argv[1], sys.argv[2])
    else:
        raise Exception("Wrong number of arguments!")
