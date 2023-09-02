
import json
from pathlib import Path
from configparser import ConfigParser

class MediaHandler:
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