# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DecimalField(decimal_places=6, max_digits=9)),
                ('y', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapsapps.Coordinate')),
            ],
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('speed_limit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoadCoord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('coordinate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapsapps.Coordinate')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapsapps.Road')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='coord_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coord_1', to='mapsapps.Coordinate'),
        ),
        migrations.AddField(
            model_name='building',
            name='coord_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coord_2', to='mapsapps.Coordinate'),
        ),
        migrations.AddField(
            model_name='building',
            name='coord_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coord_3', to='mapsapps.Coordinate'),
        ),
        migrations.AddField(
            model_name='building',
            name='coord_4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coord_4', to='mapsapps.Coordinate'),
        ),
        migrations.AlterUniqueTogether(
            name='roadcoord',
            unique_together=set([('road', 'sequence')]),
        ),
    ]
