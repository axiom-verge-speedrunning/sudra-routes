# Generated by Django 2.2.6 on 2019-11-29 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0016_itemtracker_scissorbeam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemtracker',
            old_name='scissorBeam',
            new_name='scissor_beam',
        ),
    ]
