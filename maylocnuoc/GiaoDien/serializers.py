from rest_framework import serializers
from GiaoDien.models import SlideTrangChu, HinhTrangGioiThieu, HinhTrangLienHe


class SlideTrangChuSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlideTrangChu
        fields = "__all__"

class HinhTrangGioiThieuSerializer(serializers.ModelSerializer):

    class Meta:
        model = HinhTrangGioiThieu
        fields = "__all__"

class HinhTrangLienHeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HinhTrangLienHe
        fields = "__all__"
