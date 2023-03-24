from django.db import models
from TheLoai.models import TheLoai
from tinymce import models as tinymce_models

class SanPham(models.Model):
    ten = models.CharField(max_length=500, null=False, blank=False)
    hinh_anh = models.ImageField(null=True, blank=True)
    the_loai = models.ForeignKey(TheLoai, null=False, blank=False, on_delete=models.CASCADE)
    gia = models.FloatField(null=True, blank=True, default=0)
    don_vi_tien = models.CharField(max_length=10, null=True, blank=True, default="VND")
    mo_ta_ngan = models.TextField(null=True, blank=True)
    mo_ta_dai = tinymce_models.HTMLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.ten
