# Generated by Django 3.1.6 on 2021-02-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20210211_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(blank=True, default=False, verbose_name='Featured Post'),
        ),
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(blank=True, default=False, verbose_name='Featured Post'),
        ),
    ]