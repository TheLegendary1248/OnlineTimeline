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

