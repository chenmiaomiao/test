# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_employee_relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=10)),
                ('employee_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='client_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=10)),
                ('client_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='employee_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10)),
                ('employee_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='fund_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_id', models.CharField(max_length=10)),
                ('net_value', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='order_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=10)),
                ('fund_id', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=1000000000)),
                ('order_date', models.DateField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='submitted_tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10)),
                ('client_id', models.CharField(max_length=10)),
                ('quantity', models.FloatField(max_length=1000000000)),
                ('order_date', models.CharField(max_length=10)),
                ('register_date', models.CharField(max_length=10)),
                ('confirmation_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='task_factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10)),
                ('factor', models.CharField(max_length=10)),
                ('task_valid_date', models.DateField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='task_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_id', models.CharField(max_length=10)),
                ('start_date', models.DateField(max_length=10)),
                ('end_date', models.DateField(max_length=10)),
                ('order_type', models.CharField(max_length=10)),
                ('fund_valid_date', models.DateField(max_length=10)),
            ],
        ),
    ]