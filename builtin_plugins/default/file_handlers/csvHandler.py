"Builtin handler for CSV data. Outputs to dict"
from __future__ import annotations
import csv
from io import TextIOWrapper, IOBase
from pathlib import Path
from pprint import pprint

from OnlineTimeline.OTPlugin.Config import ConfigRoot, DataHandlerConfig
from OnlineTimeline.OTPlugin.DataHandlerBase import DataHandlerBase 
from OnlineTimeline.OTPlugin.VariableKeyDict import PatternKeyDict
from OnlineTimeline.OTPlugin.ValueConverter import ConversionConfig
from collections import UserDict


class BuiltinCSVHandler(DataHandlerBase):
    """The builtin handler for CSV files"""
    readBinary = False
    def __init__(self) -> None:
        super().__init__()
        
    def LoadConfig(self, config: TextIOWrapper) -> None:
        super().LoadConfig(config)
        self.typedConfig = ConfigRoot(CSVConfigRoot, self.configRoot)
        self.configRoot = ConfigRoot(CSVConfigRoot, self.configRoot)
        
    def VerifyHeader(self):
        """Verifies the expected header field from config"""
        expectedHeader = self.configRoot.config.expectedHeader
        if expectedHeader == None:
            print("Config does not include Expected Header")
            return
        if isinstance(expectedHeader, list):
            # Check that all values are in the Expected Header
            if not all([val in self.csvreader.fieldnames for val in expectedHeader]):
                raise BaseException(f"Expected header does not match that found in {self.csvreader}")
            else:
                print("Header is verified")
        else:
            print("No given header for verification")
    
    def DoConversions():
        
        pass

    def ProcessData(self, data: TextIOWrapper) -> None:
        self.csvreader = csv.DictReader(data)
        self.VerifyHeader()
        self.dictArr: list[dict] = []
        for row in self.csvreader: 
            self.dictArr.append(row)
        self.DoConversions()
        return self.dictArr

class CSVConfigRoot(DataHandlerConfig):
    """Test Text"""
    def __init__(self, config: dict) -> None:
        self.configRoot = config
        self.expectedHeader: list[str] = config["expectedHeader"]
        self.conversions =  ShallowConversionConfig(config["conversions"])
    def __repr__(self):
        return f"{self.__class__.__name__}({self.configRoot})"

class ShallowConversionConfig(PatternKeyDict[ConversionConfig]):
    """Class for representing configuration for conversions, assuming the given dictionary isn't nested"""
    def __init__(self,*args):
        super().__init__(*args)
        self.LoadConfig()
        
    def LoadConfig(self):
        """Create proper wrappers for this dictionary's items"""
        for k,v in self.items():
            self[k] = ConversionConfig(v)
        pass
    def __repr__(self):
        return f"{self.__class__.__name__}({self.configRoot})"

if  __name__ == '__main__':
    handler = BuiltinCSVHandler()
    handler.UseCmdArguments()