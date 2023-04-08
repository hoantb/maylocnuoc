from django.db import models

class TheLoai(models.Model):
    ten = models.CharField(max_length=500, null=False, blank=False)
    hien_thi_trang_chu =models.BooleanField(null=True, default=False)

    def __str__(self) -> str:
        return self.ten