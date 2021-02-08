# Generated by Django 3.1.6 on 2021-02-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['-language'], 'verbose_name': 'Language', 'verbose_name_plural': 'Languages'},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='featured_image',
            field=models.ImageField(upload_to='images', verbose_name='Featured Image'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='langs',
            field=models.ManyToManyField(blank=True, to='pages.Language', verbose_name='languages'),
        ),
    ]