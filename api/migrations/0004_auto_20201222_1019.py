# Generated by Django 2.2.10 on 2020-12-22 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201221_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='last_login',
            name='wallet_balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='last_login',
            name='last_login',
            field=models.DateField(default=datetime.date(2020, 12, 22)),
        ),
    ]
