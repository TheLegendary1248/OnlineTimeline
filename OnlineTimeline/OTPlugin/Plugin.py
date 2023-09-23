"""This module contains all necessary logic about Plugins"""
from __future__ import annotations

from pathlib import Path 
import os
from OnlineTimeline import globals

import sys
from pprint import pprint

import argparse
from OnlineTimeline.OTPlugin import MediaHandler, FileHandlerBase
#TODO Figure out if to use jsonschema and how


#UNNAMEDMARKER: Possibly use a json for individual config
pluginResourcePaths = {
    "mediaNameMatch" : "media_name_match.ini",
    "fileHandlers" : "file_handlers"
}

class Plugin:
    loadedPlugins: list[Plugin] = [] 
    """Main class to represent a plugin"""
    def __init__(self, pathstr: Path) -> None:
        #Do condition tests
        if not pathstr.is_dir():
            raise BaseException("Plugin folder is not a folder")
        print(f'Got plugin at {pathstr.absolute()}')
        self.fileHandlers = None
        """Python files that handle processing the users data into OnlineTimeline's format"""
        self.mediaNameMatch = MediaHandler.MediaHandler(pathstr / pluginResourcePaths["mediaNameMatch"])
        """Config for matching folders to their corresponding media type"""
    @classmethod
    def ReloadPlugins(self) -> None:
        """Reload plugins, at both the plugin folder and set external plugin folder"""
        self.loadedPlugins.append(Plugin(Path("builtin_plugins/default")))
        
    def ReloadThisPlugin(self) -> None:
        raise NotImplementedError()


def DetectFolderMedia():
    """Detects the media that a folder belongs to"""
    for i in os.listdir(globals.CONFIG["DataLocation"]):
        pprint(Plugin.loadedPlugins[0].mediaNameMatch.GetFolderMedia(i))


def ReloadPlugins():
    Plugin.ReloadPlugins()

##Plugin.ReloadPlugins()
#Process command line arguments for function testing
if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 1:
        print("No arguments were given. Testing loading of plugins")
        ReloadPlugins()
        os._exit(0)
        # Plugin.ReloadPlugins()
    # print('plugin cannot run on its own')
    # os._exit(0)
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