from rest_framework import serializers
from NguoiDung.models import TinNhanGopY, DangKySubscribe


class TinNhanGopYSerializer(serializers.ModelSerializer):
    class Meta:
        model = TinNhanGopY
        fields = ["ten", "email", "so_dien_thoai", "tieu_de", "tin_nhan"]

class DangKySubscribeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, allow_null=False, allow_blank=False)

    class Meta:
        model = DangKySubscribe
        fields = ["email"]
