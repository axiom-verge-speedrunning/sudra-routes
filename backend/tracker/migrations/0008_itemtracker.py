# Generated by Django 2.2.6 on 2019-11-28 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20191125_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTracker',
            fields=[
                ('main_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='item_info', serialize=False, to='tracker.TrackerInformation')),
            ],
        ),
    ]
