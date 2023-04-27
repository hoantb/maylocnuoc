from django.contrib import admin
from GiaoDien.models import SlideTrangChu, HinhTrangGioiThieu, HinhTrangLienHe

class SlideTrangChuAdmin(admin.ModelAdmin):
    pass

class HinhTrangGioiThieuAdmin(admin.ModelAdmin):
    pass

class HinhTrangLienHeAdmin(admin.ModelAdmin):
    pass

admin.site.register(SlideTrangChu, SlideTrangChuAdmin)
admin.site.register(HinhTrangGioiThieu, HinhTrangGioiThieuAdmin)
admin.site.register(HinhTrangLienHe, HinhTrangLienHeAdmin)