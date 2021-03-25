# Generated by Django 3.1.6 on 2021-03-17 15:41

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210315_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scripts',
            name='script_file',
            field=models.FileField(blank=True, default='scripts/', null=True, upload_to=accounts.models.Scripts.get_file_path),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='script_size',
            field=models.IntegerField(blank=True),
        ),
    ]
