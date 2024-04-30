import asyncio

# An event object acts as a boolean flag that blocks execution until it is set to true
event = asyncio.Event()

async def wait():
    print("Waiting...")
    await event.wait()
    print("Waiting finished")

async def set():
    print("Setting...")
    await asyncio.sleep(3)
    event.set()
    print("Setting finished")

async def main():
    async with asyncio.TaskGroup() as group:
        group.create_task(wait())
        group.create_task(set())

if __name__ == '__main__':
    asyncio.run(main())