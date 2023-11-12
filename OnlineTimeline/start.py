import sys
import os
sys.path.append('./')
print(sys.path)
print(os.getcwd())

import asyncio
import time
import WebGUIInterface as GUI
#import OTPlugin

# for root, dirs, files in os.walk(".", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

async def runTillTheEnd():
    # OTPlugin.ReloadPlugins()
    while True:
        await asyncio.sleep(0)
        print(f"GUI is still running at {time.time()}")
        if not GUI.running:
            break

async def main():
    
    input_tasks = [
        asyncio.create_task(GUI.main()),
        asyncio.create_task(runTillTheEnd())]
    print([await t for t in asyncio.as_completed(input_tasks)])
    pass

if __name__ == "__main__":
    print("hello world!")
    input("Press anything to enter")
    GUI.newmain()
    input("Enter anything to leave")
    pass