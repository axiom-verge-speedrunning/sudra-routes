# Generated by Django 2.2.8 on 2020-03-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0002_auto_20200310_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='title',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
