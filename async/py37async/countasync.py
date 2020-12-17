#!/usr/bin/env python3
# countasync.py

import asyncio

async def count(n: int):
    print(f"One in {n}")
    await asyncio.sleep(1)
    print(f"Two in {n}")

async def main():
    await asyncio.gather(count(0), count(1), count(2))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
