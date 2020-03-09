#!/usr/bin/env python

from argparse import ArgumentParser
import traceback
import csv
import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from utils import FileUtils
from image import compare_images


class ImageDiff:

    def __init__(self):
        self.input_file = None
        self.output_file = "output.csv"

    def parse_arguments(self):
        parser = ArgumentParser()
        parser.add_argument("--input-file", dest="input_file",
                            help="Input CSV File location", required=True)
        parser.add_argument("--output-file", "-o", dest="output_file",
                            help="Output CSV File Location", required=False)
        args = parser.parse_args()
        return args

    def process_images(self, input_file):
        with open(input_file) as input_csv:
            csv_reader = csv.reader(input_csv, delimiter=' ')
            line_count = 0
            with open(self.output_file, 'w') as output_csv:
                csv_writer = csv.writer(output_csv, delimiter=' ')
                for row in csv_reader:
                    line_count += 1
                    if line_count > 1:
                        ts = time.time()
                        image_1 = row[0]
                        image_2 = row[1]
                        image_score = compare_images(image_1, image_2)
                        task_duration = round((time.time() - ts), 2)
                        csv_writer.writerow([image_1, image_2, image_score, task_duration])
                        # print(f"Image Result => {image_score} in {task_duration}")
                    else:
                        csv_writer.writerow(["image1", "image2", "similar", "elapsed"])
            print(f'Processed {line_count - 1} files.')

    def main(self):
        try:
            print("Parsing Arguments")
            args = self.parse_arguments()
            self.input_file = args.input_file
            if args.output_file:
                self.output_file = args.output_file

            if FileUtils.file_exists(self.input_file):
                self.process_images(self.input_file)
                print("Image Diff Done")
            else:
                print(f"Couldn't find input file => {self.input_file}")
        except Exception as ex:
            print(traceback.format_exc())
            print(f"Exception occurred => {ex}")


if __name__ == "__main__":
    ImageDiff().main()
