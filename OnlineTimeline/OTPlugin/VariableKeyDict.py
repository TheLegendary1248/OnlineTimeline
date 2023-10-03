import argparse 
import re
from typing import TypeVar, Generic, Type

configType = TypeVar('configType')
class IsRegex(dict):
    """Class for representing dictionary keys that are purposely Regex"""
    def __init__(self) -> None:
        self.isRegex = False
    pass

class PatternKeyDict(Generic[configType], dict[str,configType]):
    """Class for representing dictionaries with keys that represent patterns"""
    def __init__(self, *args) -> None:
        super().__init__(*args)
    
    def FindKeysByRegex(self, pattern:str) -> [str]:
        r = re.compile(pattern)
        list(filter(r.match, self.keys()))
    
