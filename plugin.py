import re
from pathlib import Path 
import os
import globals
from pprint import pprint
from configparser import ConfigParser


class Plugin:
    """Main class to represent a plugin"""
    def __init__(self, pathstr: Path) -> None:
        #Do condition tests
        if not pathstr.is_dir():
            raise BaseException("Plugin folder is not a folder")
        print(f'Got plugin at {pathstr}')
        self.meta = None
        self.mediaHandlers = None
        self.fileHandlers = None
        self.mediaNameMatch = MediaMatcher(pathstr / "media_name_match.ini")

class MediaHandler:
    "Class to represent the sub media handlers of the plugin"
    def __init__(self, pathstr: Path) -> None:
        pass
    pass

class MediaMatcher:
    "Class to represent the media matcher"
    def __init__(self, pathstr: Path) -> None:
        if not pathstr.is_file():
            raise BaseException("Media matcher is not a file")
        print(f'Got media_name_match at {pathstr}')
        parser = ConfigParser()
        parser.read(pathstr)
        self.exact = dict(parser['exact'].items())
        pprint(self.exact)
        self.regex = dict(parser['regex'].items())
        pprint(self.regex)
        
    def GetFolderMedia(self, foldername) -> None:
        "Determine the media of a folder"
        mediaNames = []
        for mediaName, exMatch in self.exact:
            if exMatch == foldername:
                mediaNames.append(mediaNames)
        for mediaName, regMatch in self.regex:
            pattern = re.compile(regMatch)
            if pattern.fullmatch(pattern):
                mediaNames.append[mediaName]
        return { foldername : mediaNames}

        #Test regex match

def DetectFolderMedia():
    """Detects the media that a folder belongs to"""
    #Get exact matches first
    for i in os.listdir(globals.CONFIG["DataLocation"]):
        print()
    #Use regex matching next
    pass

DetectFolderMedia()

class FileHandlerBase():
    def HandleFile():
        """"""
        pass
    def LoadConfig(config: dict) -> None:
        """Loads the configuration for this handler"""
        pass

def ReloadPlugins() -> None:
    """Reload plugins, at both the plugin folder and set external plugin folder"""
    Plugin(Path("builtin"))

ReloadPlugins()