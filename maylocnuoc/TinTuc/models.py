from django.db import models
from tinymce import models as tinymce_models

class TinTuc(models.Model):
    tieu_de = models.CharField(max_length=1000, null=False, blank=False)
    mo_ta_ngan = models.TextField()
    mo_ta_dai = tinymce_models.HTMLField(null=True, blank=True)
