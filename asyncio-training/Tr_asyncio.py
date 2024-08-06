import asyncio
import time


async def fetching_urls():
    print('Start Fetching URLS...')
    await asyncio.sleep(2)
    print('URLS Fetched')

async def fetching_avatars():
    print('Start Fetching AVATARS...')
    await asyncio.sleep(1)
    print('AVATARS Fetched')

async def main():
    start_time = time.time()
    # task =  asyncio.create_task(fetching_avatars())
    task = await asyncio.gather(fetching_urls(), fetching_avatars())

    print(f"Ended At {time.time() - start_time}") # 4.00354790687561
    


asyncio.run(main())

