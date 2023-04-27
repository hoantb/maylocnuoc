from django.db import models


class SlideTrangChu(models.Model):
    hinh_anh = models.ImageField(null=True, blank=True, upload_to='giao-dien')

class HinhTrangGioiThieu(models.Model):
    hinh_anh = models.ImageField(null=True, blank=True, upload_to='giao-dien')

class HinhTrangLienHe(models.Model):
    hinh_anh = models.ImageField(null=True, blank=True, upload_to='giao-dien')