# Generated by Django 3.0.5 on 2020-07-29 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0012_auto_20200728_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(default=None, upload_to='images/%y/%m/%d'),
        ),
    ]
