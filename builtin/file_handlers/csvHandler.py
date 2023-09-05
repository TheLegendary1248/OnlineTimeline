"This module handles CSV files"
import csv
import sys
from io import TextIOWrapper
import os
from pathlib import Path
from pprint import pprint
import argparse
from typing import TypedDict

if __name__ == '__main__':
    # Make sure import works
    # sys.path.append(str(Path.cwd()))
    pprint(sys.path)
    print("Running CSV Handler as main")

from OnlineTimeline.plugin.FileHandlerBase import FileHandlerBase
from OnlineTimeline.TimelineManager import Event
#defaultDialect = csv.Dialect()

class CSVConfig(TypedDict):
    config: dict

#TODO Use 'expected' header to certify csv header

class BuiltinCSVHandler(FileHandlerBase):
    """The builtin handler for CSV files"""
    def __init__(self) -> None:
        super().__init__()
        self.config = None

    def LoadConfig(self, config: TextIOWrapper) -> None:
        super().LoadConfig(config)
        
    def VerifyHeader(self):
        """Verifies the expected header field from config"""
        expectedHeader = self.config["expectedHeader"]
        if isinstance(expectedHeader, list):
            if not all([val in self.csvreader.fieldnames for val in expectedHeader]):
                raise BaseException(f"Expected header does not match that found in {self.csvreader}")
        else:
            print("No given header for verification")
        
    def CreateEvents(self, file: TextIOWrapper) -> None:
        self.csvreader = csv.DictReader(file)
        self.eventArr: list[Event] = []
        for row in self.csvreader: 
            for i in range(0):
                pass
                # Run conversions
            self.eventArr.append(Event(timestamp=row["Request Time"],data=row))
            pass
        for event in self.eventArr:
            print(str(event.data))

if  __name__ == '__main__':
    handler = BuiltinCSVHandler()
    handler.UseCmdArguments()
    
    
    
