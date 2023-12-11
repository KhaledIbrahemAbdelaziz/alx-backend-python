#!/usr/bin/env python3
"""Asyncronus python
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n
def measure_time(n: int, max_delay: int) -> float:
    """finds the total time for the function to run"""
    begin = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - begin)/n
