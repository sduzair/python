import asyncio

shared_resource = 0

# creates a semophore object that allows max 2 tasks to concurrently access the shared resource
semaphore = asyncio.Semaphore(2)


async def access_resource(id: int, delay=3):
    global shared_resource
    async with semaphore:
        print(
            f"Accessing resource by coroutine {id} - Resource before usage: {shared_resource}"
        )
        shared_resource += 1
        await asyncio.sleep(delay)
        print(
            f"Releasing resource by coroutine {id} - Resource after usage: {shared_resource}"
        )
        return {"id": id}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(access_resource(i + 1)) for i in range(5)]

    print([task.result() for task in tasks])


if __name__ == "__main__":
    asyncio.run(main())
