from django.db import models

class TinNhanGopY(models.Model):
    ten = models.CharField(max_length=500, null=False, blank=False)
    tin_nhan = models.TextField(null=False, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True)
    so_dien_thoai = models.CharField(max_length=100, null=True, blank=True)
    tieu_de = models.CharField(max_length=500, null=True, blank=True)
    ngay_tao = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.ten

class DangKySubscribe(models.Model):
    email = models.CharField(max_length=100, null=True, blank=True)
    ngay_tao = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.email
