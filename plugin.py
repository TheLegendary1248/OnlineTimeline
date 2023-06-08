"""This module contains all necessary logic about Plugins"""
from __future__ import annotations

import re
from pathlib import Path 
import os
import globals
from pprint import pprint
from configparser import ConfigParser


class Plugin:
    loadedPlugins: list[Plugin] = [] 
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
    @classmethod
    def ReloadPlugins(cls) -> None:
        """Reload plugins, at both the plugin folder and set external plugin folder"""
        cls.loadedPlugins.append(Plugin(Path("builtin")))

    
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
        self.data = dict(parser['data'].items())
        pprint(self.data)
        
    def GetFolderMedia(self, foldername: str) -> None:
        "Determine the media of a folder"
        detectedNames = []
        for mediaName, regMatch in self.data.items():
            pattern = re.compile(regMatch)
            if pattern.fullmatch(foldername):
                detectedNames.append(mediaName)

        return { foldername : detectedNames}

        #Test regex match

def DetectFolderMedia():
    """Detects the media that a folder belongs to"""
    for i in os.listdir(globals.CONFIG["DataLocation"]):
        pprint(Plugin.loadedPlugins[0].mediaNameMatch.GetFolderMedia(i))

Plugin.ReloadPlugins()
DetectFolderMedia()

class FileHandlerBase():
    def HandleFile():
        """"""
        pass
    def LoadConfig(config: dict) -> None:
        """Loads the configuration for this handler"""
        pass


