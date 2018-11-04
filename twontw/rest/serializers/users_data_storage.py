from rest_framework import serializers
from twontw.models.user_data_storage import *
from selenium import webdriver



class UserDataStorageSerializers(serializers.ModelSerializer):
    """
     serializer
    """
    send_queue = serializers.SerializerMethodField()
    url_time = serializers.SerializerMethodField()

    class Meta:
        model = UserDataStorageModel
        fields = ('url_link',
                  'url_category',
                  'url_desc',
                  'watch_count',
                  'send_queue',
                  'url_time')

    def get_send_queue(self, obj):
        elem = obj.send_queue = STATUS[1][0]
        return elem

    def get_url_time(self, obj):
        driver = webdriver.Chrome()
        driver.get(obj.url_link)
        data =driver.find_element_by_class_name('ytp-time-duration').text
        time_calculator_list=0
        while(time_calculator_list.__len__()>0):
            time_calculator_list=data.split(':')[::-1]
            seconds =0
            for i in range(len(time_calculator_list)):
                if i == 0:
                    seconds= int(time_calculator_list[i]) +seconds
                if i == 1:
                    seconds= int(time_calculator_list[i])*60 +seconds
                if i == 2:
                    seconds= int(time_calculator_list[i])*360 +seconds
            obj.url_time = seconds
        return obj.url_time









