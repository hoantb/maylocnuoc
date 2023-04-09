from django.contrib import admin
from TheLoai.models import TheLoai

class TheLoaiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten', 'hien_thi_trang_chu')

admin.site.register(TheLoai, TheLoaiAdmin)