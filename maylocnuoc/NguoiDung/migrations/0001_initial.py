# Generated by Django 4.1.7 on 2023-03-29 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TinNhanGopY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=500)),
                ('tin_nhan', models.TextField()),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('so_dien_thoai', models.CharField(blank=True, max_length=100, null=True)),
                ('tieu_de', models.CharField(blank=True, max_length=500, null=True)),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]