# Generated by Django 2.2.6 on 2019-11-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20191125_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackerinformation',
            name='max_health',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]