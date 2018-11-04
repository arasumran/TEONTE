from django.apps.config import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class TwontwRestAppConfig(AppConfig):
    name = 'twontw.rest'
    label = 'twontw_rest'
    verbose_name = _('Twontw Rest')

