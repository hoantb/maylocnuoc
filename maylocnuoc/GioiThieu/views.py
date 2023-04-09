from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from GioiThieu.models import GioiThieu
from GioiThieu.serializers import GioiThieuSerializer

class GioiThieuViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing GioiThieu.
    """
    def list(self, request):
        queryset = GioiThieu.objects.all()
        serializer = GioiThieuSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=200)
