from rest_framework import serializers
from TheLoai.models import TheLoai
from SanPham.serializers import SanPhamShortSerializer
from SanPham.models import SanPham

class TheLoaiSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheLoai
        fields = "__all__"


class TheLoaiTrangChuSerializer(serializers.ModelSerializer):
    san_phams = serializers.SerializerMethodField()

    class Meta:
        model = TheLoai
        fields = ["id", "ten", "san_phams"]
    
    def get_san_phams(self, instance):
        """
        Get each categories 4 products
        """
        queryset = SanPham.objects.filter(the_loai=instance)[:4]
        serializer = SanPhamShortSerializer(instance=queryset, many=True)
        return serializer.data