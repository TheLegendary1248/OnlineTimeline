## This file deals with
import globals
from pathlib import Path
import json
import os
import datetime

savePath = Path(globals.CONFIG["SaveLocation"])

timelinePath = savePath / "timeline"
objectsPath = savePath / "objects"



class Event:
    """Represents a data point, or that sorta of thing"""
    def __init__(self, id, timestamp, content) -> None:
        self.timestamp = timestamp
        """The time at which this event happened"""
        self.content = content
        """The content regarding this event"""
        self.id = id
        """The unique id for this event"""
    def toObject(self) -> object:
        """Converts the Event into it's appropiate JSON object"""
        obj = {
            self.id :
            {
                "time" : self.timestamp,
                "data" : self.content,
            }
        }
        return obj

def AppendDay(date: datetime.datetime):
    """Appends onto the day file"""
    fileDayPath = timelinePath / f"{date.year}/{date.month}/{date.day}.json"
    EnsurePath(fileDayPath)
    file = fileDayPath.open("w")
    #Get day as an object
    dayObject = dict()
    events = dict()
    dayObject.update(events)

    json.dump(dayObject, file)

    file.flush()
    file.close()
    pass



def SaveEvents(events: list[Event]):
    """Saves the list of events to their corresponding files"""
    for event in events:
        pass

def GetExistingJSONObject():
    """Get the existing json object for said day"""

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
AppendDay(datetime.datetime.now())