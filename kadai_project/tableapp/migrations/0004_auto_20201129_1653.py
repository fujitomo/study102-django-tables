# Generated by Django 3.1.3 on 2020-11-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0003_sexmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sexmodel',
            name='image',
        ),
        migrations.AlterField(
            model_name='kimetsucharactormodel',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='イメージ画像'),
        ),
    ]
