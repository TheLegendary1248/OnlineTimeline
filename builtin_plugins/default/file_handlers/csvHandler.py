"Builtin handler for CSV data. Outputs to dict"
from __future__ import annotations
import csv
from io import TextIOWrapper, IOBase
from pathlib import Path
from pprint import pprint

from OnlineTimeline.OTPlugin.Config import ConfigRoot, DataHandlerConfig
from OnlineTimeline.OTPlugin.DataHandlerBase import DataHandlerBase, VariableKeyDict

class BuiltinCSVHandler(DataHandlerBase):
    """The builtin handler for CSV files"""
    readBinary = False
    def __init__(self) -> None:
        super().__init__()
        
    def LoadConfig(self, config: TextIOWrapper) -> None:
        super().LoadConfig(config)
        self.typedConfig = ConfigRoot(self.config, CSVConfigRoot)
        
    def VerifyHeader(self):
        """Verifies the expected header field from config"""
        expectedHeader = self.typedConfig.config.expectedHeader
        if expectedHeader == None:
            print("Config does not include Expected Header")
            return
        if isinstance(expectedHeader, list):
            # Check that all values are in the Expected Header
            if not all([val in self.csvreader.fieldnames for val in expectedHeader]):
                raise BaseException(f"Expected header does not match that found in {self.csvreader}")
        else:
            print("No given header for verification")
        
    def ProcessData(self, data: TextIOWrapper) -> None:
        
        self.csvreader = csv.DictReader(data)
        self.dictArr: list[dict] = []
        for row in self.csvreader: 
            self.dictArr.append(row)
        return self.dictArr
        




class CSVConfigRoot(DataHandlerConfig):
    """Test Text"""
    def __init__(self, config: dict) -> None:
        self.config = config
        self.expectedHeader: list[str] = config["expectedHeader"]
        self.conversions =  ShallowConversionConfig(config["conversions"])
    def __repr__(self):
        return f"{self.__class__.__name__}({self.config})"

class ShallowConversionConfig(VariableKeyDict):
    """Class for representing config for conversions"""
    def __init__(self, config: dict) -> None:
        self.config = config
    def __repr__(self):
        return f"{self.__class__.__name__}({self.config})"

if  __name__ == '__main__':
    handler = BuiltinCSVHandler()
    handler.UseCmdArguments()