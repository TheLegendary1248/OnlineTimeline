#This python file is in charge of the settings file
import json
from pathlib import Path

VARS = {
    "ROOT_DIR" : str(Path.cwd()) 
}

CONFIG = {
    "SaveLocation" : str(Path.cwd() / "usersaves")
}
"""Contains global variables"""

#Check for settings existence
settingFileName = "settings.json"
settingFilePath = Path(VARS["ROOT_DIR"]) / settingFileName

def WriteToSettings():
    file = Path.open(settingFilePath, "w")
    file.write(json.dumps(CONFIG))
    file.flush()
    file.close()

if Path.exists(settingFilePath):
    file = Path.open(settingFilePath, 'r')
    context = file.read()
    file.close()
    try:
        contextDict = json.loads(context)
        CONFIG.update(json.loads(context))
        WriteToSettings()
    except:
        print(f"{__file__} : {settingFileName} is not valid JSON. It will be overwritten")
        WriteToSettings()
    else:
        pass
else:
    print(f"{__file__} : {settingFileName} does not exist so one will be created in the root directory")
    WriteToSettings()