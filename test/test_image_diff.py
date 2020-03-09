import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from image_diff.image_diff import ImageDiff
from utils import *


class ImageDiffTest(unittest.TestCase):

    def setUp(self):
        print(f"{self.__class__.__name__} is starting...")

    def tearDown(self):
        print(f"Tearing down {self.__class__.__name__} resources...")

    def test_process_images(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        print(f"Current Working Directory is => {current_dir}")
        input_file = f"{current_dir}/test/input.csv"
        output_file = f"{current_dir}/test/output.csv"
        ImageDiff().process_images(input_file)
        assert os.path.exists(output_file) == 1


if __name__ == '__main__':
    unittest.main()
