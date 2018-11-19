from rest_framework.viewsets import ModelViewSet

from twontw.models.user_data_storage import UserDataStorageModel
from twontw.rest.serializers.users_data_storage import UserDataStorageSerializers


class UsersDataStorageViewset(ModelViewSet):
    """

       view

    """

    search_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        return UserDataStorageModel.objects.all()

    def get_serializer_class(self):
        return UserDataStorageSerializers
