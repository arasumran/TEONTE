# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class TwontwConfig(AppConfig):
    name = 'twontw'
    def ready(self):
        from twontw.tasks.get_hello_task import *
