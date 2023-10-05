import argparse 
import re
from typing import TypeVar, Generic, Type

configType = TypeVar('configType')
class IsRegex(dict):
    """Class for representing dictionary keys that are purposely Regex"""
    def __init__(self) -> None:
        self.isRegex = False
    pass


    
class PatternKey(str):
    regex: re.Pattern
    def __new__(cls, value):
        obj = str.__new__(cls, value)
        obj.regex = re.compile(value)
        return obj
    
    
class PatternKeyDict(Generic[configType], dict[PatternKey,configType]):
    """Class for representing dictionaries with keys that represent patterns"""
    def __init__(self, *args) -> None:
        super().__init__(*args)
        # This indeed works https://www.grepper.com/answers/533612/how+to+replace+single+string+in+all+dictionary+keys+in+python?ucard=1
        converted = {PatternKey(key) : value for key,value in self.items()}
        self.clear()
        self.update(converted)
    
    def FindKeysByRegex(self, value:str) -> list[str]:
        # Get a list of all keys that match, None where it does not
        k = [key if key.regex.match(value) else None for key in self.keys()]
        # Filter out None's
        return list(filter(None, k))