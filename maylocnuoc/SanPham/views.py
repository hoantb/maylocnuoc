from rest_framework import viewsets, mixins
from SanPham.models import SanPham, SanPhamNoiBat
from django.shortcuts import get_object_or_404
from SanPham.serializers import SanPhamSerializer, SanPhamNoiBatSerializer
from rest_framework.response import Response
from rest_framework import pagination

class SanPhamPagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 50



class SanPhamViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    A simple ViewSet for listing or retrieving SanPham.
    """
    serializer_class = SanPhamSerializer
    pagination_class = SanPhamPagination

    def get_queryset(self):
        return SanPham.objects.all()

    def list(self, request):
        queryset = SanPham.objects.all()
        sort_type = request.GET.get('sort-type', None)

        if sort_type == "latest":
            queryset = queryset
        elif sort_type == "popular":
            queryset = queryset
        elif sort_type == "price_low_to_high":
            queryset = queryset.order_by('gia')
        elif sort_type == "price_high_to_low":
            queryset = queryset.order_by('-gia')
        else:
            queryset = queryset.order_by('title')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SanPham.objects.all()
        san_pham = get_object_or_404(queryset, pk=pk)
        serializer = SanPhamSerializer(san_pham)
        return Response(serializer.data)

class SanPhamNoiBatViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving SanPhamNoiBat.
    """
    def list(self, request):
        queryset = SanPhamNoiBat.objects.all().order_by('-do_noi_bat')
        serializer = SanPhamNoiBatSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SanPhamNoiBat.objects.all()
        san_pham = get_object_or_404(queryset, pk=pk)
        serializer = SanPhamNoiBatSerializer(san_pham)
        return Response(serializer.data)

