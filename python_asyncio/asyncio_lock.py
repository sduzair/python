import asyncio

shared_resource = 0

# creates an instance of Lock that is used to synchronize access of shared resource between tasks
lock = asyncio.Lock()


async def coroutine_uses_lock(id: int, delay=2):
    global shared_resource
    async with lock:
        # Critical Section start
        print(f"Resource before: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(delay)
        print(f"Resource after: {shared_resource}")
        # Critical Section end


async def main():
    async with asyncio.TaskGroup() as group:
        [group.create_task(coroutine_uses_lock(i)) for i in range(3)]


if __name__ == "__main__":
    asyncio.run(main())
