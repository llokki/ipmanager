#!/usr/bin/env python3

from tortoise import Tortoise, run_async
from database.connectToDatabase import db_connect


async def main():
    await db_connect()
    await Tortoise.generate_schemas()

if __name__ == '__main__':
    run_async(main())
