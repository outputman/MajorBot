import asyncio
from contextlib import suppress

from bot.utils.launcher import process
from bot.core.tapper import initialize_background_tasks


async def main():
    await initialize_background_tasks()
    await process()


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
