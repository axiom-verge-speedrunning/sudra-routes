# Generated by Django 2.2.6 on 2019-11-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20191128_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtracker',
            name='lab_coat',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
