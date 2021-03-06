# Generated by Django 3.1.6 on 2021-02-05 16:07

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210204_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-category'],
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('brief_desription', models.CharField(max_length=100, verbose_name='Brief Description')),
                ('featured_image', models.ImageField(upload_to='images', verbose_name='Featured Image')),
                ('github_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Github Link')),
                ('project_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='ProjectLink')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('cats', models.ManyToManyField(blank=True, to='pages.Category', verbose_name='category')),
                ('langs', models.ManyToManyField(blank=True, to='pages.Language', verbose_name='languages')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
    ]
