from rest_framework import serializers
from TheLoai.models import TheLoai


class TheLoaiSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheLoai
        fields = "__all__"
