# TODO: Create static function for getting all subclasses via https://stackoverflow.com/questions/3862310/how-to-find-all-the-subclasses-of-a-class-given-its-name
from __future__ import annotations
import argparse

class ValueConverter():
    """This class is for value conversions, usually for parsing strings"""
    registered:dict = {}
    def __init__(self) -> None:
        pass
    
    def LoadConfig(self) -> None:
        pass
    def ConvertValue(self, val) -> None:
        pass
    @staticmethod
    def registerConverter(name: str, c: ValueConverter):
        """Register a converter with a name"""
        ValueConverter.registered[name] = c
        pass

    @staticmethod
    def convertValue(name: str, val, config: dict):
        """Convert the value with said config"""
        converter = ValueConverter.registered[str]
        pass

class TimeConverter(ValueConverter):
    def ConvertValue(self, val) -> None:
        
        return
    def LoadConfig(self, val: dict) -> None:
        return super().LoadConfig()
        # return super().ConvertValue(val)
    pass

class EnumConverter(ValueConverter):
    def ConvertValue(self, val) -> None:
        values: dict = None
        return values["val"]
        # return super().ConvertValue(val)
    pass

all_subclasses = ValueConverter.__subclasses__()
if __name__ == '__main__':
    print(all_subclasses)
