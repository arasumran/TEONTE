from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from twontw.models import UserDataStorageModel
from twontw.utils import get_user


class SendQueueViewSets(ViewSet):
    """
       view
    """

    def list(self, request, *args, **kwargs):
        current_user = get_user.get_user()
        try:
            UserDataStorageModel.objects.filter(user_id=current_user.id).update(send_queue='ACTIVE')
            return Response({'key': 'value'}, status=status.HTTP_200_OK)
        except:
            return IOError
