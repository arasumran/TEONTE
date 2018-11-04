from django.db import models
from django.utils.translation import ugettext_lazy as _
from twontw.utils.mixins import *

class UrlQueueWatchModel(TimeStampMixin):
    url_id =models.IntegerField()
    status = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    class Meta:
        verbose_name = _('Url Queue Watch')
        verbose_name_plural = _('Url Queue Watches')
        db_table = 'url_queue_watch'
