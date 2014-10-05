from rest_framework import serializers
from . import models

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team

class PlayerSerializer(serializers.ModelSerializer):
    """Generic serializer."""
    class Meta:
        model = models.Player
        fields = ('id', 'name', 'team', 'owner', )

class PlayerReadOnlySerializer(serializers.ModelSerializer):
    """Read only serializer."""
    team = TeamSerializer()

    class Meta:
        model = models.Player
        fields = ('id', 'name', 'team', 'owner', )
