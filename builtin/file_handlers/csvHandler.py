"This module handles CSV files"
import csv
import sys
import os
from pathlib import Path
from pprint import pprint
import argparse

if __name__ == '__main__':
    # Make sure import works
    sys.path.append(str(Path.cwd()))
    print("Running CSV Handler as main")

from plugin import FileHandlerBase
from TimelineManager import Event

#defaultDialect = csv.Dialect()

class BuiltinCSVHandler(FileHandlerBase):
    """The builtin handler for CSV files"""
    def __init__(self) -> None:
        super().__init__()
        self.firstField = "skip"
        self.fields = []

    def LoadConfig(config: dict) -> None:
        super().LoadConfig()
        self.config = config

    def CreateEvents() -> None:
        events = []

        pass

if  __name__ == '__main__':
    #Setup cmd line parsing
    parser = argparse.ArgumentParser(description=__doc__)
    #Input file
    parser.add_argument('f', help="The path to the input csv file")
    #Input config (if not the default dialect)
    parser.add_argument('-c', help="The path to the input config json")
    #Output file
    parser.add_argument('-o')
    parser.parse_args()
