from django.contrib import admin
from SanPham.models import SanPham

class SanPhamAdmin(admin.ModelAdmin):
    pass

admin.site.register(SanPham, SanPhamAdmin)