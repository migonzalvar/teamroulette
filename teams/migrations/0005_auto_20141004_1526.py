# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0004_team_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, default=None)),
                ('teams', models.ManyToManyField(to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, default=None),
            preserve_default=True,
        ),
    ]
