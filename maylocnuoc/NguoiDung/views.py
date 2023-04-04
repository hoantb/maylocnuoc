from rest_framework import views
from NguoiDung.models import TinNhanGopY
from NguoiDung.serializers import TinNhanGopYSerializer, DangKySubscribeSerializer
from rest_framework.response import Response

class TinNhanGopYView(views.APIView):
    serilizer_class = TinNhanGopYSerializer

    def post(self, request):
        serializer = TinNhanGopYSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Gui Gop Y Thanh Cong"}, status=200)
        
        return Response({"success": False, "error": "Sai Du Lieu Nhap Vao"}, status=400)

class DangKySubscribeView(views.APIView):
    serilizer_class = DangKySubscribeSerializer

    def post(self, request):
        serializer = DangKySubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Subscribe Thanh Cong"}, status=200)
        
        return Response({"success": False, "error": "Sai Du Lieu Nhap Vao"}, status=400)
