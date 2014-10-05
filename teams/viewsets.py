from rest_framework.viewsets import ModelViewSet
from . import models
from . import permisssions
from . import serializers

class TeamViewSet(ModelViewSet):
    model = models.Team
    serializer_class = serializers.TeamSerializer
    permission_classes = (permisssions.IsOwnerPermission, )

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.filter(owner=self.request.user)

class PlayerViewSet(ModelViewSet):
    permission_classes = (permisssions.IsOwnerPermission, )
    queryset = models.Player.objects.all()
    
    def get_serializer_class(self):
        # Use a different serializer for read and write operations
        if self.request.method in ('GET', ):
            return serializers.PlayerReadOnlySerializer
        else:
            return serializers.PlayerSerializer

class TournamentViewSet(ModelViewSet):
    model = models.Tournament
    permission_classes = (permisssions.IsOwnerPermission, )


class RoundViewSet(ModelViewSet):
    model = models.Round
    permission_classes = (permisssions.IsOwnerPermission, )

