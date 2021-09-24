from os import listdir
from os.path import isfile, join

import io
from PIL import Image
from PIL import ImageCms

"""
img = cv.imread("debug/243.295.png")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k != None:
    sys.exit()
"""

path_custom = "CustomBattlers"
path_debug = "debug"
bad_fusions = []


main_path = path_custom


TEST_SIZE = True
VERBOSE_MODE = False


def is_valid_size(image):
    return image.size == (288,288)


def analyze_sprite(element):
    fusion_name = element[:-4]
    try:
        image = Image.open(join(main_path, element))
        
    except Exception as e:
        print(fusion_name, "[UNKOWN FILE ERROR]", e)
    else:
        if TEST_SIZE and not is_valid_size(image):
            print(fusion_name, "[SIZE ERROR]", image.size)
        else:
            if VERBOSE_MODE:
                print(fusion_name, "[OK]")
        image.close()
        



    """
    import cv2 as cv
    import sys
    img = cv.imread(join(main_path, element), cv.IMREAD_UNCHANGED )
    if img is None:
        sys.exit("Could not read " + element)
    print(fusion_name, img.shape)
    alpha = img[:, :, -1]
    bgr = img[:, :, 0:3]
    binary = ~alpha
    cv.imshow(element, binary)
    k = cv.waitKey(0)
    """


def explore_sprites():
    print("[ START ]")
    print(" ")
    for element in listdir(main_path):
        if isfile(join(main_path, element)) and element.endswith(".png"):
            analyze_sprite(element)
    print(" ")
    print("[ END ]")


explore_sprites()

# analyze_sprite("243.315.png")

