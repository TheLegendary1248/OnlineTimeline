"""This module contains all necessary logic about Plugins"""
from __future__ import annotations

import re
from pathlib import Path 
import os
import globals
from pprint import pprint
from configparser import ConfigParser
import argparse
import sys
import json
from typing import TypedDict, Any
#TODO Figure out if to use jsonschema and how

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
    def ReloadPlugins(self) -> None:
        """Reload plugins, at both the plugin folder and set external plugin folder"""
        self.loadedPlugins.append(Plugin(Path("builtin")))

    
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
        with open('folder-media', 'r+') as file:
            mediaData = json.load(file)
            mediaData.update(detectedNames)
            file.seek(0)
            json.dump(mediaData, file)
        
        return detectedNames

        #Test regex match

def DetectFolderMedia():
    """Detects the media that a folder belongs to"""
    for i in os.listdir(globals.CONFIG["DataLocation"]):
        pprint(Plugin.loadedPlugins[0].mediaNameMatch.GetFolderMedia(i))

class HandlerConfigBase(TypedDict):
    config: Any
    """The config for the"""

class FileHandlerBase():
    """Base class for all file type handlers that """
    def __init__(self, config: dict=None) -> None:
        if config != None:
            self.LoadConfig(config)
        pass
    def HandleFile():
        """"""
        pass
    def LoadConfig(self, config: dict) -> None:
        """Loads the configuration for this handler"""
        #Ensure type here
        self.config = json.load(config)
        pass

##Plugin.ReloadPlugins()
#Process command line arguments for function testing
if __name__ == '__main__':
    print('plugin cannot run on its own')
    os._exit(0)
    #Setup cmd line parsing
    parser = argparse.ArgumentParser(description=__doc__)
    #Input file
    parser.add_argument('file', type=open,help="The path to the input csv file")
    #Input config (if not the default dialect)
    parser.add_argument('-config', type=open,help="The path to the input config json")
    #Output file
    parser.add_argument('-output', help="The output file")
    #Output limit
    parser.add_argument('-limit',type=int)
    #If send to timeline
    arguments = parser.parse_args()
    #Create handler instance
    handler = BuiltinCSVHandler()
    
    ##INSERT OPTIONALS HERE
    if arguments.config != None:
        handler.LoadConfig(arguments.config)
    #Run logic
    handler.CreateEvents(arguments.file)
    
    Event.AppendEvents(handler.eventArr, "Uber")
        
    
