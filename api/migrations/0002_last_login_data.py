# Generated by Django 2.2.10 on 2020-12-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='last_login',
            name='data',
            field=models.TextField(null=True),
        ),
    ]
