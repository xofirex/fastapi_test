import asyncio
import json

import aio_pika

from rabbitmq_connection import handle_messages


async def process_messages(message: aio_pika.IncomingMessage):
    print(json.loads(message.body.decode('utf-8')), flush=True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(handle_messages(loop, process_messages))
    loop.run_forever()
