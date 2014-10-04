# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20141004_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('foreign_team', models.ForeignKey(to='teams.Team', related_name='foreign_team')),
                ('home_team', models.ForeignKey(to='teams.Team', related_name='home_team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
