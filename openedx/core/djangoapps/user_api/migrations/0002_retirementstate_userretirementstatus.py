# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetirementState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30, unique=True)),
                ('state_execution_order', models.SmallIntegerField(unique=True)),
                ('is_dead_end_state', models.BooleanField(db_index=True, default=False)),
                ('required', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('state_execution_order',),
            },
        ),
        migrations.CreateModel(
            name='UserRetirementStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('original_username', models.CharField(db_index=True, max_length=150)),
                ('original_email', models.EmailField(db_index=True, max_length=254)),
                ('original_first_name', models.CharField(blank=True, max_length=30)),
                ('original_last_name', models.CharField(blank=True, max_length=150)),
                ('retired_username', models.CharField(db_index=True, max_length=150)),
                ('retired_email', models.EmailField(db_index=True, max_length=254)),
                ('responses', models.TextField()),
                ('current_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_state', to='user_api.RetirementState')),
                ('last_state', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_state', to='user_api.RetirementState')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Retirement Status',
                'verbose_name_plural': 'User Retirement Statuses',
            },
        ),
    ]
