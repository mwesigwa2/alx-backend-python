#!/usr/bin/env python3
'''
    a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.

    measure_runtime should measure the total runtime and return it.
'''

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' returns total runtime '''

    start_time = asyncio.get_event_loop().time()

    # Using asyncio.gather to execute async_comprehension 4 times in parallel
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
