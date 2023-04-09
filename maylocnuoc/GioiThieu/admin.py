from django.contrib import admin
from django import forms
from GioiThieu.models import GioiThieu
from tinymce.widgets import TinyMCE

class SanPhamForm(forms.ModelForm):
    mo_ta_dai = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = GioiThieu
        fields = '__all__'

class GioiThieuAdmin(admin.ModelAdmin):
    pass

admin.site.register(GioiThieu, GioiThieuAdmin)