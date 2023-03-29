from rest_framework import views
from NguoiDung.models import TinNhanGopY
from NguoiDung.serializers import TinNhanGopYSerializer
from rest_framework.response import Response

class TinNhanGopYView(views.APIView):
    serilizer_class = TinNhanGopYSerializer

    def post(self, request):
        serializer = TinNhanGopYSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Gui Gop Y Thanh Cong"}, status=200)
        
        return Response({"error": "wrong the form input"}, status=404)
