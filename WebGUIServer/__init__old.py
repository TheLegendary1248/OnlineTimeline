# from webui import webui
from time import time
import asyncio
#TODO: FUNCTIONIZE THIS
# def other():
#     global running
#     running = True
#     global MyWindow
#     MyWindow = webui.window()
#     MyWindow.set_runtime(webui.runtime.nodejs)
#     MyWindow.show('WebGUIInterface/ot_frontend/build/index.js', webui.browser.firefox)
#     MyWindow.bind("MyID", my_function)
#     print('before cycle')

# def my_function(e : webui.event):
#     print("Data from JavaScript: " + e.data) # Message from JS
#     return f"Message from Python at {time()}"

# def waitOnWindow():
#     webui.wait()
#     while not MyWindow.is_shown():    
#         webui.wait()
#         print('while cycle')


# async def Hello(interval):
#     print(f'run hello! {interval}')
#     while True:
#         await asyncio.sleep(interval)
#         print(f'hello world at {interval}')

# async def main():
#     other()
#     print('running main')
#     coro = asyncio.to_thread(waitOnWindow)
#     onlyTask = asyncio.create_task(coro)
#     # report a message
#     print('Main doing other things')
#     # allow the scheduled task to start
#     # await asyncio.sleep(0)
#     # await the task
#     await onlyTask
#     global running
#     running = False
    
from nodejs import node, npm
# import nodejs
def newmain():
    node.call(["WebGUIInterface/build/index.js"])
    #start html server
        #this server works for Svelte
    #start python server
        #this server works in communication with OT
    pass

if __name__ == "__main__":
    
    print('hey!')
    newmain()
    print('exit cycle')


