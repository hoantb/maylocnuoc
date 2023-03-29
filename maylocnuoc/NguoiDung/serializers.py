from rest_framework import serializers
from NguoiDung.models import TinNhanGopY


class TinNhanGopYSerializer(serializers.ModelSerializer):

    class Meta:
        model = TinNhanGopY
        fields = ["ten", "email", "so_dien_thoai", "tieu_de", "tin_nhan"]

