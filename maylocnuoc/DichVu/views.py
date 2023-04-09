from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from DichVu.models import DichVu
from DichVu.serializers import DichVuSerializer

class DichVuViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing DichVu.
    """
    def list(self, request):
        queryset = DichVu.objects.all()
        serializer = DichVuSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=200)
