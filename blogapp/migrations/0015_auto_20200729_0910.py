# Generated by Django 3.0.5 on 2020-07-29 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_auto_20200729_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/%y/%m/%d'),
        ),
    ]
