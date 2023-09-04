"""This module contains all necessary logic about Plugins"""
from __future__ import annotations

from pathlib import Path 
import os
from OnlineTimeline import globals

from pprint import pprint

import argparse
from OnlineTimeline.plugin import MediaHandler, FileHandlerBase
#TODO Figure out if to use jsonschema and how

print("Plugin loaded")
class Plugin:
    loadedPlugins: list[Plugin] = [] 
    """Main class to represent a plugin"""
    def __init__(self, pathstr: Path) -> None:
        #Do condition tests
        if not pathstr.is_dir():
            raise BaseException("Plugin folder is not a folder")
        print(f'Got plugin at {pathstr}')
        self.fileHandlers = None
        self.mediaNameMatch = MediaHandler(pathstr / "media_name_match.ini")
    @classmethod
    def ReloadPlugins(self) -> None:
        """Reload plugins, at both the plugin folder and set external plugin folder"""
        self.loadedPlugins.append(Plugin(Path("builtin")))
        #Test regex match

def DetectFolderMedia():
    """Detects the media that a folder belongs to"""
    for i in os.listdir(globals.CONFIG["DataLocation"]):
        pprint(Plugin.loadedPlugins[0].mediaNameMatch.GetFolderMedia(i))


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
        
    
