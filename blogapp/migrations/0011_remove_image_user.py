# Generated by Django 3.0.5 on 2020-07-28 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20200728_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
    ]
