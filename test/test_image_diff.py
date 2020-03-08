import os, sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from image_diff.image_diff import ImageDiff


class ImageDiffTest(unittest.TestCase):

    def setUp(self):
        print(f"{self.__class__.__name__} is starting...")

    def tearDown(self):
        print(f"Tearing down {self.__class__.__name__} resources...")

    def test_process_images(self):
        input_file = "input.csv"
        output_file = "output.csv"
        ImageDiff().process_images(input_file)
        assert os.path.exists(output_file) == 1


if __name__ == '__main__':
    unittest.main()
