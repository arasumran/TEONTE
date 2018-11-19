from rest_framework import serializers
from selenium import webdriver

from twontw.models.user_data_storage import *


class UserDataStorageSerializers(serializers.ModelSerializer):
    """
     serializer
    """
    send_queue = serializers.SerializerMethodField()
    url_time = serializers.SerializerMethodField()

    class Meta:
        model = UserDataStorageModel
        fields = ('url_link', 'url_category', 'url_desc', 'watch_count', 'send_queue', 'url_time')

    def get_send_queue(self, obj):
        elem = obj.send_queue = STATUS[1][0]
        return elem

    def get_url_time(self, obj):
        driver = webdriver.Chrome()
        driver.get(obj.url_link)
        data = driver.find_element_by_class_name('ytp-time-duration').text
        while (not data):
            data = driver.find_element_by_class_name('ytp-time-duration').text
        time_calculator_list = data.split(':')[::-1]
        seconds = 0
        for i in range(len(time_calculator_list)):
            if i == 0:
                seconds = int(time_calculator_list[i]) + seconds
            if i == 1:
                seconds = int(time_calculator_list[i]) * 60 + seconds
            if i == 2:
                seconds = int(time_calculator_list[i]) * 360 + seconds
        obj.url_time = seconds
        return obj.url_time

    def validate(self, attrs):
        if attrs['watch_count'] > User.objects.count():
            raise serializers.ValidationError("watch count must be smaller than : {} ".format(User.objects.count()))
        return attrs
