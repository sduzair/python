import asyncio
import asyncio_async


async def main():
    await asyncio.gather(*[asyncio_async.coroutine(i, i) for i in range(3)])


if __name__ == "__main__":
    asyncio.run(main())
