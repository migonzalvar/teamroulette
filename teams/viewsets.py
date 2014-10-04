from rest_framework.viewsets import ModelViewSet
from . import models
from . import permisssions
from . import serializers

class TeamViewSet(ModelViewSet):
    model = models.Team
    permission_classes = (permisssions.IsOwnerPermission, )

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.filter(owner=self.request.user)


class PlayerViewSet(ModelViewSet):
    model = models.Player
    serializer_class = serializers.PlayerSerializer
    permission_classes = (permisssions.IsOwnerPermission, )


class TournamentViewSet(ModelViewSet):
    model = models.Tournament
    permission_classes = (permisssions.IsOwnerPermission, )
