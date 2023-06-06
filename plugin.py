import re
from pathlib import Path 
import os
import globals
class Plugin:
    """Main class to represent a plugin"""
    def __init__(self, pathstr: Path) -> None:
        #Do condition tests
        if not pathstr.is_dir():
            raise BaseException("Plugin folder is not a folder")
        self.meta = None
        self.mediaHandlers = None
        self.fileHandlers = None
        self.mediaNamePatterns = None
        print("Hey?")
        print(pathstr.absolute())

def ReloadPlugins() -> None:
    """Reload plugins, at both the plugin folder and set external plugin folder"""
    Plugin(Path("builtin"))

ReloadPlugins()

class MediaHandler():
    "Class to represent the sub media handlers of the plugin"
    pass

class MediaMatcher:
    exactMatching = {}
    regexMatching = {}

def DetectFolderMedia():
    """Detects the media that a folder belongs to"""
    #Get exact matches first

    #Use regex matching next
    pass

class FileHandlerBase():
    def HandleFile():
        """"""
        pass
    def LoadConfig(config: dict) -> None:
        """Loads the configuration for this handler"""
        pass