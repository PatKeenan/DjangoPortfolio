# Generated by Django 3.1.6 on 2021-02-05 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20210205_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='brief_desription',
            new_name='desription',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='brief_desription',
            new_name='desription',
        ),
    ]
