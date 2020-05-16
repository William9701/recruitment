#!coding=utf-8

from celery import Celery

# First parameter is the current script name, second parameter is the broker service address
app = Celery('tasks', backend='redis://127.0.0.1', broker='redis://127.0.0.1')


@app.task
def add(x, y):
    return x + y
