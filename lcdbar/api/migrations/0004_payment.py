# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-23 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181023_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]