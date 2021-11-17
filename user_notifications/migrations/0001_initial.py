# Generated by Django 3.1.13 on 2021-11-16 18:06

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.manager
import user_notifications.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='Notification Name')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('display_type', models.IntegerField(choices=[(100, 'Bootstrap Alert'), (200, 'Modal')], default=100, verbose_name='Message Type')),
                ('message', models.JSONField(blank=True, default=user_notifications.models.set_default_message, null=True, verbose_name='Message Content')),
                ('deliver_once', models.BooleanField(default=True, verbose_name='Deliver Once')),
                ('start_date', models.DateTimeField(blank=True, help_text='Notification Start Date?', null=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, help_text='Notification End Date?', null=True, verbose_name='End Date')),
                ('rules', models.JSONField(blank=True, default=list, null=True)),
                ('meta', models.JSONField(blank=True, default=dict, null=True)),
                ('sites', models.ManyToManyField(blank=True, related_name='notifications', to='sites.Site', verbose_name='Sites')),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
