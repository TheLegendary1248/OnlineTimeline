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
    sys.path.append(str(Path.cwd()))
    print("Running CSV Handler as main")

from plugin import FileHandlerBase
from TimelineManager import Event

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
        expectedHeader = self.config["config"]["expectHeader"]
        if isinstance(expectedHeader, list):
            if not all([val in self.csvreader.fieldnames for val in expectedHeader]):
                raise BaseException(f"Expected header does not match that found in {self.csvreader}")
        else:
            print("No given header for verification")
        
    def CreateEvents(self, file: TextIOWrapper) -> None:
        self.csvreader = csv.DictReader(file)
        self.eventArr = []
        for row in self.csvreader:    
            self.eventArr.append(Event(timestamp=row["Request Time"],data=row))
            pass
        pprint(self.eventArr)

if  __name__ == '__main__':
    #Setup cmd line parsing
    parser = argparse.ArgumentParser(description=__doc__)
    #Input file
    parser.add_argument('file', type=open,help="The path to the input csv file")
    #Input config (if not the default dialect)
    parser.add_argument('-config', type=open,help="The path to the input config json")
    #Output file
    parser.add_argument('-output', help="The output file")
    #Output limit
    parser.add_argument('-limit',type=int)
    #If send to timeline
    arguments = parser.parse_args()
    #Create handler instance
    handler = BuiltinCSVHandler()
    
    ##INSERT OPTIONALS HERE
    if arguments.config != None:
        handler.LoadConfig(arguments.config)
    #Run logic
    handler.CreateEvents(arguments.file)
    
    Event.AppendEvents(handler.eventArr, "Uber")
    
