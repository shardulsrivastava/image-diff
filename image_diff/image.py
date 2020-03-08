#!/usr/bin/env python

import cv2
from skimage.metrics import structural_similarity


def compare_images(image_1, image_2):
    image_1 = cv2.cvtColor(cv2.imread(image_1), cv2.COLOR_BGR2GRAY)
    image_2 = cv2.cvtColor(cv2.imread(image_2), cv2.COLOR_BGR2GRAY)

    return 1 - ((1 + structural_similarity(image_1, image_2)) / 2)
