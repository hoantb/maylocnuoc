# Generated by Django 4.2 on 2023-04-09 05:56

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DichVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=1000)),
                ('mo_ta_ngan', tinymce.models.HTMLField(blank=True, null=True)),
                ('mo_ta_dai', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
    ]
