import asyncio


async def coroutine(id: int, delay=2):
    print(f"Starting task {id}")
    await asyncio.sleep(delay)
    print(f"Ending task {id}")
    return { 'id': id }


async def main():
    r1 = await coroutine(1)
    r2 = await coroutine(2)
    print("No dep")
    print(f"Result of task 1: {r1}")
    print(f"Result of task 2: {r2}")


if __name__ == "__main__":
    asyncio.run(main())
