# Generated by Django 4.1.3 on 2023-01-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='imege.jpg', upload_to='blog/img/%Y', verbose_name='Изображения'),
            preserve_default=False,
        ),
    ]