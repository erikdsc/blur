import cv2
import sys
from blur_subsection import blur_image_subsection

"""
Usage:
    python3 blur_faces.py [source_image_to_blur] [name_for_blurred_image]
    (the name argument is optional)
"""

def blur(src, dst=None):
    """
    Blurs all faces that are detected until there are no faces left in the image
    Input:
        src (str): A filepath that points to the image that you want to remove
            faces from.
        dst (str): A filename to give the image with blurred faces. If nothing
            is specified, it will not create an image.
    Output:
        An array containing the image with faces blurred.
    """
    image = cv2.imread(src)
    #Detects faces and stores it in the faces variable
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor =1.025 ,
        minNeighbors =5 ,
        minSize =(30, 30)
    )
    try:
        #applies a level of blur to all detected faces while there are faces
        while (faces.any()):
            for (x, y, w, h) in faces:
                print(("Applying a layer of blur to face found at: x1:%i, " +
                    "y1:%i, x2:%i, y2:%i") % (x, y, x+w, y+h))
                image = blur_image_subsection(image, x, y, w, h)
            faces = faceCascade.detectMultiScale(
                image,
                scaleFactor =1.025 ,
                minNeighbors =5 ,
                minSize =(30, 30)
            )
    finally:
        if (dst != None):
            cv2.imwrite(dst, image)
            print("Blurred image saved to \"" + dst + "\".")
        return image

if __name__ == "__main__":
    #Assumes sys.argv[1] is source image and sys.argv[2] is destination
    if (len(sys.argv) == 2):
        blur(sys.argv[1])
    elif (len(sys.argv) == 3):
        blur(sys.argv[1], sys.argv[2])
    else:
        raise Exception("Wrong number of arguments!")