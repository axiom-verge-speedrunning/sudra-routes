# Generated by Django 2.2.8 on 2019-12-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20191210_2359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ('pk',)},
        ),
        migrations.AddField(
            model_name='tutorial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
