# Generated by Django 3.1.3 on 2020-11-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0002_auto_20201129_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='sexmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
