"This module handles CSV files"
from __future__ import annotations
import csv
from io import TextIOWrapper
from pathlib import Path
from pprint import pprint

from OnlineTimeline.OTPlugin.Config import ConfigRoot, DataHandlerConfig
from OnlineTimeline.OTPlugin.DataHandlerBase import DataHandlerBase
from OnlineTimeline.TimelineManager import Event

class BuiltinDictHandler(DataHandlerBase):
    """The builtin handler for Python dict objects"""
    def __init__(self) -> None:
        super().__init__()
        
    def LoadConfig(self, config: TextIOWrapper) -> None:
        super().LoadConfig(config)
        self.typedConfig = ConfigRoot(self.config, DictConfigRoot)
        
    def ProcessData(self, data: TextIOWrapper) -> None:
        self.eventArr = []
        return self.eventArr

class DictConfigRoot(DataHandlerConfig):
    """Test Text"""
    def __init__(self, config: dict) -> None:
        self.config = config
    def __repr__(self):
        return f"{self.__class__.__name__}({self.config})"

if  __name__ == '__main__':
    handler = BuiltinDictHandler()
    handler.UseCmdArguments()