from rest_framework import serializers
from TheLoai.models import TheLoai
from SanPham.serializers import SanPhamShortSerializer

class TheLoaiSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheLoai
        fields = "__all__"


class TheLoaiTrangChuSerializer(serializers.ModelSerializer):
    san_phams = SanPhamShortSerializer

    class Meta:
        model = TheLoai
        fields = ["id", "ten", "san_phams"]