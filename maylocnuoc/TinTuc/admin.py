from django.contrib import admin
from django import forms
from TinTuc.models import TinTuc
from tinymce.widgets import TinyMCE

class TinTucForm(forms.ModelForm):
    mo_ta_dai = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 100}))
    class Meta:
        model = TinTuc
        fields = '__all__'

class TinTucAdmin(admin.ModelAdmin):
    form = TinTucForm

admin.site.register(TinTuc, TinTucAdmin)