from rest_framework import serializers
from DichVu.models import DichVu


class DichVuSerializer(serializers.ModelSerializer):

    class Meta:
        model = DichVu
        fields = "__all__"
