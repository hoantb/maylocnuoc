from django.contrib import admin
from django import forms
from SanPham.models import SanPham
from tinymce.widgets import TinyMCE

class PersonForm(forms.ModelForm):
    mo_ta_dai = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = SanPham
        fields = '__all__'

class SanPhamAdmin(admin.ModelAdmin):
    form = PersonForm

admin.site.register(SanPham, SanPhamAdmin)