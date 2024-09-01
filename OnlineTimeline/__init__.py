"""The core of OnlineTimeline"""

# Prepare to do things async
# import asyncio
# import time
import importlib.util
import sys
import os
from pprint import pprint
sys.path.append('./')
pprint(sys.path)

def loadcore():
    pass


def loadplugs():
    spec = importlib.util.spec_from_file_location("DB", os.path.abspath("../DB/__init__.py"))
    print("this is spec", spec)
    # print("these are mods", sys.modules)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    
    spec.loader.exec_module(spec)
    print(DB.load())
    
    pass

if __name__ == "__main__":
    print('Running OT init')
    loadcore()
    loadplugs()
