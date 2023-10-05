"Builtin handler for CSV data. Outputs to dict"
from __future__ import annotations
import csv
from io import TextIOWrapper
from pprint import pprint
from OnlineTimeline.OTPlugin.Config import ConfigRoot, DataHandlerConfig
from OnlineTimeline.OTPlugin.DataHandlerBase import DataHandlerBase 
from OnlineTimeline.OTPlugin.VariableKeyDict import PatternKeyDict
from OnlineTimeline.OTPlugin.ValueConverter import ConversionConfig, ValueConverter
from OnlineTimeline.TimelineManager import Event


class BuiltinCSVHandler(DataHandlerBase):
    """The builtin handler for CSV files"""
    readBinary = False
    def __init__(self) -> None:
        super().__init__()
        
    def LoadConfig(self, config: TextIOWrapper) -> None:
        super().LoadConfig(config)
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
    
    def DoConversions(self):
        config = self.configRoot.config
        for i in range(len(self.dictArr)):
            dictObj = self.dictArr[i]
            for k,v in dictObj.items():
                matchedKeys = config.conversions.FindKeysByRegex(k)
                if len(matchedKeys) == 0:
                    continue
                if len(matchedKeys) > 1:
                    raise LookupError(f"Conversions regex matched more than one key: matches {matchedKeys}, key: {k}")
                conversionConfig = config.conversions[matchedKeys[0]]
                pprint(conversionConfig)
                dictObj[k] = ValueConverter.ConvertValue(conversionConfig.type, v, conversionConfig.config)
        pass

    def ToEvent(self):
        self.eventArr: list[Event] = []
        for dict in self.dictArr:
            time = dict.pop("time")
            self.eventArr.append(E)
        Event.AppendEvents([], "uber")
        pass
    def ProcessData(self, data: TextIOWrapper) -> None:
        """Process the given data"""
        self.csvreader = csv.DictReader(data)
        self.VerifyHeader()
        self.dictArr: list[dict[str,any]] = []
        for row in self.csvreader: 
            self.dictArr.append(row)
        self.DoConversions()
        self.ToEvent()
        return self.dictArr

class CSVConfigRoot(DataHandlerConfig):
    """Test Text"""
    def __init__(self, *args) -> None:
        super().__init__(*args)
        # TODO  this
        self.expectedHeader: list[str] = self["expectedHeader"]
        conversions = ShallowConversionConfig(self["conversions"])
        self["conversions"] = conversions
        self.conversions =  conversions
        toEvent = ToEventConfig(self["toEvent"])
        self["toEvent"] = toEvent
        self.toEvent =  toEvent
    def __repr__(self):
        return f"\n{self.__class__.__name__}({super(type(self), self).__repr__()})"

class ShallowConversionConfig(PatternKeyDict[ConversionConfig]):
    """Class for representing configuration for conversions, assuming the given dictionary isn't nested"""
    def __init__(self,*args) -> None:
        super().__init__(*args)
        self.LoadConfig()
        
    def LoadConfig(self):
        """Create proper wrappers for this dictionary's items"""
        for k,v in self.items():
            self[k] = ConversionConfig(v)
        pass

    def __repr__(self):
        return f"\n{self.__class__.__name__}({super(type(self), self).__repr__()})"

class ToEventConfig(dict):
    time: float | int
    endtime: float | int
    def __init__(self, *args) -> None:
        super().__init__(*args)
        time = self["time"]
        endtime = self["endtime"]


if  __name__ == '__main__':
    handler = BuiltinCSVHandler()
    handler.UseCmdArguments()
