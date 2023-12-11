#!/usr/bin/env python3
"""asynchronous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    """
    waits = random.random() * max_delay
    await asyncio.sleep(waits)
    return waits
