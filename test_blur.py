import numpy as np
import cv2
import blur_1
import blur_2
import blur_3
from random import randint
from os import remove

"""
Simple unit tests for the blur implementations.
Checks that the blurred image's max color value is less than the original
and that the blur is done correctly for a randomly picked pixel
"""

class BlurTest:
    def test_max_values(blur_method):
        """
        Checks if the max color values of the blurred picture are less than the
        original picture
        Input:
            blur_method (module): An imported module that contains the method 
                .blur_image()
        """
        a_height = randint(40, 90)
        a_width = randint(40, 90)
        array1 = np.zeros((a_height, a_width, 3))
        for i in np.arange(a_height):
            for j in np.arange(a_width):
                for h in np.arange(3):
                    if (i<=a_height-1 and j <= a_width-1):
                        array1[i][j][h] = randint(0, 255)

        cv2.imwrite("test_image1.jpg", array1)
        array1 = cv2.imread("test_image1.jpg")
        array2 = blur_method.blur_image("test_image1.jpg")
        print("  Test 1/2: ", end="")
        assert np.amax(array1) > np.amax(array2), ("The blurred image's" +
            "max value is too high!")
        try:
            remove("test_image1.jpg")
        except: pass
        print("Passed.")

    def test_one_pixel(blur_method):
        """
        Checks if a randomly chosen pixel is actually the average of the ones
        around it from the original picture
        Input:
            blur_method (module): An imported module that contains the method 
                .blur_image()
        """
        a_height = randint(40, 90)
        a_width = randint(40, 90)
        array1 = np.zeros((a_height, a_width, 3))
        for h in np.arange(a_height):
            for w in np.arange(a_width):
                for c in np.arange(3):
                    array1[h][w][c] = randint(0, 255)

        cv2.imwrite("test_image1.jpg", array1)
        array2 = blur_method.blur_image("test_image1.jpg")
        h = randint(1, a_height-2)
        w = randint(1, a_width-2)
        print("  Test 2/2 :", end="")
        array1 = cv2.imread("test_image1.jpg")
        for c in range(3):
            pixel_avg = ((array1[h][w][c].astype("uint32") + array1[h-1][w][c] + 
            array1[h+1][w][c] + array1[h][w-1][c] + array1[h][w+1][c] + 
            array1[h-1][w-1][c] + array1[h-1][w+1][c] + array1[h+1][w-1][c] + 
            array1[h+1][w+1][c]) // 9)
            assert int(array2[h][w][c]) == pixel_avg, ("The randomly chosen pixel " +
                "was not correct!")
        try:
            remove("test_image1.jpg")
        except: pass
        print("Passed.")

if __name__ == "__main__":
    print("Testing blur_1:")
    BlurTest.test_max_values(blur_1)
    BlurTest.test_one_pixel(blur_1)
    print("Testing blur_2:")
    BlurTest.test_max_values(blur_2)
    BlurTest.test_one_pixel(blur_2)
    print("Testing blur_3:")
    BlurTest.test_max_values(blur_3)
    BlurTest.test_one_pixel(blur_3)
