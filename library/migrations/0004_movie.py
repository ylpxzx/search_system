# Generated by Django 2.2.2 on 2019-06-07 01:28

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20190603_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=4, verbose_name='评分')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('movie_url', models.URLField(verbose_name='电影链接')),
                ('image', models.ImageField(blank=True, upload_to=library.models.custom_path, verbose_name='电影封面')),
                ('info', models.TextField(verbose_name='简介')),
            ],
            options={
                'verbose_name': '电影',
                'verbose_name_plural': '电影',
            },
        ),
    ]
