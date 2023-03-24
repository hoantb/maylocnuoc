from rest_framework import viewsets
from TheLoai.models import TheLoai
from django.shortcuts import get_object_or_404
from TheLoai.serializers import TheLoaiSerializer
from rest_framework.response import Response


class TheLoaiViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving TheLoai.
    """
    def list(self, request):
        queryset = TheLoai.objects.all()
        serializer = TheLoaiSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TheLoai.objects.all()
        san_pham = get_object_or_404(queryset, pk=pk)
        serializer = TheLoaiSerializer(san_pham)
        return Response(serializer.data)


