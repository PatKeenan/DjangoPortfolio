# Generated by Django 3.1.6 on 2021-02-05 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210205_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image_description',
            field=models.CharField(default='', max_length=400, verbose_name='Image Description'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_description',
            field=models.CharField(default='', max_length=400, verbose_name='Image Description'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='github_link',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Github Link'),
        ),
    ]
