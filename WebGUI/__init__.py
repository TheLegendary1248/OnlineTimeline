from webui import webui
from time import time
import asyncio 

import functools

def run_in_executor(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(None, lambda: f(*args, **kwargs))

    return inner

@run_in_executor
def foo(arg):  # Your wrapper for async use
    resp = waitOnWindow()
    return 
    # f"{arg}{len(resp)}" 

async def asyncWaitOnWindow(input):
    res = await foo(input)
    return

MyWindow = webui.window()
MyWindow.show('WebGUI/html/test.html', webui.browser.firefox)
def my_function(e : webui.event):
    print("Data from JavaScript: " + e.data) # Message from JS
    return f"Message from Python at {time()}"

MyWindow.bind("MyID", my_function)

print('before cycle')

async def waitOnWindow():
    webui.wait()
    while MyWindow.is_shown():    
        webui.wait()
        print('while cycle')

async def Hello(interval):
    print(f'run hello! {interval}')
    while True:
        await asyncio.sleep(interval)
        print(f'hello world at {interval}')

async def main():
    print('running main')
    input_tasks = [
        asyncio.create_task(asyncWaitOnWindow("my input")),
        asyncio.create_task(Hello(0.67)),
        asyncio.create_task(Hello(0.95)),
        asyncio.create_task(Hello(1.53)),]
    print([await t for t in asyncio.as_completed(input_tasks)])

asyncio.run(main())

print('exit cycle')


# webui.set_timeout(10)