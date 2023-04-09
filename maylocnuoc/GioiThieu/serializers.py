from rest_framework import serializers
from GioiThieu.models import GioiThieu


class GioiThieuSerializer(serializers.ModelSerializer):

    class Meta:
        model = GioiThieu
        fields = "__all__"
