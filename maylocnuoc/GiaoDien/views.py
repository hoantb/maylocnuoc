from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from GiaoDien.models import SlideTrangChu
from GiaoDien.serializers import SlideTrangChuSerializer

class GiaoDienViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing GiaoDien.
    """
    def list(self, request):
        queryset = SlideTrangChu.objects.all()
        serializer = SlideTrangChuSerializer(queryset, many=True)
        
        return Response({"data": {"slides": serializer.data}}, status=200)
