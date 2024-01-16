#!/usr/bin/env python3
'''
    coroutine called async_generator that takes
    no arguments.

    The coroutine loops 10 times, each time asynchronously
    waits 1 second, then yields a random number between 0 and 10.
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' asynchronous func that yields random number '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
