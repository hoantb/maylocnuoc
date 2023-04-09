"""maylocnuoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from SanPham.views import SanPhamViewSet, SanPhamNoiBatViewSet
from TheLoai.views import TheLoaiViewSet
from NguoiDung.views import TinNhanGopYView, DangKySubscribeView
from GioiThieu.views import GioiThieuViewSet

router = DefaultRouter()
router.register(r'api/san-pham', SanPhamViewSet, basename='san-pham')
router.register(r'api/danh-muc', TheLoaiViewSet, basename='danh-muc')
router.register(r'api/san-pham-noi-bat', SanPhamNoiBatViewSet, basename='san-pham-noi-bat')
router.register(r'api/gioi-thieu', GioiThieuViewSet, basename='san-pham-noi-bat')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/tin-nhan-gop-y', TinNhanGopYView.as_view()),
    path('api/dang-ky-subscribe', DangKySubscribeView.as_view())
]

urlpatterns += router.urls