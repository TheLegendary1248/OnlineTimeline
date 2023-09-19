# Prepare to do things async
import asyncio
import time
print("Hey, is this supposed to run?")

# Launch WebUI
import WebGUIInterface as GUI



async def runTillTheEnd():
    import core
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
    asyncio.run(main())
    pass