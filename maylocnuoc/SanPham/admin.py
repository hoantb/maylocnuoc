from django.contrib import admin
from django import forms
from SanPham.models import SanPham, SanPhamNoiBat
from tinymce.widgets import TinyMCE

class SanPhamForm(forms.ModelForm):
    mo_ta_dai = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 100}))
    class Meta:
        model = SanPham
        fields = '__all__'

class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten', 'the_loai')

class SanPhamNoiBatAdmin(admin.ModelAdmin):
    list_display = ('id', 'san_pham', 'do_noi_bat')

admin.site.register(SanPham, SanPhamAdmin)
admin.site.register(SanPhamNoiBat, SanPhamNoiBatAdmin)