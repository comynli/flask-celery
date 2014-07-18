# coding=utf-8

from celery import Celery as C

__author__ = 'comyn'


class Celery(object):
    def __init__(self, app=None):
        self._celery = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self._celery = C(app.import_name, broker=app.config['CELERY_BROKER_URL'])
        self._celery.conf.update(app.config)
        TaskBase = self._celery.Task
        class ContextTask(TaskBase):
            abstract = True
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
        self._celery.Task = ContextTask

    def __getattr__(self, item):
        return getattr(self._celery, item)