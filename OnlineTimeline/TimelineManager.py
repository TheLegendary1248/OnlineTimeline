from __future__ import annotations

## This file deals with
from OnlineTimeline import globals
from OnlineTimeline.Utils import EnsurePath
from pathlib import Path
import json
from datetime import datetime, date, timedelta
import os
savePath = Path(globals.CONFIG["OnlineTimelineCore"]["SaveLocation"])

timelinePath = savePath / "timeline"
objectsPath = savePath / "objects"

class Event:
    """Represents a data point at a given time for the user"""
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
    def __str__(self):
        return f"Event {self.id} from {self.timestamp}"
    
    def __repr__(self):
        return self.__str__()
    
    def toDict(self) -> dict:
        """Converts the Event into it's appropiate JSON object"""
        obj = {
                "time" : self.timestamp,
                "data" : self.data,
            }
        if self.end_timestamp != None:
            obj["endtime"] = self.end_timestamp
            
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
            eventDaysFromEpoch = timedelta(seconds=event.timestamp).days
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
            fileDate = epoch + timedelta(days=daysFromEpoch)
            fileDayPath = timelinePath / f"{fileDate.year}/{fileDate.month}/{fileDate.day}.json"
            EnsurePath(fileDayPath)
            filesize = os.path.getsize(fileDayPath)
            if filesize != 0:
                with open(fileDayPath, 'w') as f:
                    dayData = json.load(f) or {}
                    dayData.update(mediaObj)
                    f.seek(0)
                    json.dump(dayData, f)
            else:
                with open(fileDayPath, 'r+') as f:
                    json.dump(mediaObj, f)
                    
            daysFromEpoch = eventDaysFromEpoch
            allEventsInDay.clear()
            allEventsInDay.append(event)
            pass

        return
        
        pass

def GetExistingJSONObject():
    """Get the existing json object for said day"""
    pass
