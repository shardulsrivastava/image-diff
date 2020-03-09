import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from image_diff.image import *


class ImageTest(unittest.TestCase):

    def setUp(self):
        print(f"{self.__class__.__name__} is starting...")

    def tearDown(self):
        print(f"Tearing down {self.__class__.__name__} resources...")

    def test_process_images(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        image_1 = f"{current_dir}/test/dp.png"
        image_2 = f"{current_dir}/test/dp.png"
        assert compare_images(image_1, image_2) == 0


if __name__ == '__main__':
    unittest.main()
