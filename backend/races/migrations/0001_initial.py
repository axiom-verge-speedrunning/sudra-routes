# Generated by Django 2.2.8 on 2020-03-10 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('start_time', models.BigIntegerField(blank=True, null=True)),
                ('started', models.BooleanField(null=True)),
                ('commentator_name', models.CharField(blank=True, max_length=256, null=True)),
                ('game_name', models.CharField(blank=True, max_length=256, null=True)),
                ('extra_information', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('end_time', models.BigIntegerField(blank=True, null=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runners', to='races.Race')),
            ],
        ),
    ]