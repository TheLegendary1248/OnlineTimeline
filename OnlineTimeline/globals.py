#This python file is in charge of the settings file
"""Global variables for the whole program"""
import json
from pathlib import Path

VARS = {
    "ROOT_DIR" : str(Path.cwd()),
    "BUILTIN_DIR" : str(Path.cwd() / "builtin")
}
"""Contains global variables determined at run time"""

CONFIG = {
    "OnlineTimelineCore" : {
        "SaveLocation" : str(Path.cwd() / "usersaves"),
        "TempLocation" : str(Path.cwd() / "temp")
    }
}
"""Contains global variables"""

#Check for settings existence
settingFileName = "settings.json"
settingFilePath = Path(VARS["ROOT_DIR"]) / settingFileName

def WriteToSettings():
    """Simple function to write to settings file"""
    file = Path.open(settingFilePath, "w")
    json.dump(CONFIG, file, indent=4)
    file.flush()
    file.close()

#Logic for reading settings file
if Path.exists(settingFilePath):
    #Get
    file = Path.open(settingFilePath, 'r')
    context = file.read()
    file.close()
    try:
        contextDict = json.loads(context)
        CONFIG.update(json.loads(context))
        WriteToSettings()
    except:
        #JSON File failed to parse correctly
        print(f"{__file__} : {settingFileName} is not valid JSON. It will be overwritten")
        WriteToSettings()
    else:
        pass
else:
    #JSON File doesn't exist
    print(f"{__file__} : {settingFileName} does not exist so one will be created in the root directory")
    WriteToSettings()