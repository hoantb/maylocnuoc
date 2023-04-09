from django.db import models
from tinymce import models as tinymce_models

class GioiThieu(models.Model):
    mo_ta_ngan = tinymce_models.HTMLField(null=True, blank=True)
    mo_ta_dai = tinymce_models.HTMLField(null=True, blank=True)
