from rest_framework import serializers
from TinTuc.models import TinTuc


class TinTucSerializer(serializers.ModelSerializer):

    class Meta:
        model = TinTuc
        fields = "__all__"
