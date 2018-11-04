from datetime import datetime

from twontw.models import UrlQueueWatchModel
from twontw.models import UserDataStorageModel


class SendUrlToQueue(object):
    def __init__(self):
        pass

    def get_data(self):
        try:
            non_active_data = UserDataStorageModel.objects.filter(send_queue='ACTIVE')
        except:
            non_active_data = None
        return non_active_data

    def procces_data(self):
        send_queue = self.get_data()
        for i in send_queue:
            UrlQueueWatchModel.objects.create(
                url_id=i.id,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                status=0,
                owner=i.updated_by,
            )
            i.delete()
