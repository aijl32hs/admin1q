import asyncio
import aiohttp
import time

# Target URL
target_url = 'http://127.0.0.1:8000'  # O'zingizning local serveringizni kiriting

# Number of requests
num_requests = 1000  # So‘rovlar soni
concurrent_requests = 50  # Bir vaqtda yuboriladigan so‘rovlar

async def send_request(session, request_num):
    """Bitta HTTP so‘rovni yuborish va natijani qayd qilish"""
    try:
        start_time = time.time()
        async with session.get(target_url) as response:
            end_time = time.time()
            print(f"[{request_num}] Status: {response.status}, Time: {end_time - start_time:.4f}s")
    except Exception as e:
        print(f"[{request_num}] Error: {e}")

async def main():
    """Asinxron yuklama testi"""
    connector = aiohttp.TCPConnector(limit=concurrent_requests)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [send_request(session, i) for i in range(num_requests)]
        await asyncio.gather(*tasks)

# Testni ishga tushirish
asyncio.run(main())
