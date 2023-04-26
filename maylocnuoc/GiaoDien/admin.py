from django.contrib import admin
from GiaoDien.models import SlideTrangChu

class SlideTrangChuAdmin(admin.ModelAdmin):
    pass

admin.site.register(SlideTrangChu, SlideTrangChuAdmin)
