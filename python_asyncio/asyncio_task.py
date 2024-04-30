import asyncio
import asyncio_async


async def main():
    task1 = asyncio.create_task(asyncio_async.coroutine(1, 2))
    task2 = asyncio.create_task(asyncio_async.coroutine(2, 2))
    task3 = asyncio.create_task(asyncio_async.coroutine(3, 2))

    await task1
    print('dep')
    await task2
    await task3


if __name__ == "__main__":
    asyncio.run(main())
