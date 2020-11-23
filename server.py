import typing

from fastapi import FastAPI
from pydantic import BaseModel

from rabbitmq_connection import send_to_rabbit_mq


app = FastAPI()


class Item(BaseModel):
    taskId: str
    title: str
    params: typing.Dict[str, str] = {}


@app.post("/add_task/")
async def create_task(item: Item):
    await send_to_rabbit_mq(vars(item))
    return item



