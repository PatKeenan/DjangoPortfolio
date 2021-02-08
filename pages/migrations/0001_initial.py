# Generated by Django 3.1.6 on 2021-02-04 15:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 's',
                'ordering': ['-language'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('featured_image', models.CharField(max_length=900, verbose_name='Featured Image')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('github_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Github Link')),
                ('project_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='ProjectLink')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
                ('langs', models.ManyToManyField(blank=True, null=True, to='pages.Language', verbose_name='languages')),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
                'ordering': ['-date_added'],
            },
        ),
    ]