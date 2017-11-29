# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_hash', models.CharField(blank=True, max_length=100, null=True)),
                ('access_token', models.CharField(blank=True, max_length=100, null=True)),
                ('scope', models.CharField(blank=True, max_length=100, null=True)),
                ('admin_storeuser_id', models.IntegerField(blank=True, null=True)),
                ('storeusers', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bc_id', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('storeusers', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
