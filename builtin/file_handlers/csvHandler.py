import csv
import sys
import os
from pathlib import Path
from pprint import pprint

if __name__ == '__main__':
    # Make sure import works
    sys.path.append(str(Path.cwd()))
    print("Running CSV Handler as main")

from plugin import FileHandlerBase
from TimelineManager import Event

defaultDialect = None

class BuiltinCSVHandler(FileHandlerBase):
    """The builtin handler for CSV files"""
    def __init__(self) -> None:
        super().__init__()
        self.firstField = "skip"
        self.fields = []

    def LoadConfig(config: dict) -> None:
        super().LoadConfig()
        if "firstField" in config:
            self.firstField = config["firstField"]
        if self.firstField != "use": 
            self.fields = config["fields"]

    def CreateEvents() -> None:
        

        pass

##Use the second argument as target file, and third argument as target config 
if  __name__ == '__main__':
    with open(sys.argv[1], newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            event = Event()
            print(', '.join(row))
    

