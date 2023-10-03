import argparse 
import re
class IsRegex(dict):
    """Class for representing dictionary keys that are purposely Regex"""
    def __init__(self) -> None:
        self.isRegex = False
    pass

class PatternKeyDict(dict):
    """Class for representing dictionaries with keys that represent patterns"""
    def __init__():
        pass
    
    def FindKeysByRegex(self, pattern:str) -> [str]:
        r = re.compile(pattern)
        list(filter(r.match, self.keys()))

    pass