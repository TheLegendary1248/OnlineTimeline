"Builtin handler for Python Dict Objects. Outputs to Event"
from __future__ import annotations
from io import TextIOWrapper
from pathlib import Path
from pprint import pprint
import pickle

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
        self.dictsArr = pickle.load(data)
        self.eventArr = []
        return self.dictsArr

class DictConfigRoot(DataHandlerConfig):
    """Test Text"""
    def __init__(self, config: dict) -> None:
        self.config = config
    def __repr__(self):
        return f"{self.__class__.__name__}({self.config})"

if  __name__ == '__main__':
    handler = BuiltinDictHandler()
    handler.UseCmdArguments()