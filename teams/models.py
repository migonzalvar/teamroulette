from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, default=None, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team)
    owner = models.ForeignKey(User, default=None, null=True)

    def __str__(self):
        tpl = '{} ({})'
        args = self.name, self.team
        return tpl.format(*args)


class Tournament(models.Model):
    name = models.CharField(max_length=128)
    teams = models.ManyToManyField(to=Team)
    owner = models.ForeignKey(User, default=None, null=True)

    def __str__(self):
        return self.name







