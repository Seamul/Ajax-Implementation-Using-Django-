# Generated by Django 3.0.5 on 2020-07-29 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_image_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
