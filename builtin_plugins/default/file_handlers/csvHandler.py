"This module handles CSV files"
from __future__ import annotations
import csv
from io import TextIOWrapper
from pathlib import Path
from pprint import pprint

from OnlineTimeline.OTPlugin.Config import ConfigRoot, FileReaderConfig
from OnlineTimeline.OTPlugin.FileHandlerBase import FileHandlerBase
from OnlineTimeline.TimelineManager import Event

class BuiltinCSVHandler(FileHandlerBase):
    """The builtin handler for CSV files"""
    def __init__(self) -> None:
        super().__init__()
        
    def LoadConfig(self, config: TextIOWrapper) -> None:
        super().LoadConfig(config)
        self.typedConfig = ConfigRoot(self.config, CSVConfigRoot)
        
    def VerifyHeader(self):
        """Verifies the expected header field from config"""
        expectedHeader = self.config["expectedHeader"]
        if isinstance(expectedHeader, list):
            # Check that all values are in the Expected Header
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
        return self.eventArr
        




class CSVConfigRoot(FileReaderConfig):
    """Test Text"""
    def __init__(self, config: dict) -> None:
        self.config = config
        self.expectedHeader: list[str] = config["expectedHeader"]
    def __repr__(self):
        return f"{self.__class__.__name__}({self.config})"


if  __name__ == '__main__':
    handler = BuiltinCSVHandler()
    handler.UseCmdArguments()