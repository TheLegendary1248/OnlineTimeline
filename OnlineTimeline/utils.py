"""This module contains utility things for me that i homebrewed"""
from __future__ import annotations
from pathlib import Path

def EnsurePath(path: Path):
    """Get the file or folder at said path, or create one if not present"""
    if path.exists():
        pass
    else:
        ##Get path
        if(path.is_dir()):
            path.mkdir(parents=True, exist_ok=True)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)

class ObjectTraverse:
    """This is a simple class for getting around objects in python, intended to be used in config"""
    def __init__(self, config=dict) -> None:
        pass
    
    ##Init
    ##Config Reading
    ##
    pass

class THINGY:
    """This class should be an interface for object traversal"""
    
class ValueConverter:
    """This class is for value conversions, usually for parsing strings"""
    registered:dict = {}
    def __init__(self) -> None:
        pass
    """An array of registered converters"""
    
    def convertValue(self, val, config):
        pass
    @staticmethod
    def registerConverter(name: str,c: ValueConverter):
        """Register a converter with a name"""
        ValueConverter.registered[name] = c
        pass

    @staticmethod
    def convertValue(name: str, val, config: dict):
        """Convert the value with said config"""
        converter = ValueConverter.registered[str]
        
        pass

class TimeConverter(ValueConverter):
    """Class """
    def convertValue(self, val, config):
        print("HEY")
        pass

ValueConverter.registerConverter("time", TimeConverter)