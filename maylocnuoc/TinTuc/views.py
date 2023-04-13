from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from TinTuc.models import TinTuc
from TinTuc.serializers import TinTucSerializer

class TinTucViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing TinTuc.
    """
    def list(self, request):
        queryset = TinTuc.objects.all()
        serializer = TinTucSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=200)
