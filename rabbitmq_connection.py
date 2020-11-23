import json
import os
import typing

import aio_pika

RABBITMQ_URL = os.environ.get('RABBITMQ_URL', 'amqp://rabbitmq:rabbitmq@rabbitmq1')
QUEUE_NAME = 'item_process'


async def send_to_rabbit_mq(data: dict):
    connection = await aio_pika.connect(RABBITMQ_URL)
    channel = await connection.channel()

    await channel.default_exchange.publish(
        aio_pika.Message(json.dumps(data).encode('utf-8')),
        routing_key=QUEUE_NAME
    )

    await connection.close()


async def handle_messages(loop, func: typing.Callable) -> aio_pika.Connection:
    connection = await aio_pika.connect_robust(RABBITMQ_URL, loop=loop)
    channel = await connection.channel()
    queue = await channel.declare_queue(QUEUE_NAME)
    await queue.consume(func, no_ack=True)
    return connection
