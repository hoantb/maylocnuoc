from django.db import models

class TheLoai(models.Model):
    ten = models.CharField(max_length=500, null=False, blank=False)
