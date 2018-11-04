from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from twontw.rest.views.users_data_storage import UsersDataStorageViewset
from twontw.rest.views.send_queue import SendQueueViewSets
router = DefaultRouter()

router.register('data_storage', UsersDataStorageViewset, base_name="data_storage")
router.register('send_queue', SendQueueViewSets, base_name="send_queue")


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),

]
