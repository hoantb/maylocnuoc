from django.contrib import admin
from django import forms
from DichVu.models import DichVu
from tinymce.widgets import TinyMCE

class DichVuForm(forms.ModelForm):
    mo_ta_ngan = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 50}))
    mo_ta_dai = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 100}))
    class Meta:
        model = DichVu
        fields = '__all__'

class DichVuAdmin(admin.ModelAdmin):
    form = DichVuForm

admin.site.register(DichVu, DichVuAdmin)