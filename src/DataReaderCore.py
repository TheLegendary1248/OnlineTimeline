##Not sure, im still thinking about it
import globals
from pathlib import Path
import json
import os
import datetime

savePath = Path(globals.CONFIG["SaveLocation"])

timelinePath = savePath / "timeline"
objectsPath = savePath / "objects"
resources = savePath / "resources" 

class PathStruct():
    """Representation of ..."""
    def __init__(self, dict):
        self.isFile = False
        """Is this path a file?"""
        self.isRegex = False
        """Is the path a regex string"""
        self.desc = ""
        """The description of this file"""

        pass

def GetAllPaths():
    """Get everything in a directory, literally"""
    pass

def GetPathConfig():
    """Get the config for a specific path"""
    pass

def ProcessMediaFolder():
    
    # If not enough config is given
    if False:
        ## Folder/File exists, but config is not given
        message = f"{'FILENAME'} exists, but config is incomplete"
    if False: 
        ##Folder
        pass

def UpdateCompletionCache():
    
    pass

print("Hello")
import sys
print(sys.stdout)