# Generated by Django 3.1.6 on 2021-02-04 16:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210204_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
