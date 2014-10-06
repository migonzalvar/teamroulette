# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20141004_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('foreign_team', models.ForeignKey(related_name='foreign_team', to='teams.Team')),
                ('home_team', models.ForeignKey(related_name='home_team', to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
