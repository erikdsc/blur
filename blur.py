from argparse import ArgumentParser
import cv2
import blur_1
import blur_2
import blur_3

"""
Simple command line interface for the blur implementations.

Usage:  python blur.py -src SOURCE_IMAGE [args]
"""

parser = ArgumentParser(description="Blurinator v1 \n ")
parser.add_argument("-src", required=True, help="The picture you wish to blur")
parser.add_argument("-method", default="3", type=int, 
                    help="What blur method to use [1/2/3]")
parser.add_argument("-dst", default="blurred_image.jpg", 
                    help="Filename for the blurred image")

args = parser.parse_args()
if (args.method == 1):
    blurred_image = blur_1.blur_image(args.src, args.dst)
elif (args.method == 2):
    blurred_image = blur_2.blur_image(args.src, args.dst)
elif(args.method == 3):
    blurred_image = blur_3.blur_image(args.src, args.dst)
else: 
    raise Exception("Invalid arguments")