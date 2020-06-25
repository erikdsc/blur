import cv2
import numpy as np

def blur_image_subsection(src, x1, y1, width, height, dst=None):
    """
    A function that utilizes vectorization to blur a subsection of an image
    array.
    Input: 
        src (str): An image that you want to blur
        x1 (int): The number of pixels from the left til the subsection is
            reached.
        y1 (int): The number of pixels from the top til the subsection is
            reached.
        width (int): The width of the subsection in pixels.
        height (int): The height of the subsection in pixels. 
        dst (str): The name for the newly blurred image. Defaults to not saving
            the image
    Output:
        An array containing the source image with a layer of blur applied to the
        specified subsection.
    """
    #converting to 32 bit prevents overflow when calculating the averages
    src = src.astype("uint32")
    blurred_image = src.copy()
    #padding the source image so there's adjacent pixels to use in the 
    #calculation for the edges
    src = np.pad(src, ((1,1),(1,1),(0,0)), "edge")

    #vectorization that calculates the average of all adjacent pixels for the
    #pixels between (x1, y1) and (x1+width, y1+height)
    array1 = src[y1:y1+height, x1:x1+width]
    array2 = src[y1+1:y1+height+1, x1:x1+width]
    array3 = src[y1+2:y1+height+2, x1:x1+width]
    array4 = src[y1:y1+height, x1+1:x1+width+1]
    array5 = src[y1+2:y1+height+2, x1+1:x1+width+1]
    array6 = src[y1:y1+height, x1+2:x1+width+2]
    array7 = src[y1+1:y1+height+1, x1+2:x1+2+width]
    array8 = src[y1+2:y1+height+2, x1+2:x1+2+width]
    blurred_image[y1:y1+height, x1:x1+width] = (src[y1+1:y1+height+1,
        x1+1:x1+width+1] + array1 + array2 + array3 + array4 + array5 + array6 +
         array7 + array8) // 9
    
    #converting back to 8 bit so cv2 can handle the array
    blurred_image = blurred_image.astype("uint8")
    if (dst != None):
        cv2.imwrite(dst, blurred_image)
    return blurred_image