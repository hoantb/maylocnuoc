from rest_framework import serializers
from GiaoDien.models import SlideTrangChu


class SlideTrangChuSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlideTrangChu
        fields = "__all__"
