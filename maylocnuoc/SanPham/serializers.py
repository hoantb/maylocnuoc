from rest_framework import serializers
from SanPham.models import SanPham


class SanPhamSerializer(serializers.ModelSerializer):

    class Meta:
        model = SanPham
        fields = "__all__"
