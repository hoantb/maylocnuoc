from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from GiaoDien.models import SlideTrangChu, HinhTrangGioiThieu, HinhTrangLienHe
from GiaoDien.serializers import SlideTrangChuSerializer, HinhTrangGioiThieuSerializer, HinhTrangLienHeSerializer

class GiaoDienViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing GiaoDien.
    """
    def list(self, request):
        queryset = SlideTrangChu.objects.all()
        serializer = SlideTrangChuSerializer(queryset, many=True)
        gioi_thieu = None
        lien_he = None
        if HinhTrangGioiThieu.objects.filter():
            gioi_thieu = HinhTrangGioiThieuSerializer(HinhTrangGioiThieu.objects.filter().first()).data
        if HinhTrangLienHe.objects.filter():
            lien_he = HinhTrangLienHeSerializer(HinhTrangLienHe.objects.filter().first()).data
        return Response({"data": {"slides": serializer.data, "gioi_thieu": gioi_thieu, "lien_he": lien_he}}, status=200)
