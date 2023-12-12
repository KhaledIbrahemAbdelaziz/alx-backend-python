#!/usr/bin/env python3
"""Asyncio corotnue"""
from time import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """should measure the total runtime and return it."""
    begin = time()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    return time() - begin
