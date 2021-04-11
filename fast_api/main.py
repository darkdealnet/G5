import os
from fastapi import FastAPI
from pydantic import BaseModel
from validate import value_validate
from celery import Celery

os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

app_celery = Celery('app_celery')
app_celery.config_from_envvar('CELERY_CONFIG_MODULE')


class Item(BaseModel):
    value: str


app = FastAPI()


@app.post("/")
async def create_item(items: Item):
    try:
        value, valid, error = value_validate(items.value)
    except KeyError:
        value, valid, error = None, False, "KeyError"

    if valid:
        app_celery.send_task('tasks.add', (value,))
        return {"message": "accepted"}
    else:
        return {"error": error}
