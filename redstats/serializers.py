from rest_framework import serializers
from redstats.models import Subscribers, ImagesParams

class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'


class ImagesParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesParams
        fields = '__all__'



