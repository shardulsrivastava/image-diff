#!/usr/bin/env python

import os.path


class FileUtils:

    @staticmethod
    def file_exists(file_location):
        return os.path.isfile(file_location)

    @staticmethod
    def read_local_file(file_path):
        if FileUtils.file_exists(file_path):
            with open(file_path) as f:
                try:
                    lines = f.read()
                except IOError:
                    ErrorUtils.print_error_and_exit("Couldn't read file => {}".format(file_path))
        else:
            ErrorUtils.print_error_and_exit("Couldn't find file => {}".format(file_path))

        return lines


class ErrorUtils:

    @staticmethod
    def print_error_and_exit(message):
        print(message)
        exit(1)
