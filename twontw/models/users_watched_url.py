from twontw.utils.mixins import *


class UsersWatchedUrlModel(TimeStampMixin):
    user_id = models.IntegerField()
    url_id = models.IntegerField()

    class Meta:
        db_table = 'users_watched_url'
        verbose_name = 'users_watched_url'
        verbose_name_plural = 'user_watched_urls'
