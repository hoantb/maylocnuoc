from rest_framework import serializers
from NguoiDung.models import TinNhanGopY, DangKySubscribe


class TinNhanGopYSerializer(serializers.ModelSerializer):
    class Meta:
        model = TinNhanGopY
        fields = ["ten", "email", "so_dien_thoai", "tieu_de", "tin_nhan"]

class DangKySubscribeSerializer(serializers.Serializer):
    class Meta:
        model = DangKySubscribe
        fields = ["email"]
