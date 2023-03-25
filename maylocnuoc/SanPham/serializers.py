from rest_framework import serializers
from SanPham.models import SanPham, SanPhamNoiBat


class SanPhamSerializer(serializers.ModelSerializer):

    class Meta:
        model = SanPham
        fields = "__all__"

class SanPhamNoiBatSerializer(serializers.ModelSerializer):
    san_pham = SanPhamSerializer()

    class Meta:
        model = SanPhamNoiBat
        fields = ['id', 'do_noi_bat', 'san_pham']
