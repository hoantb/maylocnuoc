from django.contrib import admin
from NguoiDung.models import TinNhanGopY


class TinNhanGopYAdmin(admin.ModelAdmin):
    pass

admin.site.register(TinNhanGopY, TinNhanGopYAdmin)