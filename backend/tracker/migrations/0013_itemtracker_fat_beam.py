# Generated by Django 2.2.6 on 2019-11-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_itemtracker_note_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtracker',
            name='fat_beam',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
