# Generated by Django 3.1.6 on 2021-03-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210317_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_ip_address',
            field=models.CharField(default='1.1.1.1', max_length=16),
        ),
    ]
