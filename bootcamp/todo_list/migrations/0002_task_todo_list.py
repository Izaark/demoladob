# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='todo_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todo_list.TodoList'),
            preserve_default=False,
        ),
    ]
