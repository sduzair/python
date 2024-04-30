import asyncio
import asyncio_async

# TaskGroup is a good way to schedule multiple tasks
async def main():
    tasks = []
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(asyncio_async.coroutine(i, i + 1)) for i in range(3)]
    
    print([tasks[i].result() for i in range(3)])

if __name__ == '__main__':
    asyncio.run(main())