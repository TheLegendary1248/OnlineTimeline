from __future__ import annotations

## This file deals with
from OnlineTimeline import globals 
from pathlib import Path
import json
from datetime import datetime, date

savePath = Path(globals.CONFIG["SaveLocation"])

timelinePath = savePath / "timeline"
objectsPath = savePath / "objects"

class Event:
    """Represents a data point, or that sorta of thing"""
    def __init__(self,timestamp:int, data:dict, id=None, end_timestamp=None) -> None:
        self.timestamp: int = timestamp
        """The UNIX time at which this event happened"""
        if end_timestamp != None:
            self.end_timestamp: int = end_timestamp
            """The UNIX end time of this event, if one is given"""
        self.data: dict = data
        """The content regarding this event"""
        self.id: str = id
        """The unique id for this event. If one is not given, timestamp is used instead"""
    def __str__(self) -> str:
        return f"Event {self.id} at {date.fromtimestamp(self.timestamp)}"
    
    def toDict(self) -> dict:
        """Converts the Event into it's appropiate JSON object"""
        obj = {
                "time" : self.timestamp,
                "data" : self.data,
            }
        return obj
    
    @staticmethod
    def AppendEvents(events: list[Event], medianame="unknown"):
        """Write events into their corresponding day files"""
        ##Sort events by time
        def GetTS(event: Event):
            return event.timestamp
        
        epoch = datetime.utcfromtimestamp(0)
        daysFromEpoch = 0
        events.sort(key=GetTS)
        allEventsInDay:list[Event] = []

        for event in events:
            eventDaysFromEpoch = epoch - event
            #Day difference checker, for file purposes 
            if daysFromEpoch == eventDaysFromEpoch:
                allEventsInDay.append(event)
                continue
            #Generate object containing all events with id's
            eventsAsDict = {}
            for e in allEventsInDay:
                eventsAsDict[e.id] = e.toDict()
            #Generate media-specific object
            mediaObj = {
                medianame : eventsAsDict
            }
            continue
            #If difference, flush current file and flush to next
            with open('DAY.json', 'r+') as f:
                dayData = json.load(f)
                dayData.update(mydict)
                f.seek(0)
                json.dump(dayData, f)
            daysFromEpoch = eventDaysFromEpoch
            allEventsInDay.clear()
            allEventsInDay.append(event)
            pass

        return
        fileDayPath = timelinePath / f"{date.year}/{date.month}/{date.day}.json"
        EnsurePath(fileDayPath)
        pass

def GetExistingJSONObject():
    """Get the existing json object for said day"""
    pass

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