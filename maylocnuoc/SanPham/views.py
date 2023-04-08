from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from SanPham.models import SanPham, SanPhamNoiBat
from SanPham.serializers import SanPhamSerializer, SanPhamNoiBatSerializer, SanPhamShortSerializer


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
    
    @action(methods=['POST'], detail=True, url_path='san-pham-lien-quan')
    def get_relevant_products(self, request, *args, **kwargs):
        obj = self.get_object()
        queryset = SanPham.objects.filter(the_loai=obj.the_loai)[:4]
        serializer = SanPhamShortSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=200)

    def list(self, request):
        queryset = SanPham.objects.all()
        sort_type = request.GET.get('sort-type', None)
        search_name = request.GET.get('search-name', None)
        categories_filter = request.GET.get('categories-filter', None)

        if search_name:
            queryset = queryset.filter(ten__icontains=search_name)
        
        if categories_filter:
            categories_filter = categories_filter.strip()
            categories_filter = [int(category_str) for category_str in categories_filter.split(',')]
            queryset = queryset.filter(the_loai_id__in=categories_filter)

        if sort_type == "latest":
            queryset = queryset
        elif sort_type == "popular":
            queryset = queryset
        elif sort_type == "price_low_to_high":
            queryset = queryset.order_by('gia')
        elif sort_type == "price_high_to_low":
            queryset = queryset.order_by('-gia')
        else:
            queryset = queryset.order_by('ten')

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

