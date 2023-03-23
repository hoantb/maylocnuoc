from django.contrib import admin
from TheLoai.models import TheLoai

class TheLoaiAdmin(admin.ModelAdmin):
    pass

admin.site.register(TheLoai, TheLoaiAdmin)