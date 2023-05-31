##Not sure, im still thinking about it
import globals
from pathlib import Path
import json
import os
import datetime

savePath = Path(globals.CONFIG["SaveLocation"])

timelinePath = savePath / "timeline"
objectsPath = savePath / "objects"
resources = savePath / "resources" 