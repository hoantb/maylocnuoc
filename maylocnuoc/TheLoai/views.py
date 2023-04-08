from rest_framework import viewsets
from TheLoai.models import TheLoai
from django.shortcuts import get_object_or_404
from TheLoai.serializers import TheLoaiSerializer, TheLoaiTrangChuSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TheLoaiViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving TheLoai.
    """
    @action(methods=['GET'], detail=False, url_path='danh-muc-trang-chu')
    def get_categories(self, request, *args, **kwargs):
        queryset = TheLoai.objects.all(hien_thi_trang_chu=True)
        serializer = TheLoaiSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=200)

    def list(self, request):
        queryset = TheLoai.objects.all()
        serializer = TheLoaiSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        queryset = TheLoai.objects.all()
        san_pham = get_object_or_404(queryset, pk=pk)
        serializer = TheLoaiSerializer(san_pham)
        return Response(serializer.data, status=200)


