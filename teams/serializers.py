from rest_framework import serializers
from . import models

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team

class PlayerSerializer(serializers.ModelSerializer):
    team_alias = serializers.SerializerMethodField('get_team')

    class Meta:
        model = models.Player
        fields = ('id', 'name', 'team', 'owner', 'team_alias', )
        write_only_fields = ('team', )

    def get_team(self, obj):
        return obj.team.name.upper()