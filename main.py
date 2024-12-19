import asyncio
import random
import aiohttp
import aiofiles
import time

async def fetch_waifus(type: str, category: str):
    url = f"https://api.waifu.pics/many/{type}/{category}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"exclude": []}) as response:
            response.raise_for_status()
            return await response.json()


async def fetch_multiple_waifus(type: str, count: int):
    categories = ["waifu", "neko", "shinobu", "bully", "cry", "hug", "kiss", "lick", "pat", "smug", "highfive", "nom", "bite", "slap", "wink", "poke", "dance", "cringe", "blush"]
    tasks = [fetch_waifus(type, random.choice(categories)) for _ in range(count)]
    results = await asyncio.gather(*tasks)
    return results

SAVE_PATH = "/mnt/teldrive/waifu/"

async def download_image(url: str, filename: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            async with aiofiles.open(SAVE_PATH + filename, 'wb') as f:
                await f.write(await response.read())
    print(f"Downloaded: {url}")

async def fetch_and_save_waifus(type: str, count: int):
    results = await fetch_multiple_waifus(type, count)
    for i, result in enumerate(results):
        for url in result['files']:
            filename = url.split('/')[-1]
            await download_image(url, filename)

async def fetch_and_save_waifus_forever(type: str, count: int):
    while True:
        await fetch_and_save_waifus(type, count)
        time.sleep(60)

# Example usage

type = "sfw"

asyncio.run(fetch_and_save_waifus_forever(type, 1))
