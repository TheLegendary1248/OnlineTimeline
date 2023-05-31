## This file deals with
import globals
from pathlib import Path
import json
import os
import datetime

savePath = Path(globals.CONFIG["SaveLocation"])

timelinePath = savePath / "timeline"
objectsPath = savePath / "objects"

def AppendDay(date: datetime.datetime):
    """Appends onto the day file"""
    fileDayPath = timelinePath / f"{date.year}/{date.month}/{date.day}.json"
    EnsurePath(fileDayPath)
    file = fileDayPath.open("w")
    json.dump({"hey": "ok", "array":[1,2,3]},file)
    file.flush()
    file.close()
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