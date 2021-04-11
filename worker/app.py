from __future__ import absolute_import, unicode_literals
import os

from celery import Celery


os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')
def add(x, y):
    return x + y
app_celery = Celery('app_celery', include = ['tasks'])
