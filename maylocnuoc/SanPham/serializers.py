from rest_framework import serializers
from SanPham.models import SanPham, SanPhamNoiBat


class SanPhamSerializer(serializers.ModelSerializer):

    class Meta:
        model = SanPham
        fields = "__all__"

class SanPhamShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = SanPham
        fields = ["id", "ten", "gia", "hinh_anh"]

class SanPhamNoiBatSerializer(serializers.ModelSerializer):
    san_pham = SanPhamShortSerializer()

    class Meta:
        model = SanPhamNoiBat
        fields = ['id', 'do_noi_bat', 'san_pham']
