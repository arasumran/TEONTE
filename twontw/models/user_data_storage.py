from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from twontw.utils.mixins import AuditMixin

CATEGORIES = (('genel', 'genel'),
              ('sanat', 'sanat'),
              ('askeri', 'askeri'),
              ('oyun', 'oyun'),
              ('bilim kurgu', 'bilim kurgu'),
               ('muzik', 'muzik'),
              ('gunluk yasam', 'gunluk yasam'
               ))

STATUS = (('ACTIVE', 'ACTIVE'), ('IN_QUEUE', 'IN_QUEUE'), ('FINISHED', 'FINISHED'))


class UserDataStorageModel(AuditMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    url_link = models.URLField()
    url_category = models.CharField(choices=CATEGORIES, max_length=255)
    url_desc = models.TextField()
    url_time = models.IntegerField(null=True)
    watch_count = models.IntegerField()
    send_queue = models.CharField(choices=STATUS, max_length=255)
    class Meta:
        verbose_name = _('User Data Storage')
        verbose_name_plural = _('User Data Storages')
        db_table = 'user_data_storage'


