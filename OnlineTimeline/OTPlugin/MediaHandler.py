
import json
from pathlib import Path
from configparser import ConfigParser
from pprint import pprint
import argparse
import re
import os

isMain = False
if __name__ == "__main__":
    isMain = True

class MediaHandler:
    "Class to represent the media matcher"
    def __init__(self, pathstr: Path) -> None:
        if not pathstr.is_file():
            raise BaseException("Media matcher is not a file")
        print(f'Got media_name_match at {pathstr}')
        parser = ConfigParser()
        parser.read(pathstr)
        self.data = dict(parser['data'].items())
        
        
    def GetFolderMedia(self, foldername: str) -> None:
        "Determine the media of a folder"
        detectedNames = []
        for mediaName, regMatch in self.data.items():
            pattern = re.compile(regMatch)
            if pattern.fullmatch(foldername):
                detectedNames.append(mediaName)
        # with open('folder-media', 'r+') as file:
        #     mediaData = json.load(file)
        #     mediaData.update(detectedNames)
        #     file.seek(0)
        #     json.dump(mediaData, file)
        
        return detectedNames

if isMain:
    parser = argparse.ArgumentParser(description=__doc__)
    #Input file
    parser.add_argument('file', type=Path,help="The path to the input ini file for matching media. If left alone, will just print the matcher")
    #Input string
    parser.add_argument('-test', type=str, help="A given string for the matcher to figure out which it belongs to")

    arguments = parser.parse_args()

    Matcher = MediaHandler(arguments.file)

    if arguments.test == None:
        pprint(Matcher.data)
    else:
        pprint(Matcher.GetFolderMedia(arguments.test))
        pass