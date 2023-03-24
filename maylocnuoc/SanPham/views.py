from rest_framework import viewsets
from SanPham.models import SanPham
from django.shortcuts import get_object_or_404
from SanPham.serializers import SanPhamSerializer
from rest_framework.response import Response


class SanPhamViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving SanPham.
    """
    def list(self, request):
        queryset = SanPham.objects.all()
        serializer = SanPhamSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SanPham.objects.all()
        san_pham = get_object_or_404(queryset, pk=pk)
        serializer = SanPhamSerializer(san_pham)
        return Response(serializer.data)


