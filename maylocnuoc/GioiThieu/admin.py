from django.contrib import admin
from django import forms
from GioiThieu.models import GioiThieu
from tinymce.widgets import TinyMCE

class GioiThieuForm(forms.ModelForm):
    mo_ta_ngan = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 50}))
    mo_ta_dai = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 100}))
    class Meta:
        model = GioiThieu
        fields = '__all__'

class GioiThieuAdmin(admin.ModelAdmin):
    form = GioiThieuForm

admin.site.register(GioiThieu, GioiThieuAdmin)