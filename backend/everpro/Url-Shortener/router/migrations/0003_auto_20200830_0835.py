# Generated by Django 3.1 on 2020-08-30 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0002_auto_20200830_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='short_url',
            new_name='key',
        ),
    ]